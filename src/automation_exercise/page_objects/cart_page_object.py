from allure import step
from selene import browser, have, be

from src.automation_exercise.page_objects.stable_pages_object import StableObject


class CartPage(StableObject):
	def __init__(self):
		super().__init__()

	def check_product_count_in_cart(self, products:list):
		product_rows = browser.all('tbody tr[id^="product-"]')

		with step(f'Проверяем, что количество товаров в корзине - {len(products)}'):
			product_rows.should(have.size(len(products)))

		with step(f'Проверяем товары в корзине'):
			for i, expected_product in enumerate(products):
				# Проверка названия продукта
				with step(f'Название товара совпадает с {expected_product.name}'):
					product_rows[i].element('.cart_description h4 a').should(have.exact_text(expected_product.name))

				with step(f'Категория товара совпадает с {expected_product.category}'):
					product_rows[i].element('.cart_description p').should(have.exact_text(expected_product.category))

				with step(f'Цена товара совпадает с {expected_product.price}'):
					product_rows[i].element('.cart_price p'
											).should(be.present, have.exact_text(expected_product.price))

				with step(f'Количество товара совпадает с {expected_product.quantity}'):
					product_rows[i].element('.cart_quantity button'
											).should(be.present, have.exact_text(expected_product.quantity))

				with step(f'Название товара совпадает с {expected_product.total_price}'):
					product_rows[i].element('.cart_total_price'
											).should(be.present, have.exact_text(expected_product.total_price))
