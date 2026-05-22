import os

def verificar_carpeta_grafico():
    if not  os.path.exists('./graficos'):
        os.mkdir('./graficos')