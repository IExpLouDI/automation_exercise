from src.automation_exercise.app import Application
from src.automation_exercise.utils.check_functions import check_website_is_open, check_account_is_deleted
from allure import step


def test_user_login_with_correct_email_passw(setup_remote_browser, create_account, application):

    with step('Проверяем что открыта домашняя страница'):
        check_website_is_open()

    with step('Переходим в окно авторизации'):
        application.navigation_bar.open_login_page()

    with step('Проверяем что открыто окно авторизации'):
        application.signup_login_page.check_signup_and_login_page_is_open()

    with step('Вводим данные пользователя в форму авторизации'):
        (application.signup_login_page
         .type_email(create_account['email'], is_login=True)
         .type_password(create_account['password'])
         .pres_button_login()
         )

    with step('Проверяем, что выполнен вход в аккаунт пользователем'):
        application.navigation_bar.check_user_is_login(create_account["nick_name"])

    with step('Удаление пользователя'):
        application.navigation_bar.click_delete_user()
        check_account_is_deleted()

def test_user_login_with_no_correct_email_passw(setup_remote_browser, application):

    with step('Проверяем что открыта домашняя страница'):
        check_website_is_open()

    with step('Переходим в окно авторизации'):
        application.navigation_bar.open_login_page()

    with step('Проверяем что открыто окно авторизации'):
        application.signup_login_page.check_signup_and_login_page_is_open()

    with step('Вводим несуществующие данные пользователя в форму авторизации'):
        (application.signup_login_page
         .type_email('z211@login.page', is_login=True)
         .type_password('z211')
         .pres_button_login()
         )

    with step('Проверяем появление предупреждения об ошибке'):
        application.signup_login_page.verify_incorrect_email_pass()


def test_user_logout(setup_remote_browser, create_account, application):

    with step('Переходим в окно авторизации'):
        application.navigation_bar.open_login_page()

    with step('Выполняем вход в аккаунт'):
        (application.signup_login_page
         .type_email(create_account['email'], is_login=True)
         .type_password(create_account['password'])
         .pres_button_login()
         )

    with step('Проверяем, что выполнен вход в аккаунт пользователем'):
        application.navigation_bar.check_user_is_login(create_account['nick_name'])

    with step('Проверяем, что выполнен вход в аккаунт пользователем'):
        application.navigation_bar.click_logout()

    with step('Проверяем, что открылось окно авторизации/регистрации пользователя'):
        application.signup_login_page.check_signup_and_login_page_is_open(is_login=True)
