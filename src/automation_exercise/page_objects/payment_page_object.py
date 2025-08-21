from selene import browser, be, have
from allure import step

from src.automation_exercise.data.user import UserCard


class PaymentPage:
    def __init__(self):
        self.page_name = browser.element('div .heading')
        self.input_name_on_card = browser.element("[data-qa='name-on-card']")
        self.input_card_number = browser.element("[data-qa='card_number']")
        self.input_cvc_code = browser.element("[data-qa='cvc']")
        self.input_expiry_month = browser.element("[data-qa='expiry-month']")
        self.input_expiry_year = browser.element("[data-qa='expiry-year']")
        self.button_pay = browser.element("[data-qa='pay-button']")
        self.button_download_invoice = browser.element('a.check_out')
        self.button_continue = browser.element('a.btn-primary')

    def fill_name_on_card(self, name: str):
        with step(f'Заполнение имени на карте: "{name}"'):
            self.input_name_on_card.type(name)

    def fill_card_number(self, card_number: str):
        with step(f'Заполнение номера карты: "{card_number}"'):
            self.input_card_number.type(card_number)

    def fill_cvc_code(self, cvc: str):
        with step(f'Заполнение CVC кода: "{cvc}"'):
            self.input_cvc_code.type(cvc)

    def fill_expiry_month(self, month: str):
        with step(f'Заполнение месяца expiration: "{month}"'):
            self.input_expiry_month.type(month)

    def fill_expiry_year(self, year: str):
        with step(f'Заполнение года expiration: "{year}"'):
            self.input_expiry_year.type(year)

    def click_pay_button(self):
        with step('Нажатие кнопки "Pay and Confirm Order"'):
            self.button_pay.click()

    def fill_card_details_from_object(self, card:UserCard):
        with step(f'Заполнение данных карты: {card}'):
            self.fill_name_on_card(card.name)
            self.fill_card_number(card.number)
            self.fill_cvc_code(card.cvc)
            self.fill_expiry_month(str(card.expiration_month))
            self.fill_expiry_year(str(card.expiration_year))

    def verify_page_opened(self):
        with step('Проверка открытия страницы формирования заказа'):
            self.page_name.should(be.visible)

    def verify_order_is_placed(self):
        with step('Проверка успешного формирования заказа'):
            browser.element("[data-qa='order-placed']").should(be.present)
            browser.element('.message').should(have.exact_text('Your order has been placed successfully!'))
            browser.element("[data-qa='continue-button']").click()

    def press_download_invoice(self):
        with step('Нажимаем кнопку Download Invoice'):
            self.button_download_invoice.click()

    def press_continue(self):
        with step('Нажимаем кнопку Continue'):
            self.button_continue.click()
