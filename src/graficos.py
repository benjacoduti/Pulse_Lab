import os
import pandas as pd
from matplotlib import pyplot as plt


def verificar_carpeta_grafico():
    """
    Verifica que exista la carpeta donde se guardan los gráficos.
    """
    if not  os.path.exists('./graficos'):
        os.mkdir('./graficos')

def graficar_hits_por_fase(df: pd.DataFrame):
    """
    Grafica la cantidad de hits por fase.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos del experimento. Debe contener las columnas
        `fase` y `hit`.

    Returns
    -------
    None
        No devuelve ningún valor.
    """
    cant_hits = df.groupby('fase')['hit'].sum()

    plt.figure(figsize=(8, 5))

    cant_hits.plot(
        kind='bar',
        color='#1e3a8a',
        edgecolor='black',
        alpha=0.8
    )

    plt.title('Cantidad de hits por fase', fontsize=13, fontweight='bold')
    plt.xlabel('Fase')
    plt.ylabel('Cantidad de hits')
    plt.xticks(rotation=0)
    plt.grid(True, linestyle='--', alpha=0.5, axis='y')
    plt.tight_layout()
    plt.savefig('./graficos/hits_por_fase.png', dpi=300)
    plt.close()

def graficar_senal_tiempo_participante(df_participante: pd.DataFrame):
    """
    Grafica la señal en función del tiempo para un único participante.
    Parameters
    ----------
    df_participante : pd.DataFrame
        DataFrame con los registros de tiempo y señal del participante.
    """
    id_participante = df_participante['id'].iloc[0]
    plt.figure(figsize=(9, 5))

    plt.scatter(
        df_participante['tiempo'],
        df_participante['senal'],
        s=40,
        alpha=0.8
    )

    plt.title(
        f'Señal en función del tiempo del participante {id_participante}',
        fontsize=13,
        fontweight='bold'
    )

    plt.xlabel('Tiempo', fontsize=11)
    plt.ylabel('Señal', fontsize=11)

    plt.grid(
        True,
        linestyle='--',
        alpha=0.5
    )

    plt.tight_layout()
    plt.savefig(f'./graficos/grafico_señal_participante_{id_participante}.png', dpi=300)
    plt.close()

def graficar_senal_por_fase(df: pd.DataFrame):
    """
    Grafica la distribución de la señal según la fase experimental.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con registros de fase y señal.
    """
    plt.figure(figsize=(9, 5))

    colores = {
        "baseline": "#1e3a8a",
        "tarea": "#7c3aed"
    }

    box = plt.boxplot(
        [
            df[df['fase'] == 'baseline']['senal'],
            df[df['fase'] == 'tarea']['senal']
        ],
        labels=['baseline', 'tarea'],
        patch_artist=True
    )

    box['boxes'][0].set_facecolor('#1e3a8a')  # baseline
    box['boxes'][1].set_facecolor('#b91c1c')  # tarea

    for patch in box['boxes']:
        patch.set_alpha(0.7)

    plt.title(
        'Distribución de señal por fase',
        fontsize=13,
        fontweight='bold'
    )

    plt.xlabel('Fase')
    plt.ylabel('Señal')

    plt.grid(
        True,
        linestyle='--',
        alpha=0.5,
        axis='y'
    )

    plt.tight_layout()
    plt.savefig('./graficos/grafico_señal_por_fase.png', dpi=300)
    plt.close()
