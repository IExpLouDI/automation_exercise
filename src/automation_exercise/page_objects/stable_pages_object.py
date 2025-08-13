from allure import step
from selene import browser, be


class StableObject:
	def __init__(self):
		self.scroll_up = browser.element('#scrollUp')

	def click_scroll_up_button(self):
		with step('Нажимаем кнопку scroll_up'):
			self.scroll_up.click()

	def scroll_page(self, scroll_step: int):
		browser.execute_script(f"window.scrollBy(0, {scroll_step});")

		return self

	def scroll_down_to_footer(self):
		with step('Выполняем прокрутку до появления элемента footer'):
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		return self
