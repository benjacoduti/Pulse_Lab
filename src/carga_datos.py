import os
from pathlib import Path
import pandas as pd
from src.validacion_datos import validar_df, validar_columna_categorias


def resolver_ruta_datos(nombre_archivo: str) -> Path:
    """
    Resuelve la ruta desde donde se debe cargar el archivo de datos.
    Parameters
    ----------
    nombre_archivo : str
        Nombre o ruta del archivo de datos.
    Returns
    -------
    Path
        Ruta absoluta o relativa resuelta para el archivo.
    Raises
    ------
    ValueError
        Si el nombre del archivo es nulo o está vacío.
    """
    if nombre_archivo is None or str(nombre_archivo).strip() == "":
        raise ValueError("El nombre del archivo no es valido - Se detecto en abrir_archivo")

    ruta = Path(nombre_archivo)
    if ruta.is_absolute() or ruta.exists():
        return ruta

    return Path(os.getcwd()) / "datos" / nombre_archivo


def abrir_archivo(nombre_archivo: str) -> pd.DataFrame:
    """
    Lee un archivo CSV de datos ECG y asigna las columnas esperadas.
    Parameters
    ----------
    nombre_archivo : str
        Nombre o ruta del archivo CSV a leer.
    Returns
    -------
    pd.DataFrame
        Datos cargados con las columnas del sistema.
    Raises
    ------
    FileNotFoundError
        Si no se encuentra el archivo indicado.
    ValueError
        Si el nombre del archivo no es válido o el CSV no puede parsearse.
    """
    ruta = resolver_ruta_datos(nombre_archivo)

    try:
        df = pd.read_csv(ruta)
    except FileNotFoundError:
        raise FileNotFoundError("No se encuentra el archivo - Se detecto en abrir_archivo")
    except pd.errors.ParserError as error:
        raise ValueError(
            f"No se pudo leer el CSV {nombre_archivo}: {error} - Se detecto en abrir_archivo"
        )
    else:
        df.columns = ['id', 'tiempo', 'senal', 'fase', 'condicion_experimental', 'hit']
        return df

def normalizar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza los tipos de datos requeridos por el sistema.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con las columnas esperadas de datos ECG.
    Returns
    -------
    pd.DataFrame
        Copia del DataFrame con los tipos normalizados.
    Raises
    ------
    ValueError
        Si el DataFrame no tiene las columnas esperadas o contiene valores inválidos.
    TypeError
        Si algún dato no puede convertirse al tipo requerido.
    """
    categorias = ['id','tiempo','senal','fase','condicion_experimental','hit']
    
    if df is None or df.columns.tolist() != categorias:
        raise ValueError('El DataFrame posee columnas distintas a las requeridas para la normalización - Se detectó en normalizar datos')
    
    datos = df.copy()
    try:
        datos["id"] = pd.to_numeric(datos["id"]).astype("int64")
        datos["tiempo"] = pd.to_numeric(datos["tiempo"]).astype("float64")
        datos["senal"] = pd.to_numeric(datos["senal"]).astype("float64")
        datos["fase"] = datos["fase"].astype("string")
        datos["condicion_experimental"] = datos["condicion_experimental"].astype("string")
        validar_columna_categorias(datos, [False, True], 'hit')
        datos["hit"] = datos["hit"].map({"True": True, "False": False}).astype("bool")
    except ValueError as e:
        raise ValueError(f'{e} - Se detecto normalizar_datos')
    except TypeError as e:
        raise TypeError(f'{e} - Se detecto normalizar_datos')
    else:
        return datos

def cargar_datos(nombre_archivo: str) -> pd.DataFrame:
    """
    Carga, valida y normaliza un archivo CSV de datos ECG.
    Parameters
    ----------
    nombre_archivo : str
        Nombre o ruta del archivo CSV a cargar.
    Returns
    -------
    pd.DataFrame
        Datos validados y normalizados.
    Raises
    ------
    FileNotFoundError
        Si no se encuentra el archivo indicado.
    ValueError
        Si el archivo contiene valores nulos o datos inválidos.
    TypeError
        Si algún dato no puede convertirse al tipo requerido.
    Exception
        Si ocurre un error no contemplado durante la carga.
    """
    try:
        df = abrir_archivo(nombre_archivo)
        if df.isna().any().any():
            raise ValueError("El archivo contiene campos vacíos o valores nulos (NaN). - Se detecto en cargar_datos")
        datos = normalizar_datos(df)
        datos_validos = validar_df(datos)
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    except ValueError as e:
        raise ValueError(e)
    except TypeError as e:
        raise TypeError(e)
    except Exception as e:
        raise Exception(e)
    else:
        return datos_validos
