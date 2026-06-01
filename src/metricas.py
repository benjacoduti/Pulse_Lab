from src.utils_ecg import detectar_picos_qrs
import pandas as pd

def calcular_frecuencia_cardiaca(picos: list) -> float:
    """
    Calcula la frecuencia cardíaca a partir de tiempos de picos detectados.
    Parameters
    ----------
    picos : list
        Tiempos en los que la señal alcanzó un pico.
    Returns
    -------
    float
        Frecuencia calculada a partir de la distancia promedio entre picos.
    Raises
    ------
    ValueError
        Si la lista contiene menos de dos picos.
    ZeroDivisionError
        Si la distancia promedio entre picos es cero.
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
    Calcula la frecuencia cardíaca desde un DataFrame de datos ECG.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con columnas de tiempo y señal ECG.
    Returns
    -------
    float
        Frecuencia cardíaca calculada.
    Raises
    ------
    ValueError
        Si el DataFrame no tiene las columnas esperadas o los datos no permiten detectar picos.
    ZeroDivisionError
        Si la distancia promedio entre picos es cero.
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en calcular_fc_desde_datos')
    try:
        picos = detectar_picos_qrs(df['tiempo'].tolist(), df['senal'].tolist(), 0.8,0.3)
        fc = calcular_frecuencia_cardiaca(picos)
    except ZeroDivisionError as e:
        raise ZeroDivisionError(e)
    except ValueError as e:
        raise ValueError(e)            
    return float(fc)

def calcular_promedio_senal(df: pd.DataFrame) -> float:
    """
    Calcula el promedio de la señal ECG.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los registros de señal ECG.
    Returns
    -------
    float
        Promedio de la columna de señal.
    Raises
    ------
    ValueError
        Si el DataFrame no tiene las columnas esperadas.
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en calcular_promedio_senal')
    
    return df['senal'].mean()

def calcular_minimo_senal(df: pd.DataFrame) -> float:
    """
    Calcula el valor mínimo de la señal ECG.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los registros de señal ECG.
    Returns
    -------
    float
        Valor mínimo de la columna de señal.
    Raises
    ------
    ValueError
        Si el DataFrame no tiene las columnas esperadas.
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en calcular_minimo_senal')
    return df["senal"].min()
    
def calcular_maximo_senal(df: pd.DataFrame) -> float:
    """
    Calcula el valor máximo de la señal ECG.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los registros de señal ECG.
    Returns
    -------
    float
        Valor máximo de la columna de señal.
    Raises
    ------
    ValueError
        Si el DataFrame no tiene las columnas esperadas.
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en calcular_maximo_senal')
    
    return df["senal"].max()

def calcular_amplitud_senal(df: pd.DataFrame) -> float:
    """
    Calcula la amplitud de la señal ECG.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los registros de señal ECG.
    Returns
    -------
    float
        Diferencia entre el valor máximo y mínimo de la señal.
    Raises
    ------
    ValueError
        Si el DataFrame no tiene las columnas esperadas.
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
   
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en calcular_amplitud_senal')
    try: 
        maximo = calcular_maximo_senal(df)
        minimo = calcular_minimo_senal(df)
    except ValueError as e:
        raise ValueError(e)
    amplitud = maximo - minimo #suponiendo que la amplitud es esto 
    return amplitud
