from inventory import Inventory
from decimal import Decimal

def main():
    # crear inventario
    inv = Inventory()
    
    # bucle principal
    while True:
        print("\n=== MENÚ DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Filtrar por categoría")
        print("7. Filtrar por rango de precio")
        print("8. Verificar estado del stock")
        print("9. Calcular valor total")
        print("10. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        # opción 1: agregar producto
        if opcion == "1":
            try:
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                precio = Decimal(input("Precio: "))  # Decimal para precisión con dinero
                cantidad = int(input("Cantidad: "))
                inv.add_product(nombre, categoria, precio, cantidad)
            except:
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
                if producto := inv.find_by_name(nombre):  # walrus operator ':=' assignment expression: permite asignar y usar un valor en la misma expresión. 
                    cantidad = int(input("Nueva cantidad: "))
                    inv.update_quantity(nombre, cantidad)
                else:
                    print("Producto no encontrado") 
            except:
                print("Error: cantidad inválida")
        
        # opción 5: eliminar producto
        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            inv.delete_product(nombre)
        
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
            except:
                print("Error: precios inválidos")
        
        # opción 8: estado del stock
        elif opcion == "8":
            inv.check_stock_status()
        
        # opción 9: valor total
        elif opcion == "9":
            inv.get_total_value()
        
        # opción 10: salir
        elif opcion == "10":
            print("¡Bye Bye!")
            break
        
        # opción inválida
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
