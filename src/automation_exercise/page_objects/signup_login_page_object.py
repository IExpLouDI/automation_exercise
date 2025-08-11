import allure
from selene import browser, be, have


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

    def type_password(self, value):
        with allure.step(f'Вводим пароль - {value}'):
            self.login_password.type(value)

        return self

    def type_email(self, value, is_login=False):
        with allure.step(f'Вводим email пользователя {value}'):
            if is_login:
                self.login_email.type(value)
            else:
                self.sign_email.type(value)

        return self

    def pres_button_signup(self):
        with allure.step('Нажимаем кнопку Signup'):
            self.button_signup.click()

    def pres_button_login(self):
        with allure.step('Нажимаем кнопку Login'):
            self.button_login.click()

    @staticmethod
    def verify_incorrect_email_pass():
        with allure.step('Проверяем появление ошибки входа'):
            browser.element("form[action='/login'] p").should(be.visible)
        with allure.step('Проверяем, что текст ошибки - Your email or password is incorrect!'):
            browser.element("form[action='/login'] p").should(have.exact_text('Your email or password is incorrect!'))

    @staticmethod
    def check_signup_and_login_page_is_open(is_login=False) -> None:
        if not is_login:
            browser.element("//h2[text()='New User Signup!']").should(be.visible)
        else:
            browser.element("//h2[text()='Login to your account']").should(be.visible)
