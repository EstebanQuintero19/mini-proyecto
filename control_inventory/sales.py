from dataclasses import dataclass, field
from decimal import Decimal
from datetime import datetime
import json

@dataclass
class Sale:
    # representa una venta individual
    product_name: str
    quantity: int
    unit_price: Decimal
    total: Decimal
    sale_date: datetime = field(default_factory=datetime.now)

class Sales:
    def __init__(self, inventory):
        self.sales_history = []  # historial de ventas
        self.inventory = inventory  # referencia al inventario para actualizar stock
    
    def register_sale(self, product_name, quantity):
        # registrar una venta y actualizar el inventario
        product = self.inventory.find_by_name(product_name)
        if not product:
            return False
        
        # validar cantidad
        if quantity <= 0:
            print("Error: La cantidad debe ser mayor a cero.")
            return False
        
        # verificar stock suficiente
        if product.quantity < quantity:
            print(f"Error: Stock insuficiente. Disponible: {product.quantity}")
            return False
        
        # calcular total de la venta
        total = product.price * quantity
        
        # crear registro de venta
        sale = Sale(
            product_name=product.name,
            quantity=quantity,
            unit_price=product.price,
            total=total
        )
        self.sales_history.append(sale)
        
        # actualizar stock en el inventario
        product.quantity -= quantity
        
        print(f"Venta registrada: {quantity} unidades de {product.name}")
        print(f"Total: ${total}")
        print(f"Stock restante: {product.quantity}")
        
        # alertas de stock
        if product.quantity == 0:
            print("ALERTA: Producto sin stock!")
        elif product.quantity < 5:
            print("ADVERTENCIA: Stock bajo")
        
        return True
    
    def get_top_selling_products(self, limit=5):
        # mostrar productos más vendidos basado en el historial
        if not self.sales_history:
            print("No hay ventas registradas.")
            return
        
        # agrupar ventas por producto
        sales_by_product = {}
        for sale in self.sales_history:
            if sale.product_name in sales_by_product:
                sales_by_product[sale.product_name] += sale.quantity
            else:
                sales_by_product[sale.product_name] = sale.quantity
        
        # ordenar por cantidad vendida
        sorted_sales = sorted(sales_by_product.items(), key=lambda x: x[1], reverse=True)
        top_sales = sorted_sales[:limit]
        
        print(f"\n=== TOP {min(limit, len(top_sales))} PRODUCTOS MÁS VENDIDOS ===")
        for i, (product_name, total_sold) in enumerate(top_sales, 1):
            # buscar stock actual
            product = self.inventory.find_by_name(product_name)
            stock = product.quantity if product else "N/A"
            print(f"{i}. {product_name} - {total_sold} unidades vendidas | Stock actual: {stock}")
    
    def get_sales_report(self):
        # reporte general de ventas
        if not self.sales_history:
            print("No hay ventas registradas.")
            return
        
        total_revenue = Decimal("0.00")
        total_units = 0
        
        print("\n=== REPORTE DE VENTAS ===")
        for sale in self.sales_history:
            fecha = sale.sale_date.strftime("%d/%m/%Y %H:%M")
            print(f"{fecha} | {sale.product_name} | {sale.quantity} unidades | ${sale.total}")
            total_revenue += sale.total
            total_units += sale.quantity
        
        print(f"\nTotal de ventas: {len(self.sales_history)}")
        print(f"Unidades vendidas: {total_units}")
        print(f"Ingresos totales: ${total_revenue}")
    
    def save_to_file(self, filename):
        # guardar historial de ventas en JSON
        try:
            sales_data = []
            for sale in self.sales_history:
                sale_dict = {
                    'product_name': sale.product_name,
                    'quantity': sale.quantity,
                    'unit_price': str(sale.unit_price),  # Decimal a string
                    'total': str(sale.total),  # Decimal a string
                    'sale_date': sale.sale_date.isoformat()  # datetime a string ISO
                }
                sales_data.append(sale_dict)
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(sales_data, f, indent=2, ensure_ascii=False)
            print(f"Historial de ventas guardado en {filename}")
        except Exception as e:
            print(f"Error al guardar ventas: {e}")
    
    def load_from_file(self, filename):
        # cargar historial de ventas desde JSON
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                sales_data = json.load(f)
            
            self.sales_history = []
            for data in sales_data:
                sale = Sale(
                    product_name=data['product_name'],
                    quantity=data['quantity'],
                    unit_price=Decimal(data['unit_price']),  # string a Decimal
                    total=Decimal(data['total']),  # string a Decimal
                    sale_date=datetime.fromisoformat(data['sale_date'])  # string ISO a datetime
                )
                self.sales_history.append(sale)
            print(f"Historial de ventas cargado desde {filename}: {len(self.sales_history)} ventas")
        except FileNotFoundError:
            print("Archivo de ventas no encontrado. Iniciando historial vacío.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON de ventas.")
        except Exception as e:
            print(f"Error al cargar ventas: {e}")
