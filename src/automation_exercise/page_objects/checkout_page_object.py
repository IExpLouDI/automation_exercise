from typing import List

from selene import browser, be, have
from allure import step

from src.automation_exercise.data.product_card import ProductCard
from src.automation_exercise.data.user import User


class CheckoutPage:
    def __init__(self):
        self.page_verify_attribute = browser.element("//h2[contains(text(), 'Address')]")
        self.delivery_address_params = browser.element('#address_delivery li ~ li')
        self.billing_address_params = browser.element('#address_invoice li ~ li')
        self.description_product_name = browser.element('.cart_description a')
        self.description_product_category = browser.element('.cart_description p')
        self.product_price = browser.element('.cart_price p')
        self.product_quantity = browser.element('.cart_quantity button')
        self.product_total_price = browser.element('.cart_total p')
        self.order_message = browser.element('#ordermsg textarea')
        self.button_check_out = browser.element('div .check_out')

    def verify_checkout_page_open(self):
        self.page_verify_attribute.should(be.present)

    def check_delivery_address_params(self, user_params: User):
        with step(f'Параметры доставки совпадают с {user_params.get_user_param}'):
            self.delivery_address_params.should(have.exact_texts(user_params.get_user_param))


    def check_billing_address_params(self, user_params: User):
        with step(f'Платежные параметры совпадают с {user_params.get_user_param}'):
            self.billing_address_params.should(have.exact_texts(user_params.get_user_param))

    def verify_order_list(self, products:List[ProductCard]):

        for product in products:
            product_row = browser.element(f'#product-{product.product_id}')
            checks = [
                (self.description_product_name, 'название', product.name),
                (self.description_product_category, 'категория', product.category),
                (self.product_price, 'цена', product.price),
                (self.product_quantity, 'количество', product.quantity),
                (self.product_total_price, 'общая стоимость', product.total_price)
            ]

            for selector, attr_name, expected_value in checks:
                with step(f'Параметр "{attr_name}" совпадает с {expected_value}'):
                    product_row.element(selector).should(
                        have.exact_text(expected_value)
                    )

    def enter_order_message(self, message:str):
        self.order_message.type(message)

    def press_button_place_order(self):
        self.button_check_out.click()
