from src.validacion_datos import to_float_or_str

# Abrir Archivo

def abrir_archivo(ruta:str)->list:
    """
    Recibe la ruta de un archivo;
    Abre el archivo para poder leerlo;
    Luego cierra el archivo y devuelve las líneas

    El archivo es de tipo csv y contiene todos los datos ordenados, sin
    #ninguno faltante

    Parameters
    ----------
    ruta : str
        Ruta en la que se encuentra el archivo que se quiere abrir

    Returns
    -------
    lineas : list
        Lista que contiene strings correspondientes a las filas del archivo

    """
    archivo = open(ruta,"r")
    lineas = archivo.readlines()
    archivo.close()
    
    return lineas

# Parsear Datos

def parsear_linea(linea:str)->list:
    """
    Recibe una línea de un archivo y la devuelve modificada;
    Se encarga de separar la línea en campos y convertir la data en el tipo
    que corresponde

    Parameters
    ----------
    linea : str
        Línea que será parseada

    Returns
    -------
    linea_parseada : list
        Lista que contiene los datos convertidos de la lista parseada

    """
    linea_parseada = []
    linea = linea.strip("\n")
    data_linea = linea.split(",") #!!! split con (",") o (";") ?
    
    for dato in data_linea:
        linea_parseada.append(to_float_or_str(dato))
    return linea_parseada

# Cargar Datos

def cargar_datos(ruta:str)->list:
    """
    Recibe la ruta de un archivo y se la envía a la función abrir_archivo para que extraiga
    la información;
    Luego, por cada línea de información, llama a la función parsear_linea para poder
    castear los diferentes tipos de datos y eliminar impurezas de la línea;
    Finalmente, genera un diccionario con un registro de los participantes
    por cada participante con distinto id, y lo actualiza hasta finalizar el recorrido
    de las líneas del archivo.
    Guarda los registros de los participantes en una lista y la devuelve

    Parameters
    ----------
    ruta : str
        Ruta con la que se abrirá el archivo del cual se extraerán los datos

    Returns
    -------
    datos : list
        Lista que contiene diccionarios con los datos divididos por participantes;
        #!!! Hace falta agregar qué contiene?

    """
    datos = []
    id_anterior = None # Flag creada para la posterior comparación entre id's
    i = 1 # No tomamos en cuenta los headings
    lineas = abrir_archivo(ruta)
    
    while i < len(lineas):
        linea_parseada = parsear_linea(lineas[i])

        i_d = int(linea_parseada[0])
        tiempo = linea_parseada[1]
        valor = linea_parseada[2]
        fase = linea_parseada[3]
        condicion_experimental = linea_parseada[4]
        hit = linea_parseada[5]

        #Creación del diccionario
        if i_d != id_anterior:
            registro_participante = {} # Quitando el id, el resto de valores se guarda en listas
            
            registro_participante["id"] = i_d
            registro_participante["tiempo"] = [tiempo]
            registro_participante["valor"] = [valor]
            registro_participante["fase"] = [fase]
            registro_participante["condicion_experimental"] = [condicion_experimental]
            registro_participante["hit"] = [hit]
            
            id_anterior = i_d
            datos.append(registro_participante)
        
        # Actualización del diccionario
        else:
            registro_participante["tiempo"].append(tiempo)
            registro_participante["valor"].append(valor)
            registro_participante["fase"].append(fase)
            registro_participante["condicion_experimental"].append(condicion_experimental)
            registro_participante["hit"].append(hit)
        
        i+=1
    
    return datos
        
