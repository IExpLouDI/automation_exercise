from selene import browser, be, have
from selene.core.condition import Condition
from allure import step

from src.automation_exercise.page_objects.stable_pages_object import StableObject


class ProductsPage(StableObject):
	def __init__(self):
		super().__init__()
		self.page_name = browser.element('h2.title')
		self.input_search_product = browser.element('#search_product')
		self.button_search_product = browser.element('div #submit_search')
		self.searched_products_title = browser.element("//h2[contains(text(), 'Searched')]")

	def verify_open_products_page(self):
		with step('Проверяем, что открылась вкладка с товарами'):
			self.page_name.should(be.present)
		with step('Проверяем, что текст - ALL PRODUCTS'):
			self.page_name.should(have.exact_text('ALL PRODUCTS'))

	def add_wanted_product_in_cart(self, product_id:str):
		with step(f'Добавляем товар в корзину с идентификатором - {product_id}'):
			browser.element(f"[data-product-id='{product_id}']").hover()
			browser.element(f".overlay-content [data-product-id='{product_id}']").with_(timeout=2).click()

		return self

	def search_product(self, value:str):
		with step(f'Вводим {value[:10]} в строку поиска'):
			self.input_search_product.type(value)
		with step('Наимаем кнопку "Поиск"'):
			self.button_search_product.click()

	def verify_searched_products_is_visible(self):
		with step('Проверяем, что представлена форма с результатами поиска'):
			self.searched_products_title.should(be.present)

	def verify_all_products_are_visible(self):
		with step('Проверяем, что товары представлены на странице'):
			products = browser.all('.productinfo').should(be.visible.each)

			for product in products:
				product.should(be.visible)

	def press_button_continue_shopping(self):
		with step('Нажимаем, кнопку "Continue Shopping"'):
			browser.element('button.close-modal').click()

		return self

	def click_view_cart_page(self):
		with step('Кликаем по ссылке "View Cart"'):
			browser.element('.modal-confirm a').click()

		return self
