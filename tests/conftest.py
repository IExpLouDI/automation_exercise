import pytest
from selene import browser, be
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.client_config import ClientConfig
from dotenv import load_dotenv
import os

from selenium.webdriver.remote.remote_connection import RemoteConnection

from src.automation_exercise.API.delete_request import delete_account
from src.automation_exercise.app import Application
from src.automation_exercise.data.products import product_men_tshirt, product_women_blue_top
from src.automation_exercise.utils.attachments import add_video
from src.automation_exercise.utils.static_values import Country, Months
from src.automation_exercise.data.user import User, UserCard

from src.automation_exercise.API.post_request import post_create_account


@pytest.fixture(autouse=False, scope='function')
def setup_remote_browser():
	load_dotenv()
	SELENOID_LOGIN = os.getenv('SELENOID_LOGIN')

	SELENOID_PASSWORD = os.getenv('SELENOID_PASSWORD')
	SELENOID_HOST = os.getenv('SELENOID_HOST')

	options = Options()
	selenoid_capabilities = {
		"browserName": "chrome",
		"browserVersion": "127.0",
		"selenoid:options": {"enableVNC": True, "enableVideo": True, "enableLog": True},
		"goog:loggingPrefs": {'browser': 'ALL'},
	}
	options.add_argument("--start-maximized")
	options.add_argument("--disable-blink-features=AutomationControlled")

	options.capabilities.update(selenoid_capabilities)

	client_config = ClientConfig(
		remote_server_addr=f'https://{SELENOID_HOST}/wd/hub',
		keep_alive=True
	)
	client_config.username = SELENOID_LOGIN
	client_config.password = SELENOID_PASSWORD

	connection = RemoteConnection(client_config=client_config)

	driver = webdriver.Remote(
		command_executor=connection,
		options=options
	)

	browser.config.driver = driver

	browser.config.base_url = 'https://www.automationexercise.com'
	browser.open('/')
	browser.driver.execute_script("$('#fixedban').remove()")
	# browser.driver.execute_script("$('footer').remove()")

	if browser.element("[aria-label='Consent']").with_().matching(be.present):
		browser.element("[aria-label='Consent']").click()

	yield browser

	add_video(browser)

	browser.quit()


@pytest.fixture()
def application():
	app = Application()
	return app


@pytest.fixture()
def setup_browser():
	browser.config.driver_name = 'firefox'
	# browser.config.base_url = 'https://www.automationexercise.com'
	# opt = options.page_load_strategy = "eager"
	# browser.config.driver_options = opt
	browser.open('https://www.automationexercise.com')

	yield browser

	browser.quit()


@pytest.fixture(scope='function')
def create_user():
	"""Создание пользователя для регистрации"""
	user = User(
		nick_name='Testovich',
		email='T2@test.com',
		password='Qwe123',
		company_name='Trevor Corporation',
		country=Country.india.value,
		first_name='Trevor',
		last_name='Laxtin',
		gender='male',
		day='10',
		month=Months.may.value[0],
		year='2000',
		city='Bangladesh',
		state='Salavalas',
		first_address='Shampte 32 str., appartment 33',
		second_address='Helentors 5 str., apartment 44',
		zipcode='2331144',
		mobile_number='34534222323'
	)
	user_card = UserCard(
		name=f'{user.first_name.upper()} {user.last_name}',
		number='5677654433225566',
		cvc='111',
		expiration_month='02',
		expiration_year='2030'
	)

	user.add_card(user_card)

	return user


@pytest.fixture(scope='function')
def create_account(create_user):
	"""Создаёт пользователя и по окончанию теста - удаляет"""
	yield post_create_account(create_user)
	delete_account(create_user.email, create_user.password)


@pytest.fixture(scope='function')
def products_list():
	products = [product_men_tshirt, product_women_blue_top]
	yield products

	for product in products:
		product.reset_quantity()
