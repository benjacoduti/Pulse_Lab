# Diseño del proyecto Pulse_Lab

## Descripción general

Pulse_Lab es un proyecto en Python para cargar, validar, procesar y analizar datos de señales ECG. El sistema trabaja con archivos CSV ubicados en la carpeta `datos/`, transforma la información en un `DataFrame` de pandas, calcula métricas sobre la señal y genera gráficos en la carpeta `graficos/`.

El programa está organizado como un pipeline simple:

1. Cargar el archivo CSV.
2. Normalizar los tipos de datos.
3. Validar estructura, rangos y categorías.
4. Pedir un participante por consola.
5. Calcular métricas de señal ECG.
6. Detectar picos QRS para estimar frecuencia cardíaca.
7. Generar gráficos de análisis.
8. Mostrar resultados por consola.

## Arquitectura

El proyecto sigue una arquitectura modular. El archivo `main.py` funciona como coordinador general y delega las responsabilidades específicas a módulos dentro de `src/`.

```text
main.py
  |
  |-- src/carga_datos.py
  |     |-- abre archivos CSV
  |     |-- normaliza tipos
  |     |-- llama a validaciones
  |
  |-- src/validacion_datos.py
  |     |-- valida columnas
  |     |-- valida rangos numéricos
  |     |-- valida categorías
  |     |-- valida orden temporal por participante
  |
  |-- src/procesamiento_datos.py
  |     |-- pide un id por consola
  |     |-- filtra datos por participante
  |
  |-- src/metricas.py
  |     |-- calcula promedio, mínimo, máximo y amplitud
  |     |-- calcula frecuencia cardíaca
  |
  |-- src/utils_ecg.py
  |     |-- detecta picos QRS
  |
  |-- src/graficos.py
        |-- crea la carpeta de gráficos
        |-- genera visualizaciones
```

## Flujo de ejecución

El flujo principal empieza en `main.py`:

1. Se define el archivo de entrada: `PulseLab_mock_data.csv`.
2. Se llama a `cargar_datos()`.
3. Se verifica que exista la carpeta `graficos/`.
4. Se pide al usuario el id de un participante.
5. Se filtran los registros del participante elegido.
6. Se calculan estas métricas:
   - promedio de señal
   - señal máxima
   - señal mínima
   - amplitud de señal
   - frecuencia cardíaca
7. Se generan gráficos:
   - señal vs. tiempo para el participante
   - distribución de señal por fase
   - cantidad de hits por fase
8. Se imprimen los resultados.

El programa usa bloques `try/except` para informar errores críticos de validación, tipos, división por cero u otros errores inesperados.

## Modelo de datos

Los datos se representan con un `DataFrame` de pandas. Las columnas esperadas son:

```text
id
tiempo
senal
fase
condicion_experimental
hit
```

Tipos esperados:

| Columna | Tipo esperado | Descripción |
|---|---:|---|
| `id` | entero | Identificador del participante |
| `tiempo` | float | Tiempo de la medición |
| `senal` | float | Valor de la señal ECG |
| `fase` | string | Fase experimental |
| `condicion_experimental` | string | Condición del experimento |
| `hit` | booleano | Resultado o acierto del registro |

Categorías válidas:

| Columna | Valores permitidos |
|---|---|
| `fase` | `baseline`, `tarea` |
| `condicion_experimental` | `cooperacion`, `competencia` |
| `hit` | `True`, `False` |

Reglas principales de validación:

- El archivo no puede tener campos vacíos o valores nulos.
- `id` debe ser entero positivo.
- `tiempo` no puede ser negativo y debe estar ordenado crecientemente por participante.
- `senal` debe estar entre 0 y 2.
- Las columnas categóricas solo pueden contener valores permitidos.

## Responsabilidades por módulo

### `main.py`

Es el punto de entrada del sistema. Coordina la carga de datos, el filtrado por participante, el cálculo de métricas, la generación de gráficos y el manejo general de errores.

### `src/carga_datos.py`

Se encarga de leer y preparar los datos.

Funciones principales:

- `resolver_ruta_datos(nombre_archivo)`: resuelve la ubicación del archivo, usando `datos/` como carpeta por defecto cuando se recibe solo el nombre del CSV.
- `abrir_archivo(nombre_archivo)`: lee el CSV con pandas y asigna las columnas esperadas.
- `normalizar_datos(df)`: convierte las columnas a los tipos definidos por el sistema.
- `cargar_datos(nombre_archivo)`: integra apertura, detección de nulos, normalización y validación.

### `src/validacion_datos.py`

Centraliza las validaciones del `DataFrame`.

Funciones principales:

- `validar_df(df)`: ejecuta todas las validaciones generales.
- `validar_columna_entero_positivo(df, columna)`: verifica enteros positivos.
- `validar_columna_mayor_a_num(df, columna, num)`: verifica que una columna no tenga valores menores al mínimo permitido.
- `validar_columna_categorias(df, categorias, columna)`: verifica pertenencia a categorías válidas.
- `validar_tiempos_ordenados(df, id_col, tiempo_col)`: verifica que los tiempos crezcan por participante.

### `src/procesamiento_datos.py`

Contiene lógica de interacción y filtrado.

Funciones principales:

- `pedir_id(df)`: solicita por consola un id válido y busca el participante.
- `filtrar_por_participante(df)`: devuelve los registros del participante seleccionado.

### `src/metricas.py`

Calcula métricas numéricas sobre la señal.

Funciones principales:

- `calcular_frecuencia_cardiaca(picos)`: calcula la frecuencia cardíaca como la inversa del promedio de distancia entre picos.
- `calcular_fc_desde_datos(df)`: detecta picos QRS y calcula la frecuencia desde los datos del participante.
- `calcular_promedio_senal(df)`: promedio de la señal.
- `calcular_minimo_senal(df)`: mínimo de la señal.
- `calcular_maximo_senal(df)`: máximo de la señal.
- `calcular_amplitud_senal(df)`: diferencia entre máximo y mínimo.

### `src/utils_ecg.py`

Incluye utilidades específicas para el análisis ECG.

Función principal:

- `detectar_picos_qrs(tiempos, senal, umbral, distancia_minima, debug)`: detecta picos QRS usando derivada, energía de señal, suavizado y un umbral adaptativo.

### `src/graficos.py`

Genera visualizaciones con matplotlib.

Funciones principales:

- `verificar_carpeta_grafico()`: crea `graficos/` si no existe.
- `graficar_hits_por_fase(df)`: genera un gráfico de barras con hits por fase.
- `graficar_senal_tiempo_participante(df_participante)`: grafica la señal en función del tiempo para un participante.
- `graficar_senal_por_fase(df)`: genera un boxplot de señal por fase.

## Estructura de archivos

```text
Pulse_Lab/
├── README.md
├── diseño.md
├── main.py
├── src/
│   ├── carga_datos.py
│   ├── validacion_datos.py
│   ├── procesamiento_datos.py
│   ├── metricas.py
│   ├── utils_ecg.py
│   └── graficos.py
├── datos/
│   ├── PulseLab_mock_data.csv
│   ├── PulseLab_mock_data_error01.csv
│   ├── PulseLab_mock_data_error02.csv
│   ├── PulseLab_mock_data_error03.csv
│   ├── PulseLab_mock_data_error04.csv
│   ├── PulseLab_mock_data_error05.csv
│   ├── PulseLab_mock_data_error06.csv
│   ├── PulseLab_mock_data_error08.csv
│   ├── PulseLab_mock_data_error09.csv
│   └── PulseLab_mock_data_error10.csv
├── graficos/
│   ├── grafico_señal_participante_4.png
│   ├── grafico_señal_por_fase.png
│   └── hits_por_fase.png
├── Diagramas/
│   ├── main.png
│   ├── carga_datos.png
│   ├── abrir_archivo.png
│   ├── filtrar_por_participante.png
│   ├── pedirID.png
│   ├── calcular_fc_desde_datos.png
│   ├── calcular_frequencia_cardiaca.png
│   ├── calcular_promedio.png
│   ├── calcular_minimo_senal.png
│   ├── Calcular_max.png
│   ├── calcular_amplitud.png
│   ├── validar_linea.png
│   └── parsear_linea.png
└── env/
```

## Decisiones de diseño

- Se usa pandas para trabajar con datos tabulares de forma más clara y compacta.
- La carga, validación, procesamiento, métricas y gráficos están separados en módulos distintos.
- `main.py` no contiene la lógica interna de cálculo; solamente coordina las funciones.
- Las validaciones se ejecutan antes de calcular métricas para evitar resultados incorrectos.
- Los gráficos se guardan como archivos PNG para dejar evidencia visual del análisis.
- La detección de picos QRS está aislada en `utils_ecg.py` porque es una operación específica del dominio ECG.

## Manejo de errores

El sistema contempla errores frecuentes:

- archivo inexistente;
- CSV inválido;
- columnas inesperadas;
- valores nulos;
- valores negativos o fuera de rango;
- categorías no permitidas;
- datos no convertibles al tipo esperado;
- tiempos no crecientes;
- cantidad insuficiente de picos QRS;
- división por cero al calcular frecuencia cardíaca.

Estos errores se propagan hacia `main.py`, donde se muestran mensajes críticos por consola.

## Salidas del sistema

El sistema produce dos tipos de salida:

1. Resultados por consola:
   - id del participante encontrado;
   - promedio de señal;
   - señal máxima;
   - señal mínima;
   - amplitud;
   - frecuencia cardíaca.

2. Archivos gráficos en `graficos/`:
   - `grafico_señal_participante_<id>.png`
   - `grafico_señal_por_fase.png`
   - `hits_por_fase.png`
