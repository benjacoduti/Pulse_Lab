import pandas as pd


def validar_df(df: pd.DataFrame):
    """
    Válida una línea recibida y castea a diferentes tipos de datos si es posible
    Los datos se encuentran ordenados por posición, lo que vuelve posible
    el castearlos según la posición en la que se encuentren.

    Parameters
    ----------
    linea : list
        Linea parseada a revisar
    Raises
    ------
        ValueError si hay errores en alguna columna
        :param df:
    """
    if ~df['senal'].between(0, 2).any():
        raise ValueError('Existe una señal que no es un numero entero positivo o es mayor a 2 - Se detectó en validar_df')
    try:
        validar_columna_entero_positivo(df, "id")
        validar_columna_mayor_a_num(df, 'tiempo', 0)
        validar_columna_categorias(df, ["tarea", "baseline"], 'fase')
        validar_columna_categorias(df, ["cooperacion", "competencia"], 'condicion_experimental')
        validar_tiempos_ordenados(df)
    except ValueError as e:
        raise ValueError(e, '- Se detectó en validar_df')
    return df


def pedir_id():
    """
    Pide al usuario por consola un id que debe ser un número entero positivo.
    :return: id de participante válido
    """
    while True:
        try:
            i_d = int(input("Ingrese el id del participante: "))
            data = pd.DataFrame({'Id ingresado': i_d})
            if validar_columna_entero_positivo(data, "Id ingresado"):
                return i_d
        
        except ValueError:
            print('Error, el id del participante debe ser un numero entero positivo')

def validar_columna_entero_positivo(df, columna):
    """
    Chequea que el número sea entero postivo
    :param df: Int
    :param columna: str que corresponde a la categoria del dato que se busca validar
    :return: Devuelve True si lo valida correctamente o raisea el error si no
    :raise: Value error si el número es negativo
    """
    if (df[columna] % 1 != 0).any():
        raise ValueError(f"La columna '{columna}' contiene valores no enteros.")
    if (df[columna] <= 0).any():
        raise ValueError(f"La columna '{columna}' contiene valores no positivos.")
    return True

def validar_columna_mayor_a_num(df, columna, num):
    """
    Chequea que el número sea entero postivo
    :param df: Int
    :param columna: str que corresponde a la categoria del dato que se busca validar
    :return: Devuelve True si lo valida correctamente o raisea el error si no
    :raise: Value error si el número es negativo
    """
    if (df[columna] < num).any():
        raise ValueError(f"La columna '{columna}' contiene valores menores a {num}.")
    return True
        
def validar_columna_categorias(df, categorias, columna):
    """
    Chequea que el valor este en las categorias
    valor : str es el valor a chequear
    categorias : lista de str con los posibles valores a chequear
    nombre_del_campo : str que corresponde a la categoria del dato que se busca validar
    Raises: Value error si el valor no esta en categorias
    Returns: Devuelve True si lo valida correctamente o raisea el error si no
    """
    if (~df[columna].isin(categorias)).any():
        raise ValueError(
            f"La columna '{columna}' contiene valores fuera de {categorias}."
        )

    return True

def validar_tiempos_ordenados(df, id_col='id', tiempo_col='tiempo') -> bool:
    """
    Recibe una lista con los datos (diccionarios) de los pacientes y se fija si los tiempos están ordenados de forma creciente
    :param datos: lista con los diccionarios de cada paciente
    :return: bool True si están ordenados
    :raises: ValueError si no están ordenados los valores de tiempo de algún participante
    """
    diferencias = df.groupby(id_col)[tiempo_col].diff()

    if diferencias.le(0).any():
        raise ValueError(
            f"La columna '{tiempo_col}' contiene tiempos no crecientes."
        )

    return True