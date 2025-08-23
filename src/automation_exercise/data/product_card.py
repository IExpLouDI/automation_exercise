from dataclasses import dataclass, field
from typing import List


@dataclass
class ProductCard:
    name: str
    category: str
    price: str
    quantity: str
    product_id: str
    change_quantity_history: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.change_quantity_history:
            self.change_quantity_history.append(self.quantity)

    @property
    def total_price(self):
        currency = ''.join(el for el in self.price.replace(' ', '') if not el.isdigit())
        price = int(''.join(el for el in self.price.replace(' ', '') if el.isdigit()))
        quantity = int(self.quantity)
        return f'{currency} {price * quantity}'

    def set_quantity(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Quantity must be positive")
        self.change_quantity_history.append(str(value))
        self.quantity = str(value)


    def reset_quantity(self):
        self.quantity = self.change_quantity_history[0]


    def __repr__(self):
        return f'Product - {self.name}, quantity - {self.quantity}, price - {self.price}'
