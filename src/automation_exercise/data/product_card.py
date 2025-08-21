from dataclasses import dataclass


@dataclass
class ProductCard:
    name: str
    category: str
    price: str
    quantity: str
    product_id: str

    @property
    def total_price(self):
        currency = ''.join(el for el in self.price.replace(' ', '') if not el.isdigit())
        price = int(''.join(el for el in self.price.replace(' ', '') if el.isdigit()))
        quantity = int(self.quantity)
        return f'{currency} {price * quantity}'

    def set_quantity(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Quantity must be positive")
        self.quantity = str(value)

    def __repr__(self):
        return f'Product - {self.name}, quantity - {self.quantity}, price - {self.price}'
