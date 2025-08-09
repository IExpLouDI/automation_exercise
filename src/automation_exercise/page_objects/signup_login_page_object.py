import allure
from selene import browser


class SignUpLoginPage:
    def __init__(self):
        self.sign_name = browser.element("[data-qa='signup-name']")
        self.sign_email = browser.element("[data-qa='signup-email']")
        self.login_email = browser.element("[data-qa='login-email']")
        self.login_password = browser.element("[data-qa='login-password']")
        self.button_signup = browser.element("[data-qa='signup-button']")
        self.button_login = browser.element("[data-qa='login-button']")

    def type_sign_up_name(self, value):
        with allure.step(f'Вводим имя пользователя {value}'):
            self.sign_name.type(value)

        return self

    def type_login(self, value):
        with allure.step(f'Вводим пароль - {value}'):
            self.sign_name.type(value)

        return self

    def type_email(self, value, is_login=False):
        with allure.step(f'Вводим email пользователя {value}'):
            if is_login:
                self.login_email.type(value)
            else:
                self.sign_email.type(value)

        return self

    def pres_button_signup(self):
        with allure.step(f'Нажимаем кнопку Signup'):
            self.button_signup.click()

    def pres_button_login(self, value, is_login=False):
        with allure.step(f'Нажимаем кнопку Login'):
            self.button_login.click()
