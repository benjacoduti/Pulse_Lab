import pandas as pd

from src.validacion_datos import validar_columna_entero_positivo


def pedir_id(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pide al usuario por consola un id que debe ser un número entero positivo.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los registros de participantes.
    Returns
    -------
    pd.DataFrame
        Registros del participante cuyo id fue ingresado.
    """
    while True:
        try:
            i_d = int(input("Ingrese el id del participante: "))
            data = pd.DataFrame({'Id ingresado': [i_d]})
            if validar_columna_entero_positivo(data, "Id ingresado"):
                participante = df[df['id'] == i_d]
                if participante.size == 0:
                    print(f'No se encontró participante alguno con el id ingresado {i_d} - Se detectó en filtrar_por_participante')
                else:
                    return participante
        except ValueError:
            print('Error, el id del participante debe ser un numero entero positivo')

def filtrar_por_participante(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra los registros del participante cuyo id se ingresa por consola.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los registros de participantes.
    Returns
    -------
    pd.DataFrame
        Registros del participante seleccionado.
    Raises
    ------
    ValueError
        Si ocurre un error de validación al pedir el id.
    """
    try:
        participante = pedir_id(df)
    except ValueError as e:
        raise ValueError(e)
    else:
        return participante
