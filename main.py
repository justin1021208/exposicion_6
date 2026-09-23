# main.py
# Responsabilidad: Coordinar la ejecución general invocando los módulos.

import validaciones
import calculos
import interfaz

def ejecutar_evaluacion():
    """Coordina un ciclo completo de evaluación de producto."""
    interfaz.mostrar_encabezado()

    nombre = validaciones.solicitar_texto("Ingrese el nombre del producto: ")
    disponible = validaciones.solicitar_entero_positivo("Ingrese la cantidad disponible actual: ", minimo=0)
    minimo = validaciones.solicitar_entero_positivo("Ingrese el nivel mínimo permitido: ", minimo=0)
    habitual = validaciones.solicitar_entero_positivo("Ingrese la cantidad habitual de pedido: ", minimo=1)

    necesita_reponer, sugerido = calculos.procesar_inventario(disponible, minimo, habitual)

    interfaz.mostrar_reporte(nombre, disponible, minimo, habitual, necesita_reponer, sugerido)

def main():
    """Función principal con ciclo de repetición del programa."""
    continuar = True
    while continuar:
        ejecutar_evaluacion()
        
        respuesta = input("¿Desea evaluar otro producto? (s/n): ").strip().lower()
        if respuesta != 's':
            continuar = False

    interfaz.mostrar_mensaje_despedida()

if __name__ == "__main__":
    main()