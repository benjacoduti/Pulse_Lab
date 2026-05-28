from src.utils_ecg import detectar_picos_qrs
import pandas as pd

def calcular_frecuencia_cardiaca(picos: list) -> float:
    """
    Recibe una lista de tiempos en los que sucedieron picos en la señal, calcula y devuelve la frequencia de estos eventos.
    :param
        -picos: list de floats - lista de tiempos en los que la señal alcanzo un pico

    :return:
        -float con la frequencia de estos eventos.
        
    :raises: ZeroDivisionError si la distancia promedio entre picos es 0
             ValueError cuando el número de picos es menor a 2
    """
    if len(picos) < 2:
        raise ValueError("El numero de picos debe ser mayor que 2 - Se detecto en calcular_frecuencia_cardiaca")
    else:
        picos = pd.DataFrame(picos)
        promedio = picos.diff().mean().iloc[0]
        try:
            return 1 / promedio #La frequencia la calculamos como 1 sobre el promedio de distancia entre picos
        except:
            raise ZeroDivisionError("Se dividió por 0 debido a que la distancia promedio entre picos es 0 - Se detectó en calcular_frecuencia_cardiaca")
            
def calcular_fc_desde_datos(df: pd.DataFrame) -> float:
    """
    Recibe una lista de diccionarios correspondientes a cada participante. 
    (Puede calcular las métricas en función de un único participante también, si se pasa el diccionario dentro de una lista)
    Crea listas con todos los tiempos y señales de todos los participantes. Utiliza la función detectar_picos_qrs para conseguir todos los picos de la señal
    Utiliza la función calcular_frecuencia_cardiaca para calcular frequencia cardiaca promedio de todos los participantes.
    :param
        -datos: lista de diccionarios correspondientes a cada participante.
    :return:
        -float con la frequencia promedio de todos los participantes.
        
    :raises: ValueError si la lista se encuentra vacía
             Propaga errores de calcular_frecuencia_car´diaca y de detectar_picos_qrs
    
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en normalizar datos')
    try:
        picos = detectar_picos_qrs(df['tiempo'].tolist(), df['senal'].tolist(), 0.8,0.3)
        fc = calcular_frecuencia_cardiaca(picos)
    except ZeroDivisionError as e:
        raise ZeroDivisionError(e)
    except ValueError as e:
        raise ValueError(e)            
    return fc.astype('float64')

def calcular_promedio_senal(df) -> float:
    """
    Recibe un lista de los registros de los participantes, analiza sus datos y guarda las señales de cada participante.
    (Puede calcular las métricas en función de un único participante también, si se pasa el diccionario dentro de una lista)
    Finalmente, calcula un promedio de señales totales en base a los datos de todos los participantes.

    Parameters
    ----------
    datos : list
        lista con registros de participantes

    Returns
    -------
    promedio : float
        Promedio de señales totales

    Raises: ValueError si no hay datos de los participantes

    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en normalizar datos')
    
    return df['senal'].mean()

def calcular_minimo_senal(df) -> float:
    """
    Calcula el valor mínimo de la señal ECG.
    (Puede calcular las métricas en función de un único participante también, si se pasa el diccionario dentro de una lista)
    Parmetr.:
    datos : (list)
        Lista de diccionarios, donde cada diccionario contiene un valor de señal en la clave valor
    Retorna:
    minimo : float
        El valor mínimo de la señal.
        
    Raises: ValueError si la lista se encuentra vacía
    
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en normalizar datos')
    return df["senal"].min()
    
def calcular_maximo_senal(df) -> float:
    """
    Calcula el valor máximo de la señal ECG.
    (Puede calcular las métricas en función de un único participante también, si se pasa el diccionario dentro de una lista)
    Parametros:
    datos : list
           Lista de diccionarios, donde cada diccionario contiene un valor de señal en la clave "valor".
    Retorna:
    maximo : float
        El valor máximo de la señal.
        
    Raises: ValueError si la lista se encuentra vacía
        
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en normalizar datos')
    
    return df["senal"].max()

def calcular_amplitud_senal(df) -> float:
    """
    Calcula la amplitud de la señal ECG.
    La amplitud se define como la diferencia entre el valor máximo y el valor mínimo.
    Parmet.:
    datos : list
            Lista de diccionarios, donde cada diccionario contiene un valor de señal en la clave "valor".
    Retorna:
    amplitud : float
            La amplitud de la señal.
        
    Raises: Propaga errores de calcular maximo y minimo senal 
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en normalizar datos')
    try: 
        maximo = calcular_maximo_senal(df)
        minimo = calcular_minimo_senal(df)
    except ValueError as e:
        raise ValueError(e)
    amplitud = maximo - minimo #suponiendo que la amplitud es esto 
    return amplitud