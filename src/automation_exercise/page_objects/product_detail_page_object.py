from allure import step
from selene import browser, have, query

from src.automation_exercise.data.product_card import ProductCard


class ProductDetailPage:
    def __init__(self):
        self.product_name = browser.element('.product-information h2')
        self.product_category = browser.element('//div[@class="product-information"]/p[1]')
        self.product_price = browser.element('.product-information span span')
        self.product_quantity = browser.element('#quantity ')
        self.button_add_to_cart = browser.element('.product-information .btn')

    def press_button_add_to_cart(self):
        with step('Нажимаем кнопку - Add to cart'):
            self.button_add_to_cart.click()

    def set_product_quantity(self, value):
        with step(f'Устанавливаем количество продукта - {value}'):
            self.product_quantity.clear().type(value)

    def check_product_detail(self, product:ProductCard):
        checks = [
            (self.product_name, 'название', product.name),
            # (self.product_category, 'категория', 'Category: ' + product.category),
            (self.product_price, 'цена', product.price)
        ]

        for element, param, value in checks:
            with step(f'Проверяем, {param} = {value}'):
                actual_text = element.get(query.text)
                normalized_actual = ' '.join(actual_text.split())
                normalized_expected = ' '.join(value.split())

                assert normalized_actual == normalized_expected, \
                    f'Expected: "{normalized_expected}", but got: "{normalized_actual}"'
