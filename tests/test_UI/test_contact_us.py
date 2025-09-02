import os.path

import allure
from allure_commons.types import Severity

from src.automation_exercise.utils.check_functions import check_website_is_open
from allure import step

from src.automation_exercise.utils.paths import images_dir


@allure.id('01_CONTACT_US')
@allure.tag('UI', 'CONTACT_US')
@allure.severity(Severity.BLOCKER)
@allure.parent_suite('UI')
@allure.suite('CONTACT_US')
@allure.label('owner', 'vssuchkov')
@allure.link('https://www.automationexercise.com', name='Testing UI')
def test_contact_us_form(setup_remote_browser, application, create_user_account):
    with step('Открываем окно обратной связи'):
        application.navigation_bar.open_contact_us_page()

    with step('Проверяем, что форма обратной связи открыта'):
        application.contact_us_page.verify_page_is_open()

    with step('Заполняем форму обратной связи'):
        (application.contact_us_page
         .type_user_name(create_user_account['nick_name'])
         .type_user_email(create_user_account['email'])
         .type_mail_subject('Test')
         .type_message('lorem')
         .upload_user_file(os.path.join(images_dir,'cat.jpeg'))
         .press_submit_button()
         )

    with step('Подтверждаем отправку в всплывающем окне'):
        application.contact_us_page.confirm_alert()

    with step('Проверяем, что сообщение отправлено и возвращаемся на стартовую страницу'):
        application.contact_us_page.verify_successful_submited()

    with step('Проверяем, что открыта стартовая страница'):
        check_website_is_open()
