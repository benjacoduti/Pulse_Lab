from src.carga_datos import cargar_datos
from src.metricas import calcular_fc_desde_datos, calcular_maximo_senal, calcular_minimo_senal, calcular_amplitud_senal, calcular_promedio_senal
from src.procesamiento_datos import filtrar_por_participante

ruta = './datos/PulseLab_mock_data_error01.csv'

try:
    datos = cargar_datos(ruta)

    promedio = calcular_promedio_senal(datos)
    fc = calcular_fc_desde_datos(datos)
    senal_max, senal_min = calcular_maximo_senal(datos), calcular_minimo_senal(datos)
    amplitud = calcular_amplitud_senal(senal_max, senal_min)

    print(f'El promedio de la senal es: {promedio}')
    print(f'La frequencia cardiaca promedio es de {fc}Hz')
    print(f'El maximo de la señal es de {senal_max} y el minimo es de {senal_min}')

    participante = filtrar_por_participante(datos)
    print(f'Se encontro a un participante con el id {participante["id"]}')
    fc_participante = calcular_fc_desde_datos([participante])
    promedio_participante = calcular_promedio_senal([participante])
    max_participante = calcular_maximo_senal([participante])
    min_participante = calcular_minimo_senal([participante])
    amplitud_participante = calcular_amplitud_senal(max_participante, min_participante)
    print(f'\n| El promedio del participante {participante["id"]} es de {promedio_participante}\n| Su maximo es de {max_participante}\n| Su minimo es de {min_participante}\n| Su amplitud es de {amplitud_participante}\n| Su frequencia es de {fc_participante}Hz')

except ValueError as e:
    print("[ERROR CRITICO] Tipo de error: ValueError. Descripcion:", e)
except TypeError as e:
    print("[ERROR CRITICO] Tipo de error: TypeError. Descripcion:", e)
except ZeroDivisionError as e:
    print("[ERROR CRITICO] Tipo de error: ZeroDivisionError. Descripcion:",e)
except Exception as e:
    print ("[ERROR INESPERADO] Tipo de error: Exception. Descripcion:", e)