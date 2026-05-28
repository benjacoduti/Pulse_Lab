from src.graficos import graficar_senal_tiempo_participante, graficar_senal_por_fase
from src.graficos import graficar_por_fase
from src.carga_datos import cargar_datos
from src.metricas import calcular_fc_desde_datos, calcular_maximo_senal, calcular_minimo_senal, calcular_amplitud_senal, calcular_promedio_senal
from src.procesamiento_datos import filtrar_por_participante
from src.graficos import verificar_carpeta_grafico

nombre_archivo = 'PulseLab_mock_data.csv'

try:
    datos = cargar_datos(nombre_archivo)

    verificar_carpeta_grafico()

    participante = filtrar_por_participante(datos)
    fc_participante = calcular_fc_desde_datos(participante)
    promedio_participante = calcular_promedio_senal(participante)
    max_participante = calcular_maximo_senal(participante)
    min_participante = calcular_minimo_senal(participante)
    amplitud_participante = calcular_amplitud_senal(participante)

    graficar_senal_tiempo_participante(participante)
    graficar_senal_por_fase(datos)
    graficar_por_fase(datos)

except ValueError as e:
    print("[ERROR CRITICO] Tipo de error: ValueError. Descripción:", e)
except TypeError as e:
    print("[ERROR CRITICO] Tipo de error: TypeError. Descripción:", e)
except ZeroDivisionError as e:
    print("[ERROR CRITICO] Tipo de error: ZeroDivisionError. Descripción:",e)
except Exception as e:
    print ("[ERROR INESPERADO] Tipo de error: Exception. Descripción:", e)
else:
    print(f'| Se encontro a un participante con el id {participante['id'].iloc[0]}')
    print(f'| El promedio de señal del participante {participante['id'].iloc[0]} es de: {promedio_participante:.3f}\n'
          f'| Su máxima señal es de: {max_participante}\n'
          f'| Su mínima señal es de: {min_participante}\n'
          f'| Su amplitud es de: {amplitud_participante}\n'
          f'| Su frequencia es de: {fc_participante:.3f}Hz')