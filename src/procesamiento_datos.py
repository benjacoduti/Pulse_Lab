def filtrar_por_participante(datos: list, id_participante: int) -> dict:
    """
    Recibe una lista con registros de participantes y un id que se desea buscar; filtra al participante cuyo id sea igual al recibido

    Parameters
    ----------
    datos : list
        Lista de registros
    id_participante : int
        Id de participante solicitado

    Raises
    ------
    Exception
        No hay participante con ese id ingresado

    Returns
    -------
    dict
        Registro del participante buscado 

    """
    i=0
    while i <len(datos): 
        
        if datos[i]["id"] == id_participante:
            return datos[i]
        else:
            i += 1
    
    raise Exception("No se encontro participante alguno con el id ingresado")