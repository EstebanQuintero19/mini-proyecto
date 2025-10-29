from product import Product
from decimal import Decimal

class Inventory:
    def __init__(self):
        self.products = []  # inicializa una lista vacía de productos

    def add_product(self, name: str, category: str, price: Decimal, quantity: int):
        new_product = Product(name=name, category=category, price=price, quantity=quantity)
        self.products.append(new_product) # se agregaría a la lista
        print(f"Producto agregado: {new_product.name}")

    def list_products(self):
        if not self.products: # verificar que si está vavía
            print("Inventario vacío.")
            return
        for p in self.products: # mostraría los 
            print(f"{p.name} | {p.category} | {p.price} | {p.quantity}")

    def find_by_name(self, name: str):
        for p in self.products:
            if p.name.lower() == name.lower(): # búsqueda ignorando las mayúsculas/minúsculas
                return p
        print("Producto no encontrado.") 
