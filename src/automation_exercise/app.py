from src.automation_exercise.page_objects.cart_page_object import CartPage
from src.automation_exercise.page_objects.checkout_page_object import CheckoutPage
from src.automation_exercise.page_objects.contact_us_page_object import ContactUsPage
from src.automation_exercise.page_objects.footer_page_object import Footer
from src.automation_exercise.page_objects.home_page_object import HomePage
from src.automation_exercise.page_objects.navigation_bar_object import NavigationBar
from src.automation_exercise.page_objects.payment_page_object import PaymentPage
from src.automation_exercise.page_objects.product_detail_page_object import ProductDetailPage
from src.automation_exercise.page_objects.products_page_object import ProductsPage
from src.automation_exercise.page_objects.signup_login_page_object import SignUpLoginPage
from src.automation_exercise.page_objects.stable_pages_object import StableObject
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
		self.cart_page = CartPage()
		self.product_detail_page = ProductDetailPage()
		self.check_out_page = CheckoutPage()
		self.stable_elements = StableObject()
		self.payment_page = PaymentPage()
