from src.validacion_datos import validar_linea

# Abrir Archivo
def abrir_archivo(ruta:str)->list:
    """
    Recibe la ruta de un archivo;
    Abre el archivo para poder leerlo;
    Luego cierra el archivo y devuelve las líneas

    El archivo es de tipo csv y contiene todos los datos ordenados, sin
    ninguno faltante

    Parameters
    ----------
    ruta : str
        Ruta en la que se encuentra el archivo que se quiere abrir

    Returns
    -------
    lineas : list
        Lista que contiene strings correspondientes a las filas del archivo

    """
    if ruta is None or ruta == "":
        raise ValueError("La ruta de archivo no es valido - Se detectó en abrir_archivo")
    try:
        archivo = open(ruta,"r")
        lineas = archivo.readlines()
        archivo.close()
    except (FileNotFoundError, Exception):
        raise FileNotFoundError("No se encuentra el archivo - Se detectó en abrir_archivo")
    else:
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
    linea_parseada = linea.split(",") #!!! split con (",") o (";") ?

    # Si usásemos validar dato:

    #for i in range(0, len(data_linea)):
    #    dato_valido = validar_dato(data_linea[i], i)
    #    linea_parseada.append(dato_valido)
        
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
    lineas = abrir_archivo(ruta)

    for linea in lineas:
        linea_parseada = parsear_linea(linea)
        linea_valida = validar_linea(linea_parseada)

        i_d = (linea_valida[0])
        tiempo = linea_valida[1]
        valor = linea_valida[2]
        fase = linea_valida[3]
        condicion_experimental = linea_valida[4]
        hit = linea_valida[5]

        registro_participante = None

        for p in datos:
            if p["id"] == i_d:
                registro_participante = p
                break

        #Creación del diccionario
        if registro_participante is None:
            registro_participante = {
                "id": i_d,
                "tiempo": [],
                "valor": [],
                "fase": [],
                "condicion_experimental": [],
                "hit": []
            }
            datos.append(registro_participante)

        # Actualización del diccionario
        registro_participante["tiempo"].append(tiempo)
        registro_participante["valor"].append(valor)
        registro_participante["fase"].append(fase)
        registro_participante["condicion_experimental"].append(condicion_experimental)
        registro_participante["hit"].append(hit)
    
    return datos