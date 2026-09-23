# calculos.py
# Responsabilidad: Procesar algoritmos y cálculos del inventario.

def evaluar_reposicion(disponible, minimo):
    """
    Compara la cantidad disponible contra el nivel mínimo permitido.
    Retorna True si requiere reposición, False en caso contrario.
    """
    return disponible < minimo

def calcular_cantidad_sugerida(necesita_reposicion, habitual):
    """
    Determina las unidades a pedir. Si necesita reposición devuelve el lote habitual,
    de lo contrario devuelve 0.
    """
    if necesita_reposicion:
        return habitual
    else:
        return 0

def procesar_inventario(disponible, minimo, habitual):
    """""
    Función integradora que coordina las llamadas de cálculo.
    Retorna una tupla con el diagnóstico (Booleano) y la cantidad sugerida (Entero).
    """
    necesita = evaluar_reposicion(disponible, minimo)
    cantidad = calcular_cantidad_sugerida(necesita, habitual)
    return necesita, cantidad