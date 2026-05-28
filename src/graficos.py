import os
import pandas as pd
from matplotlib import pyplot as plt


def verificar_carpeta_grafico():
    if not  os.path.exists('./graficos'):
        os.mkdir('./graficos')

def graficar_por_fase(df: pd.DataFrame):
    promedio_señal = df.groupby('fase')['senal'].mean()
    cant_hits = df.groupby('fase')['hit'].sum()

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico promedio señal
    promedio_señal.plot(
        kind='bar',
        ax=axes[0],
        color=['#1e3a8a', '#b91c1c'],
        edgecolor='black',
        alpha=0.8
    )

    axes[0].set_title('Promedio de Señal')
    axes[0].set_xlabel('Fase')
    axes[0].set_ylabel('Señal Promedio')
    axes[0].grid(True, linestyle='--', alpha=0.5, axis='y')

    # Gráfico cantidad de hits
    cant_hits.plot(
        kind='bar',
        ax=axes[1],
        color=['#1e3a8a', '#b91c1c'],
        edgecolor='black',
        alpha=0.8
    )

    axes[1].set_title('Cantidad de Hits')
    axes[1].set_xlabel('Fase')
    axes[1].set_ylabel('Cantidad de Hits')
    axes[1].grid(True, linestyle='--', alpha=0.5, axis='y')

    plt.suptitle(
        'Comparación de Métricas por Condición Experimental',
        fontsize=13,
        fontweight='bold'
    )

    axes[0].tick_params(axis='x', rotation=0)
    axes[1].tick_params(axis='x', rotation=0)
    plt.savefig('graficos_comparacion.png', dpi=300)
    plt.show()
    plt.close()