import allure
from selene import browser


class NavigationBar:
    def __init__(self):
        self.search_bar = browser.element("[action='/search'] input")
        self.home = browser.element("//a[contains(text(), 'Home')]")
        self.products = browser.element("//a[contains(text(), 'Products')]")
        self.cart = browser.element("//a[contains(text(), 'Cart')]")
        self.login = browser.element("//a[contains(text(), 'Login')]")
        self.delete = browser.element("//a[contains(text(), 'Delete')]")

    def open_home_page(self):
        with allure.step('Открываем домашнюю страницу'):
            self.home.click()

    def open_products_page(self):
        with allure.step('Открываем каталог продуктов'):
            self.products.click()

    def open_cart_page(self):
        with allure.step('Открываем корзину пользователя'):
            self.cart.click()

    def open_login_page(self):
        with allure.step('Открываем окно входа и регистрации пользователя'):
            self.login.click()

    def click_delete_user(self):
        with allure.step('Удаляем пользователя'):
            self.cart.click()

    def search_position(self, value):
        with allure.step(f'Find {value}'):
            self.search_bar.type(value).press_enter()
