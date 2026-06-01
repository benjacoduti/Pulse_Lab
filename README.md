# Pulse\_Lab



Descripción: Pulse Lab - tut: 4 - grupo: 6 - UdeSA
Integrantes : Matias Friedenbach, Benjamin Coduti, Ramiro Yoffe, Augusto Elías


Análisis de datos y calculo de métricas con información ECG



##### Errores y validación


En la carga de datos se utiliza pandas para leer el CSV, normalizar los tipos de datos y validar la información antes de calcular métricas.
Los errores considerados son:
- Archivo inexistente o nombre de archivo no válido
- CSV inválido o con columnas distintas a las requeridas
- Campos vacíos o valores nulos
- Tipo de dato str en un casillero int/float/bool
- Valores negativos o no correspondientes con el dato solicitado segun su casillero
- Categorías no permitidas en fase, condición experimental o hit
- Tiempos no crecientes para un mismo participante
- Cantidad insuficiente de picos QRS para calcular frecuencia cardíaca
- Momento en el que el promedio de la distancia entre los picos es 0 y al calcular la frecuencia cardiaca (uno sobre el promedio) causa una division por cero

Se informa cual es el tipo de dato o validación que esta en falla.
En la interfaz web, los errores de validación se muestran con `st.error` y el programa se detiene para evitar mostrar resultados incorrectos.



##### Programa en objetos



El sistema utilizaría únicamente la clase Participante, dejando la coordinación general en el main. En este caso, la clase Participante tendría como atributos el id y las listas con los datos: tiempos, valores, fase, condición experimental y hit. Tiene como métodos de cálculo : calcular\_promedio\_senal(), calcular\_frecuencia\_cardiaca() y calcular\_fc\_desde\_datos().Estos métodos utilizarían directamente funciones de los módulos del sistema. Por ejemplo, para calcular la frecuencia cardíaca, se llamaría a detectar\_picos\_qrs() y luego a calcular\_frecuencia\_cardiaca(). Para otras métricas, se usarían funciones del módulo de métricas y, en caso de ser necesario, funciones del módulo de procesamiento de datos.

El main se encargaría del funcionamiento “general” del programa: llamaría a cargar\_datos() para obtener la información, aplicaría funciones de validación de datos para verificarla, crearía los objetos Participante y luego llamaría sus métodos para calcular y mostrar los resultados.



##### Implementación de Pandas



Implementaríamos pandas para poder leer los datasets, para poder operar con los dataframes y series de una forma más sencilla, y para poder mostrar la información de una manera mucho más fácil.

Las funciones que deberíamos cambiar para la implementación de pandas son:

* abrir\_archivo
* parsear\_lineas
* cargar\_datos
* calcular\_frecuencia\_cardiaca
* calcular\_fc\_desde\_datos
* calcular\_promedio\_senal
* calcular\_minimo\_senal
* calcular\_maximo\_senal
* calcular\_amplitud\_senal
* filtrar\_por\_participante
* validar\_tiempos\_ordenados



Estas funciones deberían cambiar ya que, al operar con un tipo de dato distinto (dataframes y series en lugar de listas y diccionarios) es necesario cambiar la forma de iterar, acceder a valores y mostrarlos. A su vez, se debería cambiar el docstring de esas funciones (al menos en cuanto a los parámetros y retornos)


##### Guía de Ejecución de la Interfaz Web



Para poder ejecutar la interfaz web, primero se debe asegurar de contar con streamlit instalado en su entorno. Para poder instalarlo y probarlo, se utilizan los siguientes comandos en consola:



pip install streamlit

streamlit hello



Una vez instalado, se puede correr la interfaz a través de utilizar el siguiente comando en consola:



streamlit run app.py




