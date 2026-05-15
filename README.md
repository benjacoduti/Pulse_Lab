# Pulse\_Lab

Descripción: Pulse Lab - tut: 4 - grupo: 6 - UdeSA
Integrantes : Matias Friedenbach, Benjamin Coduti, Ramiro Yoffe, Augusto Elias
Análisis de datos y calculo de métricas con información ECG


Errores y validación:
En el parseo de datos, al momento de castear al tipo correcto, se utiliza un bloque try except para levantar errores de casteo especificos.
Los tipos de errores (ValueError) considerados son:
-) Una columna de dato del participante vacia
-) Tipo de dato str en un casillero int/float
-) Valores negativos o no correspondientes con el dato solicitado segun su casillero
-) Momento en el que el promedio de la distancia entre los picos es 0 y al calcular la frecuencia cardiaca (uno sobre el promedio) causa una division por cero
Se informa cual es el tipo de dato que esta en falla.



Programa en objetos:


El sistema utiliza únicamente la clase Participante, deja la coordinación general en el main. En este caso, la clase Participante tendría como atributos el id y las listas con los datos: tiempos, valores, fase, condición experimental y hit. Tiene como métodos de cálculo : calcular\_promedio\_senal(), calcular\_frecuencia\_cardiaca() y calcular\_fc\_desde\_datos().Estos métodos utilizarían directamente funciones de los módulos del sistema. Por ejemplo, para calcular la frecuencia cardíaca, se llamaría a detectar\_picos\_qrs() y luego a calcular\_frecuencia\_cardiaca(). Para otras métricas, se usarían funciones del módulo de métricas y, en caso de ser necesario, funciones del módulo de procesamiento de datos.

El main se encargaría del funcionamiento “general” del programa: llamaría a cargar\_datos() para obtener la información, aplicaría funciones de validación de datos para verificarla, crearía los objetos Participante y luego llamaría sus métodos para calcular y mostrar los resultados.



Implementación de Pandas:



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



Las únicas funciones que no necesitan un cambio son aquellas que reciben una lista y no datos (el df), ya que simplemente se puede cambiar el main para que esas funciones reciban una lista en lugar de una serie y funcionen correctamente. 

