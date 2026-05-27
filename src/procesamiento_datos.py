import pandas as pd

from src.validacion_datos import pedir_id

def filtrar_por_participante(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recibe una lista con registros de participantes en donde se desea buscar;
    filtra al participante cuyo id sea igual al ingresado por consola

    Parameters
    ----------
    datos : list
        Lista de registros en donde buscar el participante
        
    Returns
    -------
    dict
        Registro del participante buscado
        
    Raises
    ------
    ValueError
        si no se encuentra en la lista de registros
    Exception
        No hay participante con ese id ingresado
    """
    try:
        participante = pedir_id(df)
    except ValueError as e:
        raise ValueError(e)
    else:
        return participante

