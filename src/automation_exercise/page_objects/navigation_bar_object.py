import allure
from selene import browser, have


class NavigationBar:
    def __init__(self):
        self.search_bar = browser.element("[action='/search'] input")
        self.home = browser.element("//a[contains(text(), 'Home')]")
        self.products = browser.element("//a[contains(text(), 'Products')]")
        self.cart = browser.element("//a[contains(text(), 'Cart')]")
        self.login = browser.element("//a[contains(text(), 'Login')]")
        self.logout = browser.element("//a[contains(text(), 'Logout')]")
        self.delete = browser.element("//a[contains(text(), 'Delete')]")
        self.contact_us = browser.element("//a[contains(text(), 'Contact us')]")

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

    def open_contact_us_page(self):
        with allure.step('Открываем окно обратной связи'):
            self.contact_us.click()

    def click_delete_user(self):
        with allure.step('Удаляем пользователя'):
            self.delete.click()

    def click_logout(self):
        with allure.step('Нажимаем Logout'):
            self.logout.click()

    @staticmethod
    def check_user_is_login(nickname):
        browser.element("//a[contains(text(), 'Logged')]").should(have.text(f'Logged in as {nickname}'))
