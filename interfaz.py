# interfaz.py
# Responsabilidad: Formatear y presentar la información en la consola.

def mostrar_encabezado():
    """Imprime el título inicial del programa."""
    print("\n" + "=" * 55)
    print("   SISTEMA DE CONTROL DE INVENTARIO Y REPOSICIÓN")
    print("=" * 55)

def mostrar_reporte(nombre, disponible, minimo, habitual, necesita_reponer, sugerido):
    """
    Recibe los datos procesados e imprime el informe final formateado.
    """
    print("\n" + "-" * 55)
    print("             REPORTE DE ESTADO DE INVENTARIO")
    print("-" * 55)
    print(f"  Producto evaluado:         {nombre}")
    print(f"  Stock disponible actual:   {disponible} unidades")
    print(f"  Nivel mínimo permitido:    {minimo} unidades")
    print(f"  Lote habitual de pedido:   {habitual} unidades")
    print("-" * 55)

    if necesita_reponer:
        print("  Estado del inventario:       REPOSICIÓN NECESARIA")
        print(f"  Cantidad sugerida a pedir: {sugerido} unidades")
    else:
        print("  Estado del inventario:      INVENTARIO SUFICIENTE")
        print("  Cantidad sugerida a pedir: 0 unidades")

    print("=" * 55 + "\n")

def mostrar_mensaje_despedida():
    """Procedimiento para el cierre del programa."""
    print("¡Gracias por utilizar el sistema! Ejecución finalizada con éxito.")