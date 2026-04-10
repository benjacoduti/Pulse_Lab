# Conversión de datos de tipo string a float

def to_float_or_str(dato):
    """
    Recibe un string e intenta castearlo a float
    En caso de poder, develve el valor convertido; en caso de no poder, devuelve el mismo dato recibido

    Parameters
    ----------
    dato : str
        Texto recibido

    Returns
    -------
    dato : float si el dato puede convertirse en float
    dato : str si el dato no puede convertirse en float

    """
    try:
        return float(dato)
    except ValueError:
        return dato

def validar_dato(dato, i):
    """
    Recibe un dato perteneciente a una linea del archivo y su posicion y valida los tipos de los datos
    :param dato: Un dato especifico de la linea
    :return: Linea del archivo validada y casteada al tipo de dato correspondiente
    """
    try:
        if i < 3:
            if i == 0:
                dato = int(dato)
            elif i == 1 or i==2:
                dato = float(dato)
            if dato > 0:
                return dato
            else:
                raise ValueError("El dato es negativo")
        elif i == 3:
            if dato == "tarea" and dato == "baseline":
                return dato
            else:
                raise ValueError(f"El dato en la posicion {i+1} no es una de las opciones validas")
        elif i == 4:
            if dato == "cooperacion" and dato == "competencia":
                return dato
            else:
                raise ValueError(f"El dato en la posicion {i+1} no es una de las opciones validas")
        elif i == 5:
            if dato == "True":
                return True
            elif dato == "False":
                return False
            else:
                raise ValueError
    except ValueError:
        raise  ValueError(f"El dato en la posicion {i+1} no es del tipo especificado")