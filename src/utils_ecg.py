import os

import numpy as np

def detectar_picos_qrs(tiempos: list, senal: list, umbral: float =0.8, distancia_minima: float =0.3, debug: bool=False):
    """
    Detecta picos QRS en una señal ECG.
    Parameters
    ----------
    tiempos : list
        Tiempos de la señal en segundos.
    senal : list
        Valores de la señal ECG.
    umbral : float
        Sensibilidad usada para calcular el umbral local.
    distancia_minima : float
        Tiempo mínimo permitido entre picos detectados.
    debug : bool
        Indica si se muestra un gráfico auxiliar de energía y umbral.
    Returns
    -------
    list
        Tiempos donde se detectan picos QRS.
    Raises
    ------
    ValueError
        Si las listas tienen distinto largo, están vacías o el registro es demasiado corto.
    """

    # ---------------------------
    # Validación básica
    # ---------------------------
    if len(tiempos) != len(senal):
        raise ValueError("El tiempo y la señal deben tener el mismo largo - Se detectó en detectar_picos_qrs")

    if len(tiempos) == 0 or len(senal) == 0:
        raise ValueError("Las listas 'tiempos' y 'senal' no pueden estar vacías - Se detectó detectar_picos_qrs")

    # if np.any(np.diff(tiempos) <= 0):
    #     raise ValueError("Los valores de 'tiempos' deben estar ordenados de forma creciente - Se detectó en detectar_picos_qrs")

    if len(tiempos) < 3:
        raise ValueError("Tiempo de registro demasiado corto para detectar picos - Se detectó en detectar_picos_qrs")


    t = np.array(tiempos)
    x = np.array(senal)

    # ---------------------------
    # 0. Parámetros
    # ---------------------------

    # Frecuencia de muestreo estimada
    dt = np.diff(t)
    dt_medio = np.median(dt)

    # Ventanas expresadas en segundos y convertidas a muestras
    ventana_energia_seg = 0.03      # ~30 ms para suavizado de la señal
    ventana_umbral_seg = 2.0        # ~2 s para el umbral adaptativo
    padding_seg = 0.05              # ~50 ms

    window = max(1, int(round(ventana_energia_seg / dt_medio)))
    ventana_umbral = max(3, int(round(ventana_umbral_seg / dt_medio)))
    window = min(window, len(x))
    ventana_umbral = min(ventana_umbral, len(x))
    padding = max(1, int(round(padding_seg / dt_medio)))

    # ---------------------------
    # 1. Derivada + energía
    # ---------------------------
    dx = np.diff(x, prepend=x[0])
    energia = dx ** 2

    # ---------------------------
    # 2. Suavizado (30 ms)
    # ---------------------------
    energia_suavizada = np.convolve(
        energia,
        np.ones(window) / window,
        mode='same'
    )

    # ---------------------------
    # 3. Umbral adaptativo (2 seg)
    # ---------------------------
    media_local = np.convolve(
        energia_suavizada,
        np.ones(ventana_umbral) / ventana_umbral,
        mode='same'
    )

    var_local = np.convolve(
        (energia_suavizada - media_local) ** 2,
        np.ones(ventana_umbral) / ventana_umbral,
        mode="same"
    )

    std_local = np.sqrt(
        var_local
    )

    umbral_local = media_local + umbral * std_local

    # ---------------------------
    # 4. Detectar regiones
    # ---------------------------
    candidatos = np.where(energia_suavizada > umbral_local)[0]

    if len(candidatos) == 0:
        if debug:
            import matplotlib.pyplot as plt
            plt.figure(figsize=(12, 4))
            plt.plot(t, energia_suavizada, label="Energía suavizada")
            plt.plot(t, umbral_local, label="Umbral local", color="red")
            plt.title("Señal de energía + umbral local")
            plt.xlabel("Tiempo (s)")
            plt.legend()
            plt.show()
        return []

    grupos = []
    grupo_actual = [candidatos[0]]

    for i in candidatos[1:]:
        if i == grupo_actual[-1] + 1:
            grupo_actual.append(i)
        else:
            grupos.append(grupo_actual)
            grupo_actual = [i]

    grupos.append(grupo_actual)

    # ---------------------------
    # 5. Buscar pico real
    # ---------------------------
    picos = []
    ultimo_t = -np.inf

    for g in grupos:

        inicio = max(0, g[0] - padding)
        fin = min(len(x), g[-1] + padding + 1)

        idx_max = np.argmax(x[inicio:fin]) + inicio
        tiempo_pico = t[idx_max]

        if (tiempo_pico - ultimo_t) >= distancia_minima:
            picos.append(float(tiempo_pico))
            ultimo_t = tiempo_pico

    # ---------------------------
    # Debug opcional
    # ---------------------------
    if debug:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(12,4))
        plt.plot(t, energia_suavizada, label="Energía")
        plt.plot(t, umbral_local, label="Umbral local", color='red')
        plt.legend()
        plt.title("Energía + umbral")
        plt.xlabel("Tiempo (s)")
        plt.show()

    return picos

def verificar_script_streamlit():
    """
    Verifica que exista la carpeta donde se guardan los gráficos.
    """
    if not  os.path.exists('app.py'):
        raise FileNotFoundError("No existe el script app.py para la ejecucion de streamlit")
