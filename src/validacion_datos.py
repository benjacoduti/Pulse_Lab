def validar_linea(linea:list) ->list:
    """
    Válida una línea recibida y castea a diferentes tipos de datos si es posible
    Los datos se encuentran ordenados por posición, lo que vuelve posible
    el castearlos según la posición en la que se encuentren.

    Parameters
    ----------
    linea : list
        Linea parseada a revisar

    Returns
    -------
    linea : list
        Linea con los datos correspondientes casteados

    Raises
    ------
        ValueError si el casteo no puede llevarse a cabo
    """
    try:
        dato = "id"
        i_d = linea[0]
        validar_entero_positivo(i_d, dato)

        dato = "tiempo"
        tiempo = linea[1]
        validar_entero_positivo(tiempo, dato)

        dato = "señal"
        valor = linea[2]
        validar_entero_positivo(valor, dato)

        dato = "fase"
        fase = linea[3]
        validar_string_categorias(fase, ['baseline', 'tarea'], dato)

        dato = "condición experimental"
        condicion_experimental = linea[4]
        validar_string_categorias(condicion_experimental, ['cooperación', 'competencia'], dato)

        dato = "hit"
        hit = linea[5]
        validar_string_categorias(hit, ['True', 'False'], dato)
    except ValueError as e:
        raise ValueError(e)
    else:
        return linea

def pedir_id():
    """
    Pide al usuario por consola un id que debe ser un numero entero positivo.
    :return: id de participante valido
    """
    while True:
        try:
            i_d = int(input("Ingrese el id del participante: "))
            if validar_entero_positivo(i_d, "Id ingresado") == True:
                return i_d
        
        except ValueError:
            print('Error, el id del participante debe ser un numero')

def validar_entero_positivo(num, nombre_campo):
    """
    Chequea que el numero sea entero postivo     
    :param num: Int
    :param nombre_campo: str que corresponde a la categoria del dato que se busca validar 
    :return: Devuelve True si lo valida correctamente o raisea el error si no
    :raise: Value error si el numero es negativo 
            
    """
    if num < 0:
        raise ValueError(f'Error, el valor de {nombre_campo} no puede ser negativo - se detecto en validar_entero_positivo')
    else:
        return True
        
def validar_string_categorias(valor, categorias, nombre_del_campo):
    '''
    Chequea que el valor este en las categorias
    valor : str es el valor a chequear
    categorias : lista de str con los posibles valores a chequear
    nombre_del_campo : str que corresponde a la categoria del dato que se busca validar 
    Raises: Value error si el valor no esta en categorias
    Returns: Devuelve True si lo valida correctamente o raisea el error si no

    '''
    
    if valor not in categorias:
        raise ValueError(f'El valor de {nombre_del_campo} debe ser {categorias} - se detecto en validar_string_categorias')  
    else:
         return True