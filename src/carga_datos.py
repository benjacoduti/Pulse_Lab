import os
from pathlib import Path

import pandas as pd

from src.validacion_datos import validar_df, validar_columna_categorias


def resolver_ruta_datos(nombre_archivo: str) -> Path:
    if nombre_archivo is None or str(nombre_archivo).strip() == "":
        raise ValueError("El nombre del archivo no es valido - Se detecto en abrir_archivo")

    ruta = Path(nombre_archivo)
    if ruta.is_absolute() or ruta.exists():
        return ruta

    return Path(os.getcwd()) / "datos" / nombre_archivo


def abrir_archivo(nombre_archivo: str) -> pd.DataFrame:
    """
    Lee un CSV de datos ECG como texto crudo para que la validacion pueda
    reportar errores con valores originales y filas reales del archivo.
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
    Devuelve una copia del DataFrame con los tipos usados por el resto del sistema.
    """
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

    Retorna un DataFrame con columnas:
    id, tiempo, senal, fase, condicion_experimental y hit.
    """
    try:
        df = abrir_archivo(nombre_archivo)
        if df.isna().any().any():
            raise ValueError("Error crítico: El archivo contiene campos vacíos o valores nulos (NaN). - Se detecto en cargar_datos")
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
