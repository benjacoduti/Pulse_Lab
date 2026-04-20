# Pulse_Lab
Descripcion: Pulse Lab - tut: 4 - grupo: 6 - UdeSA
Integrantes : Matias Friedenbach, Benjamin Coduti, Ramiro Yoffe, Augusto Elias
Analisis de datos y calculo de metricas con informacion ECG
Errores y validacion:
En el parseo de datos, al momento de castear al tipo correcto, se utiliza un bloque try except para levantar errores de casteo especificos.
Los tipos de errores (ValueError) considerados son:
-) Una columna de dato del participante vacia 
-) Tipo de dato str en un casillero int/float
-) Valores negativos o no correspondientes con el dato solicitado segun su casillero
-) Momento en el que el promedio de la distancia entre los picos es 0 y al calcular la frecuencia cardiaca (uno sobre el promedio) causa una division por cero 
Se infomra cual es el tipo de dato que esta en falla. 

Programa en objetos:
El sistema utiliza únicamente la clase Participante, deja la coordinación general en el main. En este caso, la clase Participante tendría como atributos el id y las listas con los datos: tiempos, valores, fase, condición experimental y hit. Tiene como métodos de cálculo : calcular_promedio_senal(), calcular_frecuencia_cardiaca() y calcular_fc_desde_datos().Estos métodos utilizarían directamente funciones de los módulos del sistema. Por ejemplo, para calcular la frecuencia cardíaca, se llamaría a detectar_picos_qrs() y luego a calcular_frecuencia_cardiaca(). Para otras métricas, se usarían funciones del módulo de métricas y, en caso de ser necesario, funciones del módulo de procesamiento de datos.

El main se encargaría del funcionamiento “general” del programa: llamaría a cargar_datos() para obtener la información, aplicaría funciones de validación de datos para verificarla, crearía los objetos Participante y luego llamaria sus métodos para calcular y mostrar los resultados. (O pondríamos las funciones directamente acá en el main y no como método de la clase (A definir))
