from validacion_datos import pedir_id

def filtrar_por_participante(datos: list) -> dict:
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
    i=0
    
    id_participante = pedir_id()
        
    while i <len(datos): 
        
        if datos[i]["id"] == id_participante:
            return datos[i]
        else:
            i += 1
    
    raise Exception("No se encontró participante alguno con el id ingresado - Se detectó en filtrar_por_participante")

