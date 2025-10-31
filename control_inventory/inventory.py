from product import Product
from decimal import Decimal
import json

class Inventory:
    def __init__(self):
        self.products = []  # lista de productos

    def save_to_file(self, filename): #guardado de datos en archivo JSON para conserver el inventario
        with open(filename, 'w') as f:
            json.dump([p.__dict__ for p in self.products], f)

    def load_from_file(self, filename): #carga de datos desde archivo JSON para 'restaurar' el inventario
        try:
            with open(filename, 'r') as f:
                products_data = json.load(f)
                self.products = [Product(**data) for data in products_data]
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except json.JSONDecodeError:
            print("Error al leer el archivo.")

    def add_product(self, name, category, price, quantity):
        # agregar nuevo producto a la lista
        try:
            new_product = Product(name=name, category=category, price=price, quantity=quantity)
            self.products.append(new_product)
            print(f"Producto agregado: {new_product.name}")
        except:
            print("Error al agregar producto")
    
    def list_products(self):
        # mostrar todos los productos
        if not self.products:
            print("Inventario vacío.")
            return
        for p in self.products:
            # formatear fecha y hora de forma legible
            fecha = p.created_at.strftime("%d/%m/%Y %H:%M:%S")
            print(f"{p.name} | {p.category} | ${p.price} | Stock: {p.quantity} | Añadido: {fecha}")
    
    def find_by_name(self, name):
        # buscar producto por nombre
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        print("Producto no encontrado.")
        return None
    
    def update_quantity(self, name, new_quantity):
        # actualizar cantidad de producto
        product = self.find_by_name(name)
        if product:
            # validar que no sea negativo
            if new_quantity < 0:
                print("Error: La cantidad no puede ser negativa.")
            else:
                product.quantity = new_quantity
                print(f"Cantidad actualizada: {new_quantity}")
                # alerta si hay poco stock
                if new_quantity == 0:
                    print("ALERTA: Sin stock!")
                elif new_quantity < 5:
                    print("ADVERTENCIA: Stock bajo")
    
    def filter_by_category(self, category):
        # mostrar productos de una categoría
        found = False
        for p in self.products:
            if p.category.lower() == category.lower():
                print(f"{p.name} | ${p.price} | Stock: {p.quantity}")
                found = True
        if not found:
            print("No hay productos en esa categoría")
    
    def filter_by_price_range(self, min_price, max_price):
        # mostrar productos en un rango de precio
        found = False
        for p in self.products:
            if min_price <= p.price <= max_price:
                print(f"{p.name} | ${p.price} | Stock: {p.quantity}")
                found = True
        if not found:
            print("No hay productos en ese rango")
    
    def check_stock_status(self):
        # ver estado del stock
        if not self.products:
            print("Inventario vacío.")
            return
        
        # separar productos según su stock
        sin_stock = []
        stock_bajo = []
        stock_normal = []
        
        for p in self.products:
            if p.quantity == 0:
                sin_stock.append(p.name)
            elif p.quantity < 5:
                stock_bajo.append(p.name)
            else:
                stock_normal.append(p.name)
        
        # mostrar resultados
        if sin_stock:
            print(f"\nSIN STOCK ({len(sin_stock)}):")
            for name in sin_stock:
                print(f"  - {name}")
        
        if stock_bajo:
            print(f"\nSTOCK BAJO ({len(stock_bajo)}):")
            for name in stock_bajo:
                print(f"  - {name}")
        
        if stock_normal:
            print(f"\nSTOCK NORMAL ({len(stock_normal)}):")
            for name in stock_normal:
                print(f"  - {name}")
    
    def get_total_value(self):
        # calcular valor total del inventario
        total = Decimal("0.00")  # Decimal para cálculos precisos
        for p in self.products:
            total += p.price * p.quantity
        print(f"\nValor total: ${total}")
        return total
    
    def delete_product(self, name):
        # eliminar un producto del inventario
        for i, p in enumerate(self.products):
            if p.name.lower() == name.lower():
                # encontré el producto, lo elimino
                deleted_product = self.products.pop(i)
                print(f"Producto eliminado: {deleted_product.name}")
                return True
        # si llego aquí, no encontré el producto
        print("Producto no encontrado.")
        return False 
