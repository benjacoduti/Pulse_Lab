import os
import tempfile
from pathlib import Path

import streamlit as st

from src.carga_datos import cargar_datos
from src.metricas import (
    calcular_promedio_senal,
    calcular_minimo_senal,
    calcular_maximo_senal,
    calcular_amplitud_senal,
    calcular_fc_desde_datos,
)
from src.graficos import (
    verificar_carpeta_grafico,
    graficar_hits_por_fase,
    graficar_senal_por_fase
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

verificar_carpeta_grafico()

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

tab1, tab2 = st.tabs([
    "Señal por fase",
    "Hits por fase"
])

with tab1:
    graficar_senal_por_fase(df)

    ruta_grafico = Path(os.getcwd()) / 'graficos' / 'grafico_señal_por_fase.png'

    if ruta_grafico.exists():
        st.image(str(ruta_grafico), caption="Distribución de señal por fase")
    else:
        st.error(f"No se encontró el gráfico esperado: {ruta_grafico}")

with tab2:
    graficar_hits_por_fase(df)
    
    ruta_grafico = Path(os.getcwd()) / 'graficos' / 'grafico_hits_por_fase.png'

    if ruta_grafico.exists():
        st.image(str(ruta_grafico), caption="Distribución de señal por fase")
    else:
        st.error(f"No se encontró el gráfico esperado: {ruta_grafico}")
