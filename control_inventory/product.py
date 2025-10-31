from dataclasses import dataclass, field
from decimal import Decimal
from datetime import datetime

@dataclass
class Product:
    # dataclass que genera automáticamente __init__, __repr__, __eq__
    name: str = ""
    category: str = ""
    price: Decimal = Decimal("0.00")  # Decimal para precios exactos
    quantity: int = 0
    created_at: datetime = field(default_factory=datetime.now)  # fecha y hora de creación automática