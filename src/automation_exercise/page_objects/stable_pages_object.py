from allure import step
from selene import browser


class StableObject:
	def __init__(self):
		self.scroll_up = browser.element('#scrollUp')

	def click_scroll_up_button(self):
		with step('Нажимаем кнопку scroll_up'):
			self.scroll_up.click()

	def scroll_page(self, scroll_step: int):
		browser.execute_script(f"window.scrollBy(0, {scroll_step});")

		return self
