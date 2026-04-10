def detectar_picos_qrs(tiempos: list, senal: list, umbral: float = 0.9, distancia_minima: float = 0.3) -> list:
    """
    Detecta picos en la señal ECG.
    Parámetros:
    - tiempos: lista de tiempos
    - senal: lista de valores de la señal
    - umbral: valor mínimo para considerar un pico
    - distancia minima: tiempo mínimo entre picos
    Retorna:
    - lista de tiempos donde ocurren los picos
    """
    if umbral <= 0:
    
        raise ValueError ("El umbral no puede ser menor o igual a 0 - El error proviene de la funcion detectar_picos_qrs")
    
    if distancia_minima <= 0:
        
        raise ValueError("La distancia minima no puede ser menor o igual a 0 - El error proviene de la funcion detectar_picos_qrs")
    
    tiempos_picos=[]
    for i in range(len(tiempos)): # se puede usar .extend
        for k in range(len(tiempos[i])):
            if senal[i][k] >= umbral:
                if len(tiempos_picos)==0:
                    tiempos_picos.append(tiempos[i][k])
                elif tiempos[i][k] - tiempos_picos[-1] > distancia_minima:
                    tiempos_picos.append(tiempos[i][k])

    return tiempos_picos