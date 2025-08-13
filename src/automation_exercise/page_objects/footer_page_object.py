from allure import step
from selene import browser, be, have


class Footer:
    def __init__(self):
        self.input_email = browser.element('#susbscribe_email')
        self.button_subscribe = browser.element('#subscribe')
        self.success_subscribe = browser.element('#success-subscribe')

    def enter_email(self, value):
        with step(f'Вводим email - {value}'):
            self.input_email.type(value)

        return self

    def press_button(self):
        self.button_subscribe.click()

    def verify_success_subscribe(self):
        with step('Проверяем, что появилось сообщение об успешной подписке'):
            self.success_subscribe.should(be.visible)
        with step('Проверяем что текст сообщения - You have been successfully subscribed!'):
            self.success_subscribe.should(have.exact_text('You have been successfully subscribed!'))