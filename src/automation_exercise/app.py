from src.automation_exercise.page_objects.contact_us_page_object import ContactUsPage
from src.automation_exercise.page_objects.footer_page_object import Footer
from src.automation_exercise.page_objects.home_page_object import HomePage
from src.automation_exercise.page_objects.navigation_bar_object import NavigationBar
from src.automation_exercise.page_objects.products_page_object import ProductsPage
from src.automation_exercise.page_objects.signup_login_page_object import SignUpLoginPage
from src.automation_exercise.page_objects.user_account_page import UserAccountPage


class Application:
	def __init__(self):
		self.navigation_bar = NavigationBar()
		self.signup_login_page = SignUpLoginPage()
		self.user_account_page = UserAccountPage()
		self.contact_us_page = ContactUsPage()
		self.products = ProductsPage()
		self.home_page = HomePage()
		self.footer = Footer()
