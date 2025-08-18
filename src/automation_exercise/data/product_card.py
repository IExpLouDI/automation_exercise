from dataclasses import dataclass
from typing import Optional


@dataclass
class ProductCard:
    name: str
    category: str
    price: str
    quantity: str
    product_id: Optional[str] = None

    @property
    def total_price(self):
        currency = ''.join(el for el in self.price.replace(' ', '') if not el.isdigit())
        price = int(''.join(el for el in self.price.replace(' ', '') if el.isdigit()))
        quantity = int(self.quantity)
        return f'{currency} {price * quantity}'
