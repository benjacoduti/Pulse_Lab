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

def validar_registro(registro):
    
    # Esta función aparece entre las principales para entregar, hay que pensar con qué la usariamos
    
    pass