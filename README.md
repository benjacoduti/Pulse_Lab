# Pulse_Lab
Descripcion: Pulse Lab - tut: 4 - grupo: 6 - UdeSA
Integrantes : Matias Friedenbach, Benjamin Coduti, Ramiro Yoffe, Augusto Elias
Analisis de datos y calculo de metricas con informacion ECG
Errores y validacion:
En el parseo de datos, al momento de castear al tipo correcto, se utiliza un bloque try except para levantar errores de casteo especificos.
Los tipos de errores (ValueError) considerados son:
-) Una columna de dato del participante vacia 
-) Tipo de dato str en un casillero int/float
-) Un archivo scv completamente vacio
-) Valores negativos o no correspondientes con el dato solicitado segun su casillero
