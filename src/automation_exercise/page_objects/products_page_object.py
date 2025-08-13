from selene import browser, be, have
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

	def find_wanted_product(self, product_id):
		with step(f'Прокручиваем каталог продуктов, пока не будет виден товар - {product_id}'):
			while not browser.element(f"[data-product-id='{product_id}']").matching(be.visible):
				self.scroll_page(100)

	def search_product(self, value:str):
		with step(f'Вводим {value[:10]} в строку поиска'):
			self.input_search_product.type(value)
		with step('Наимаем кнопку "Поиск"'):
			self.button_search_product.click()

	def verify_searched_products_is_visible(self):
		with step('Проверяем, что представлено форма с результатами поиска'):
			self.searched_products_title.should(be.present)
