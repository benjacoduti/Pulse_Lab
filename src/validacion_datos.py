import pandas as pd

def validar_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Valida que el DataFrame cumpla las reglas requeridas por el sistema.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de datos ECG a validar.
    Returns
    -------
    pd.DataFrame
        DataFrame validado.
    Raises
    ------
    ValueError
        Si alguna columna contiene valores inválidos.
    """
    if ~df['senal'].between(0, 2).all():
        raise ValueError('Existe una señal que no es un numero entero positivo o es mayor a 2 - Se detectó en validar_df')
    try:
        validar_columna_entero_positivo(df, "id")
        validar_columna_mayor_a_num(df, 'tiempo', 0)
        validar_columna_categorias(df, ["tarea", "baseline"], 'fase')
        validar_columna_categorias(df, ["cooperacion", "competencia"], 'condicion_experimental')
        validar_tiempos_ordenados(df)
    except ValueError as e:
        raise ValueError(f'{e} - Se detecto en validar_df')
    return df

def validar_columna_entero_positivo(df: pd.DataFrame, columna: str) -> bool:
    """
    Valida que una columna contenga números enteros positivos.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene la columna a validar.
    columna : str
        Nombre de la columna a validar.
    Returns
    -------
    bool
        True si la columna cumple la validación.
    Raises
    ------
    ValueError
        Si la columna contiene valores no enteros o no positivos.
    """
    if (df[columna] % 1 != 0).any():
        raise ValueError(f'La columna {columna} contiene valores no enteros.')
    if (df[columna] <= 0).any():
        raise ValueError(f'La columna {columna} contiene valores no positivos.')
    return True

def validar_columna_mayor_a_num(df: pd.DataFrame, columna: str, num: float) -> bool:
    """
    Valida que una columna no contenga valores menores a un número dado.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene la columna a validar.
    columna : str
        Nombre de la columna a validar.
    num : float
        Valor mínimo permitido.
    Returns
    -------
    bool
        True si la columna cumple la validación.
    Raises
    ------
    ValueError
        Si la columna contiene valores menores al número indicado.
    """
    if (df[columna] < num).any():
        raise ValueError(f'La columna {columna} contiene valores menores a {num}')
    return True
        
def validar_columna_categorias(df: pd.DataFrame, categorias: list, columna: str) -> bool:
    """
    Valida que los valores de una columna pertenezcan a categorías permitidas.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene la columna a validar.
    categorias : list
        Valores permitidos para la columna.
    columna : str
        Nombre de la columna a validar.
    Returns
    -------
    bool
        True si la columna cumple la validación.
    Raises
    ------
    ValueError
        Si la columna contiene valores fuera de las categorías permitidas.
    """
    if (~df[columna].isin(categorias)).any():
        raise ValueError(
            f'La columna {columna} contiene valores fuera de {categorias}.'
        )
    return True

def validar_tiempos_ordenados(df: pd.DataFrame, id_col: str ='id', tiempo_col: str ='tiempo') -> bool:
    """
    Valida que los tiempos estén ordenados de forma creciente por participante.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los registros de participantes.
    id_col : str
        Nombre de la columna que identifica al participante.
    tiempo_col : str
        Nombre de la columna con los tiempos.
    Returns
    -------
    bool
        True si los tiempos están ordenados.
    Raises
    ------
    ValueError
        Si algún participante tiene tiempos no crecientes.
    """
    diferencias = df.groupby(id_col)[tiempo_col].diff()

    if diferencias.le(0).any():
        raise ValueError(f'La columna {tiempo_col} contiene tiempos no crecientes.')
    else:
        return True