from src.automation_exercise.app import Application
from src.automation_exercise.utils.check_functions import check_website_is_open


def test_user_login(setup_browser, create_account):
    app = Application()

    check_website_is_open()

    app.navigation_bar.open_login_page()
    app.signup_login_page.check_signup_and_login_page_is_open()

    app.signup_login_page.login_email()
