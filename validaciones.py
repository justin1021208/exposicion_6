#validaciones.py
# Responsabilidad: Capturar e inspeccionar los datos ingresados por el usuario.

def solicitar_texto(mensaje):
    """
    Solicita un texto al usuario y valida que no quede vacío.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        print("   Error: El texto no puede estar vacío. Intente de nuevo.")

def solicitar_entero_positivo(mensaje, minimo=0):
    """
    Solicita un entero, valida la conversión de tipo y que sea >= minimo.
    Demuestra el uso completo de try, except y finally.
    """
    while True:
        try:
            linea = input(mensaje)
            valor = int(linea)
            if valor < minimo:
                print(f"   Error: El número debe ser mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("   Error: Debe ingresar un número entero válido (sin letras ni decimales).")
        finally:
            # Se ejecuta siempre tras intentar la entrada, garantizando la limpieza del flujo
            pass