from src.utils_ecg import detectar_picos_qrs

def calcular_frecuencia_cardiaca(picos: list) -> float:
    """
    Recibe una lista de tiempos en los que sucedieron picos en la señal, calcula y devuelve la frequencia de estos eventos.
    :param
        -picos: list de floats - lista de tiempos en los que la señal alcanzo un pico

    :return:
        -float con la frequencia de estos eventos.
    """
    if len(picos) < 2:
        raise Exception("El numero de picos debe ser mayor que 2")
    else:
        periodos = []
        for i in range(len(picos) - 1):
            periodos.append(picos[i + 1] - picos[i])
        promedio = sum(periodos) / len(periodos)
        return 1 / promedio #La frequencia la calculamos como 1 sobre el promedio de distancia entre picos

def calcular_fc_desde_datos(datos: list) -> float:
    """
    Recibe una lista de diccionarios correspondientes a cada participante.
    Crea listas con todos los tiempos y señales de todos los participantes. Utiliza la función detectar_picos_qrs para conseguir todos los picos de la señal
    Utiliza la función calcular_frecuencia_cardiaca para calcular frequencia cardiaca promedio de todos los participantes.
    :param
        -datos: lista de diccionarios correspondientes a cada participante.
    :return:
        -float con la frequencia promedio de todos los participantes.
    """
    tiempos=[]
    senal=[]
    for d in datos:
        tiempos.append(d["tiempo"])
        senal.append(d["senal"])

    picos = detectar_picos_qrs(tiempos, senal)
