def validar_dato(dato, i):
    """
    Recibe un dato perteneciente a una línea del archivo y su posición y válida los tipos de los datos
    :param dato: Un dato específico de la línea
    :return:
    dato: dato validado y casteado al tipo de dato correspondiente
    :raises:
        ValueError: dependiendo del tipo de error
        IndexError: Si la posición indicada no existe
    """
    if i < 0 or i > 5:
        raise IndexError('La posición indicada no existe en la linea - Se detectó en validar_dato')
    if dato == " " or dato is None:
        raise ValueError(f"El dato en la posición {i+1} - Se detectó en validar_dato")
    elif i < 3:
        try:
            if i == 0:
                dato = int(dato)
            elif i == 1 or i == 2:
                dato = float(dato)
        except ValueError:
            raise ValueError(f"El dato en la posición {i+1} no es del tipo especificado - Se detectó en validar dato")
        else:
            if dato < 0:
                raise ValueError(f"El dato en la posición {i+1} es negativo - Se detectó en validar_dato")
            else:
                return dato
    elif i == 3:
        if dato == "baseline" or dato == "tarea":
            return dato
        else:
            raise ValueError(f"El dato en la posición {i+1} no es una de las opciones validas - Se detectó en validar_dato")
    elif i == 4:
        if dato == "cooperacion" or dato == "competencia":
            return dato
        else:
            raise ValueError(f"El dato en la posición {i+1} no es una de las opciones validas - Se detectó en validar_dato")
    elif i == 5:
        if dato == "True":
            return True
        elif dato == "False":
            return False
        else:
            raise ValueError(f"El dato en la posición {i+1} no es del tipo especificado - Se detectó en validar_dato")
    else:
        return None