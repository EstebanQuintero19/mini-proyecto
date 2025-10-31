from inventory import Inventory
from sales import Sales
from decimal import Decimal


def handle_option(inv: Inventory, sales: Sales, opcion: str) -> bool:
    """Ejecuta la opción indicada. Devuelve True si se debe salir del programa."""
    # opción 1: agregar producto
    if opcion == "1":
        try:
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = Decimal(input("Precio: "))  # Decimal para precisión con dinero
            cantidad = int(input("Cantidad: "))
            inv.add_product(nombre, categoria, precio, cantidad)
            # guardado automático
            inv.save_to_file("inventario.json")
        except Exception:
            print("Error: datos inválidos")

    # opción 2: listar productos
    elif opcion == "2":
        inv.list_products()

    # opción 3: buscar producto
    elif opcion == "3":
        nombre = input("Nombre del producto: ")
        producto = inv.find_by_name(nombre)
        if producto:
            print(producto)

    # opción 4: actualizar cantidad
    elif opcion == "4":
        try:
            nombre = input("Nombre del producto: ")
            if producto := inv.find_by_name(nombre):  # walrus operator
                cantidad = int(input("Nueva cantidad: "))
                inv.update_quantity(nombre, cantidad)
                # guardado automático
                inv.save_to_file("inventario.json")
            else:
                print("Producto no encontrado")
        except Exception:
            print("Error: cantidad inválida")

    # opción 5: eliminar producto
    elif opcion == "5":
        nombre = input("Nombre del producto a eliminar: ")
        if inv.delete_product(nombre):
            # guardado automático
            inv.save_to_file("inventario.json")

    # opción 6: filtrar por categoría
    elif opcion == "6":
        categoria = input("Categoría a buscar: ")
        inv.filter_by_category(categoria)

    # opción 7: filtrar por precio
    elif opcion == "7":
        try:
            min_precio = Decimal(input("Precio mínimo: "))  # Decimal para precisión
            max_precio = Decimal(input("Precio máximo: "))
            inv.filter_by_price_range(min_precio, max_precio)
        except Exception:
            print("Error: precios inválidos")

    # opción 8: estado del stock
    elif opcion == "8":
        inv.check_stock_status()

    # opción 9: valor total
    elif opcion == "9":
        inv.get_total_value()

    # opción 10: registrar venta
    elif opcion == "10":
        try:
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a vender: "))
            if sales.register_sale(nombre, cantidad):
                # guardado automático de inventario y ventas
                inv.save_to_file("inventario.json")
                sales.save_to_file("ventas.json")
        except Exception:
            print("Error: cantidad inválida")

    # opción 11: productos más vendidos
    elif opcion == "11":
        sales.get_top_selling_products()

    # opción 12: reporte de ventas
    elif opcion == "12":
        sales.get_sales_report()

    # opción 13: gráfica de inventario
    elif opcion == "13":
        inv.show_inventory_chart()

    # opción 14: guardar datos (manual)
    elif opcion == "14":
        inv.save_to_file("inventario.json")
        sales.save_to_file("ventas.json")
        print("Datos guardados.")

    # opción 15: cargar datos
    elif opcion == "15":
        inv.load_from_file("inventario.json")
        sales.load_from_file("ventas.json")

    # opción 16: salir
    elif opcion == "16":
        # salida directa (guardado automático durante las operaciones)
        print("¡Bye Bye!")
        return True

    else:
        print("Opción inválida")

    return False


def submenu_productos(inv: Inventory, sales: Sales) -> bool:
    """Submenú para opciones de productos. Devuelve True si el usuario pidió salir del programa."""
    while True:
        print("\n=== SUBMENÚ: Productos ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Filtrar por categoría")
        print("7. Filtrar por rango de precio")
        print("8. Verificar estado del stock")
        print("9. Calcular valor total")
        print("13. Gráfica de inventario")
        print("0. Volver")
        op = input("Elige una opción: ")
        if op == "0":
            return False
        if handle_option(inv, sales, op):
            return True


def submenu_ventas(inv: Inventory, sales: Sales) -> bool:
    while True:
        print("\n=== SUBMENÚ: Ventas y Reportes ===")
        print("10. Registrar venta")
        print("11. Productos más vendidos")
        print("12. Reporte de ventas")
        print("0. Volver")
        op = input("Elige una opción: ")
        if op == "0":
            return False
        if handle_option(inv, sales, op):
            return True


def submenu_datos(inv: Inventory, sales: Sales) -> bool:
    while True:
        print("\n=== SUBMENÚ: Datos y Persistencia ===")
        print("14. Guardar datos")
        print("15. Cargar datos")
        print("16. Salir")
        print("0. Volver")
        op = input("Elige una opción: ")
        if op == "0":
            return False
        if handle_option(inv, sales, op):
            return True


def submenu_todas(inv: Inventory, sales: Sales) -> bool:
    while True:
        print("\n=== TODAS LAS OPCIONES ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Filtrar por categoría")
        print("7. Filtrar por rango de precio")
        print("8. Verificar estado del stock")
        print("9. Calcular valor total")
        print("10. Registrar venta")
        print("11. Productos más vendidos")
        print("12. Reporte de ventas")
        print("13. Gráfica de inventario")
        print("14. Guardar datos")
        print("15. Cargar datos")
        print("16. Salir")
        print("0. Volver")
        op = input("Elige una opción: ")
        if op == "0":
            return False
        if handle_option(inv, sales, op):
            return True


def main():
    # crear inventario y sistema de ventas
    inv = Inventory()
    sales = Sales(inv)  # Sales necesita referencia al inventario

    # intentar cargar datos al inicio
    print("=" * 50)
    print("🔄 CARGANDO DATOS GUARDADOS...")
    print("=" * 50)
    inv.load_from_file("inventario.json")
    sales.load_from_file("ventas.json")
    print("=" * 50)
    print("✅ Sistema listo. Presiona ENTER para continuar...")
    input()

    # menú principal con apartados
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Productos")
        print("2. Ventas y Reportes")
        print("3. Datos y Persistencia")
        print("4. Todas las opciones")
        print("0. Salir")
        main_op = input("Selecciona un apartado: ")

        if main_op == "0":
            # salida directa con confirmación de guardado
            if handle_option(inv, sales, "16"):
                break
        elif main_op == "1":
            if submenu_productos(inv, sales):
                break
        elif main_op == "2":
            if submenu_ventas(inv, sales):
                break
        elif main_op == "3":
            if submenu_datos(inv, sales):
                break
        elif main_op == "4":
            if submenu_todas(inv, sales):
                break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
