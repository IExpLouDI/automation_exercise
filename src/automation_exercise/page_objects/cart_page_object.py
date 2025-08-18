from allure import step
from selene import browser, have, be

from src.automation_exercise.page_objects.stable_pages_object import StableObject


class CartPage(StableObject):
	def __init__(self):
		super().__init__()

	def check_product_in_cart(self, products:list):
		products_table = browser.element('#cart_info_table tbody')

		with step(f'Проверяем, что количество товаров в корзине - {len(products)}'):
			products_table.all('tbody tr[id^="product-"]').should(have.size(len(products)))

		for expected_product in products:
			with step(f'Проверяем товар {expected_product.name} (ID: {expected_product.product_id})'):

				product_row = browser.element(f'tr[id="product-{expected_product.product_id}"]')

				checks = [
					('.cart_description h4 a', 'название', expected_product.name),
					('.cart_description p', 'категория', expected_product.category),
					('.cart_price p', 'цена', expected_product.price),
					('.cart_quantity button', 'количество', expected_product.quantity),
					('.cart_total_price', 'общая стоимость', expected_product.total_price)
				]

				for selector, attr_name, expected_value in checks:
					with step(f'Параметр "{attr_name}" совпадает с {expected_value}'):
						product_row.element(selector).should(
							have.exact_text(expected_value)
						)
