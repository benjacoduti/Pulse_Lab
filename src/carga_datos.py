[from src.validacion_datos import validar_tiempos_ordenados, validar_linea
import pandas as pd
import os

# Abrir Archivo
def abrir_archivo(nombre_archivo:str)->list:
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
        
    Raises: ValueError si la ruta del archivo no es válida;
            FileNotFoundError si no se encuentra el archivo; 
            Exception para captar todo error posible

    """
    
    ruta = '../datos'
    os.chdir(ruta)
    
    if nombre_archivo is None or nombre_archivo == "":
        raise ValueError("El nombre del archivo no es valido - Se detectó en abrir_archivo")
    try:
        df = pd.read_csv(nombre_archivo)
    except (FileNotFoundError, Exception):
        raise FileNotFoundError("No se encuentra el archivo - Se detectó en abrir_archivo")
    else:
        return df

# Parsear Datos
def parsear_datos(df)->list:
    """
    Recibe una línea de un archivo y la devuelve modificada;
    Se encarga de eliminar impurezas y de separar la línea en campos 

    Parameters
    ----------
    linea : str
        Línea que será parseada

    Returns
    -------
    linea_parseada : list
        Lista que contiene los datos de la lista parseada
        
    Raises: ValueError si la línea no tiene las columnas requeridas
            Type Error si no se puede castear los datos correctamente

    """
    
    if df.count() != df.size():
        raise ValueError("Hay celdas vacías en el csv - Se detecto en parsear_dato")

    try:
        df = df.astype({'id':'int32',
                        'tiempo':'float64',
                        'senal':'float64',
                        'fase':'str',
                        'condicion_experimental':'str',
                        'hit':'str'}
                       )
        
        df['hit'] = df['hit'].map({'False': False, 'True': True})
        
        

    except (TypeError, Exception):
        raise TypeError(f"Error de tipo en {dato} - Se detectó en pasear_linea")
    else:
        return df

# Cargar Datos
def cargar_datos(nombre_archivo:str)->list:
    """
    Recibe la ruta de un archivo y se la envía a la función abrir_archivo para que extraiga
    la información;
    Luego, por cada línea de información, llama a la función parsear_linea para aplicar un parseo 
    Posteriorimente, llama a validar_linea que devuelve los datos validados y casteados.
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
        Lista que contiene diccionarios con los datos divididos por participantes
        
    Raises: propaga errores de funciones como abrir_archivo, parsear_linea y funciones de validación

    """
    try:
        df = abrir_archivo(nombre_archivo)
        df.columns = ('id','tiempo','senal','fase','condicion_experimental','hit')
        df_parseado = parsear_datos(df)
        df_validado = validar_df(df_parseado)
    except (FileNotFoundError, Exception) as e:
        raise FileNotFoundError(e)
    except ValueError as e:
        raise ValueError(e)
    except TypeError as e:
        raise TypeError(e)
    else:
        return df_validado


    # for linea in lineas:
    #     try:
    #       pass
    #     except ValueError as e: 
    #         raise ValueError(e)
    #     except TypeError as e:
    #         raise TypeError(e)
    #     else:
    
    #         i_d = (linea_valida[0])
    #         tiempo = linea_valida[1]
    #         valor = linea_valida[2]
    #         fase = linea_valida[3]
    #         condicion_experimental = linea_valida[4]
    #         hit = linea_valida[5]
    
    #         registro_participante = None
    
    #         for p in datos:
    #             if p["id"] == i_d:
    #                 registro_participante = p
    #                 break
    
    #         #Creación del diccionario
    #         if registro_participante is None:
    #             registro_participante = {
    #                 "id": i_d,
    #                 "tiempo": [],
    #                 "valor": [],
    #                 "fase": [],
    #                 "condicion_experimental": [],
    #                 "hit": []
    #             }
    #             datos.append(registro_participante)
    
    #         # Actualización del diccionario
    #         registro_participante["tiempo"].append(tiempo)
    #         registro_participante["valor"].append(valor)
    #         registro_participante["fase"].append(fase)
    #         registro_participante["condicion_experimental"].append(condicion_experimental)
    #         registro_participante["hit"].append(hit)
    # #Validar que los tiempos de cada participante esten ordenados
    # try:
    #     validar_tiempos_ordenados(datos)
    # except ValueError as e:
    #     raise ValueError(e)
    # return datos