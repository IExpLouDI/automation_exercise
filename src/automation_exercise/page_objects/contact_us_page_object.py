import os.path

from selene import browser, be, have
from allure import step


class ContactUsPage:
    def __init__(self):
        self.page_name = browser.element("//h2[contains(text(), 'Contact ')]")
        self.input_name = browser.element("[data-qa='name']")
        self.input_email = browser.element("[data-qa='email']")
        self.input_subject = browser.element("[data-qa='subject']")
        self.textarea_message = browser.element("[data-qa='message']")
        self.input_file = browser.element("[name='upload_file']")
        self.button_submit = browser.element("[data-qa='submit-button']")


    def type_user_name(self, value):
        with step(f'Вводим имя пользователя - {value}'):
            self.input_name.type(value)

        return self

    def type_user_email(self, value):
        with step(f'Вводим email пользователя - {value}'):
            self.input_email.type(value)

        return self

    def type_mail_subject(self, value):
        with step(f'Вводим тему письма - {value}'):
            self.input_subject.type(value)

        return self

    def type_message(self, value):
        with step(f'Вводим текст сообщения длинною {len(value)} - содержанием {value[:10]}'):
            self.textarea_message.type(value)

        return self

    def upload_user_file(self, file_path):
        with step(f'Загружаем файл - {os.path.basename(file_path)}'):
            self.input_file.send_keys(file_path)

        return self

    def press_submit_button(self):
        with step('Нажимаем кнопку submit'):
            self.button_submit.click()

    def verify_page_is_open(self):
        self.page_name.should(be.present)

    def confirm_alert(self):
        with step('Выполняем подтверждение в всплывающем окне'):
            browser.switch_to.alert.accept()

        return self

    def verify_successful_submited(self):
        with step('Проверяем, что появилось сообщения успешной отправки'):
            browser.element('.status').should(be.present)
        with step('Проверяем, что текст сообщения - Success! Your details have been submitted successfully'):
            browser.element('.status').should(have.exact_text('Success! Your details have been submitted successfully.'))
        with step('Возвращаемся на домашнюю страницу'):
            browser.element('.btn-success').click()
