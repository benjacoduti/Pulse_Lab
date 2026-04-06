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
        tiempos.append(d["tiempo"]) # se puede usar .extend
        senal.append(d["valor"])

    picos = detectar_picos_qrs(tiempos, senal)
    return calcular_frecuencia_cardiaca(picos)

def calcular_minimo_senal(datos: list) -> float:
    """
    Calcula el valor mínimo de la señal ECG.
    Parmetr.:
    datos : (list)
        Lista de diccionarios, donde cada diccionario contiene un valor de señal en la clave valor
    Retorna:
    minimo : float
        El valor mínimo de la señal.
    """
    valores_minimos = []
    for dato in datos:
        valores_minimos.append(min(dato["valor"]))
        
    minimo = min(valores_minimos)
    return minimo

def calcular_maximo_senal(datos: list) -> float:
    """
    Calcula el valor máximo de la señal ECG.
    Parametros:
    datos : list
           Lista de diccionarios, donde cada diccionario contiene un valor de señal en la clave "valor".
    Retorna:
    maximo : float
        El valor máximo de la señal.
    """
    valores_maximos = []
    for dato in datos:
        valores_maximos.append(max(dato["valor"]))
    
    maximo = max(valores_maximos)
    return maximo

def calcular_amplitud_senal(maximo, minimo) -> float:
    """
    Calcula la amplitud de la señal ECG.
    La amplitud se define como la diferencia entre el valor máximo y el valor mínimo.
    Parmet.:
    maximo : int/float
        Mínima señal de entre los participantes analizados
    minimo : int/float
        Mínima señal de entre los participantes analizados
    Retorna:
    amplitud : float
        La amplitud de la señal.
    """

    amplitud = maximo - minimo #suponiendo que la amplitud es esto 
    return amplitud