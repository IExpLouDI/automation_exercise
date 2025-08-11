from src.automation_exercise.app import Application
from src.automation_exercise.utils.check_functions import check_website_is_open, check_account_is_deleted
from allure import step


def test_user_login(setup_browser, create_account):
    app = Application()

    with step('Проверяем что открыта домашняя страница'):
        check_website_is_open()

    with step('Переходим в окно авторизации'):
        app.navigation_bar.open_login_page()

    with step('Проверяем что открыто окно авторизации'):
        app.signup_login_page.check_signup_and_login_page_is_open()

    with step('Вводим данные пользователя в форму авторизации'):
        app.signup_login_page.type_email(create_account['email'], is_login=True)
        app.signup_login_page.type_password(create_account['password'])
        app.signup_login_page.pres_button_login()

    with step('Проверяем, что выполнен вход в аккаунт пользователем'):
        app.navigation_bar.check_user_is_login(create_account["nick_name"])

    with step('Удаление пользователя'):
        app.navigation_bar.click_delete_user()
        check_account_is_deleted()
