import pytest
from selene import browser, be
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dotenv import load_dotenv
import os

from src.automation_exercise.API.delete_request import delete_account
from src.automation_exercise.app import Application
from src.automation_exercise.data.products import product_men_tshirt, product_women_blue_top
from src.automation_exercise.utils.static_values import Country, Months
from src.automation_exercise.data.user import User

from src.automation_exercise.API.post_request import post_create_account


@pytest.fixture(autouse=False, scope='session')
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
	# options.page_load_strategy = "eager"
	# options.add_experimental_option("excludeSwitches", ["enable-automation"])
	# options.add_experimental_option("useAutomationExtension", False)

	options.capabilities.update(selenoid_capabilities)

	driver = webdriver.Remote(
		command_executor=f'https://{SELENOID_LOGIN}:{SELENOID_PASSWORD}@{SELENOID_HOST}/wd/hub',
		options=options,
	)
	browser.config.driver = driver

	browser.config.base_url = 'https://www.automationexercise.com'
	browser.open('/')
	if browser.element("[aria-label='Consent']").with_().matching(be.present):
		browser.element("[aria-label='Consent']").click()

	yield browser

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


@pytest.fixture()
def create_user():
	user = User(
		nick_name='T1',
		email='T2@test.com',
		password='Qwe123',
		company_name='T2',
		country=Country.india.value,
		first_name='T3',
		last_name='T4',
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

	return user


@pytest.fixture()
def create_account(create_user):
	yield post_create_account(create_user)
	delete_account(create_user.email, create_user.password)


@pytest.fixture()
def products_list():
	return [product_men_tshirt, product_women_blue_top]
