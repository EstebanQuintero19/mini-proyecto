from dataclasses import dataclass, field
from decimal import Decimal
import uuid

@dataclass
class Product:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    category: str = ""
    price: Decimal = Decimal("0.00")
    quantity: int = 0