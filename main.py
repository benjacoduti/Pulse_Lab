from graficos import graficar_por_fase
from src.carga_datos import cargar_datos
from src.metricas import calcular_fc_desde_datos, calcular_maximo_senal, calcular_minimo_senal, calcular_amplitud_senal, calcular_promedio_senal
from src.procesamiento_datos import filtrar_por_participante
from src.graficos import verificar_carpeta_grafico

nombre_archivo = 'PulseLab_mock_data.csv'

try:
    datos = cargar_datos(nombre_archivo)

    verificar_carpeta_grafico()

    # promedio = calcular_promedio_senal(datos)
    # fc = calcular_fc_desde_datos(datos)
    # senal_max, senal_min = calcular_maximo_senal(datos), calcular_minimo_senal(datos)
    # amplitud = calcular_amplitud_senal(datos)

    participante = filtrar_por_participante(datos)
    graficar_por_fase(datos)
    # fc_participante = calcular_fc_desde_datos(participante)
    # promedio_participante = calcular_promedio_senal(participante)
    # max_participante = calcular_maximo_senal(participante)
    # min_participante = calcular_minimo_senal(participante)
    # amplitud_participante = calcular_amplitud_senal(participante)
except ValueError as e:
    print("[ERROR CRITICO] Tipo de error: ValueError. Descripción:", e)
except TypeError as e:
    print("[ERROR CRITICO] Tipo de error: TypeError. Descripción:", e)
except ZeroDivisionError as e:
    print("[ERROR CRITICO] Tipo de error: ZeroDivisionError. Descripción:",e)
except Exception as e:
    print ("[ERROR INESPERADO] Tipo de error: Exception. Descripción:", e)
else:
    # print(f'El promedio de la senal es: {promedio}')
    # print(f'La frequencia cardiaca promedio es de {fc}Hz')
    # print(f'El maximo de la señal es de {senal_max} y el minimo es de {senal_min}\n')
    #Especifico a un participante
    print(f'Se encontro a un participante con el id {participante["id"]}')
    print(f'| El promedio del participante {participante["id"]} es de {promedio_participante}\n'
          f'| Su maximo es de {max_participante}\n'
          f'| Su minimo es de {min_participante}\n'
          f'| Su amplitud es de {amplitud_participante}\n'
          f'| Su frequencia es de {fc_participante}Hz')