from src.automation_exercise.page_objects.contact_us_page_object import ContactUsPage
from src.automation_exercise.page_objects.navigation_bar_object import NavigationBar
from src.automation_exercise.page_objects.signup_login_page_object import SignUpLoginPage
from src.automation_exercise.page_objects.user_account_page import UserAccountPage


class Application:
    def __init__(self):
        self.navigation_bar = NavigationBar()
        self.signup_login_page = SignUpLoginPage()
        self.user_account_page = UserAccountPage()
        self.contact_us_page = ContactUsPage()
