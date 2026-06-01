import tempfile
from pathlib import Path

import streamlit as st
import matplotlib.pyplot as plt

from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (
    calcular_promedio_senal,
    calcular_minimo_senal,
    calcular_maximo_senal,
    calcular_amplitud_senal,
    calcular_fc_desde_datos,
)
from src.graficos import (
    graficar_hits_por_fase,
    graficar_senal_tiempo_participante,
    graficar_senal_por_fase,
)


st.set_page_config(
    page_title="Pulse Lab Dashboard",
    page_icon="🫀",
    layout="wide"
)

st.title("Pulse Lab")
st.write(
    "Dashboard interactivo para cargar, validar, procesar y visualizar datos ECG."
)

archivo = st.file_uploader(
    "Arrastrá o seleccioná un archivo CSV del laboratorio",
    type=["csv"]
)

if archivo is None:
    st.info("Cargá un archivo CSV para comenzar.")
    st.stop()

try:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(archivo.getbuffer())
        ruta_temporal = tmp.name

    df = cargar_datos(ruta_temporal)

except ValueError as error:
    st.error(f"Error de validación: {error}")
    st.stop()

except Exception as error:
    st.error(f"Ocurrió un error inesperado al cargar el archivo: {error}")
    st.stop()


st.success("Archivo cargado y validado correctamente.")

st.subheader("Vista previa de los datos")
st.dataframe(df.head())


st.subheader("Selección de participante")

ids_disponibles = sorted(df["id"].unique())

id_seleccionado = st.selectbox(
    "Seleccioná un participante",
    ids_disponibles
)

df_participante = df[df["id"] == id_seleccionado]


st.subheader("Indicadores clave")

try:
    promedio = calcular_promedio_senal(df_participante)
    minimo = calcular_minimo_senal(df_participante)
    maximo = calcular_maximo_senal(df_participante)
    amplitud = calcular_amplitud_senal(df_participante)
    frecuencia = calcular_fc_desde_datos(df_participante)

except ValueError as error:
    st.error(f"Error al calcular métricas: {error}")
    st.stop()

except Exception as error:
    st.error(f"Ocurrió un error inesperado al calcular métricas: {error}")
    st.stop()


col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Promedio señal", round(promedio, 3))
col2.metric("Señal mínima", round(minimo, 3))
col3.metric("Señal máxima", round(maximo, 3))
col4.metric("Amplitud", round(amplitud, 3))
col5.metric("Frecuencia cardíaca", round(frecuencia, 2))


st.subheader("Visualizaciones")

tab1, tab2, tab3 = st.tabs([
    "Señal del participante",
    "Señal por fase",
    "Hits por fase"
])

with tab1:
    st.write(f"Señal ECG del participante {id_seleccionado}")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(
        df_participante["tiempo"],
        df_participante["senal"],
        linewidth=2
    )
    ax.set_title(f"Señal en el tiempo - Participante {id_seleccionado}")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Señal")
    ax.grid(True, linestyle="--", alpha=0.5)

    st.pyplot(fig)
    plt.close(fig)

with tab2:
    st.write("Distribución de señal por fase")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.boxplot(
        [
            df[df["fase"] == "baseline"]["senal"],
            df[df["fase"] == "tarea"]["senal"]
        ],
        labels=["baseline", "tarea"],
        patch_artist=True
    )

    ax.set_title("Distribución de señal por fase")
    ax.set_xlabel("Fase")
    ax.set_ylabel("Señal")
    ax.grid(True, linestyle="--", alpha=0.5, axis="y")

    st.pyplot(fig)
    plt.close(fig)

with tab3:
    st.write("Cantidad de hits por fase")

    hits_por_fase = df.groupby("fase")["hit"].sum()

    fig, ax = plt.subplots(figsize=(8, 5))

    hits_por_fase.plot(
        kind="bar",
        ax=ax,
        edgecolor="black",
        alpha=0.8
    )

    ax.set_title("Cantidad de hits por fase")
    ax.set_xlabel("Fase")
    ax.set_ylabel("Cantidad de hits")
    ax.tick_params(axis="x", rotation=0)
    ax.grid(True, linestyle="--", alpha=0.5, axis="y")

    st.pyplot(fig)
    plt.close(fig)