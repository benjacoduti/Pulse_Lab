from src.carga_datos import *
from src.metricas import *
from src.procesamiento_datos import *
from src.validacion_datos import *

ruta = './datos/datos_proyecto.csv'
id = '001'

datos = cargar_datos(ruta)

promedio = calcular_promedio(datos)
participante = filtrar_por_participante(datos, id)
fc = calcular_fc_desde_datos(datos)
senal_max, senal_min = calcular_max_min(datos)
amplitud = calcular_amplitud(senal_max, senal_min)

print(f'El promedio de la senal es: {promedio}')
print(f'Se encontro a un participante con el id {id}')
print(f'La frequencia cardiaca promedio es de {fc}Hz')
print(f'El maximo de la señal es de {senal_max} y el minimo es de {senal_min}')