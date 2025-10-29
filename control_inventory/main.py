from decimal import Decimal
from inventory import Inventory

def main():
    inv = Inventory()

    while True:
        print("\n=== MENÚ DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = Decimal(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            inv.add_product(nombre, categoria, precio, cantidad)
        elif opcion == "2":
            inv.list_products()
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            producto = inv.find_by_name(nombre)
            if producto:
                print(producto)
        elif opcion == "4":
            print("salir")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
