import allure
from selene import browser


class MainHeaderPage:
    def __init__(self):
        self.search_bar = browser.element("[action='/search'] input")

    def search_position(self, value):
        with allure.step(f'Find {value}'):
            self.search_bar.type(value).press_enter()