import json

import pytest
from allure import step
from selene import browser, be
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.client_config import ClientConfig
from dotenv import load_dotenv
import os

from selenium.webdriver.remote.remote_connection import RemoteConnection

from src.automation_exercise.API.delete_request import delete_account
from src.automation_exercise.app import UIManager, APIManager
from src.automation_exercise.data.products import product_men_tshirt, product_women_blue_top
from src.automation_exercise.utils.attachments import add_video, add_logs
from src.automation_exercise.utils.paths import schemas_dir
from src.automation_exercise.utils.static_values import Country, Months
from src.automation_exercise.data.user import User, UserCard
from src.automation_exercise.API.post_request import post_create_account


# @pytest.fixture(scope="session", autouse=True)
# def generate_message():
#     yield
#     telebot_send_message()


@pytest.fixture(autouse=False, scope='function')
def setup_remote_browser():
    """Настройка и создание браузера"""
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

    if browser.element("[aria-label='Consent']").with_().matching(be.present):
        browser.element("[aria-label='Consent']").click()

    yield browser

    add_video(browser)
    add_logs(browser)

    browser.quit()


@pytest.fixture()
def application():
    """Доступ к page objects"""
    app = UIManager()
    return app


@pytest.fixture(scope='function')
def create_user():
    """Создание пользователя для регистрации"""
    user = User(
        nick_name='Testovich',
        email='testov2_qaguru@test.com',
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

    with step(f'Подготовлена запись класса user - {user}.\n С картой {user.card}'):
        return user


@pytest.fixture(scope='function')
def create_user_account(create_user):
    """Создаёт пользователя и по окончанию теста - удаляет"""

    """
	Предварительная попытка удаления пользователя,
	на случай падения теста с регистрацией
	"""
    delete_account(create_user.email, create_user.password)

    yield post_create_account(create_user)

    """Удаляем после теста"""
    delete_account(create_user.email, create_user.password)


@pytest.fixture(scope='function')
def products_list():
    products = [product_men_tshirt, product_women_blue_top]
    yield products

    for product in products:
        product.reset_quantity()


@pytest.fixture(scope='function')
def api_application():
    return APIManager()


@pytest.fixture(scope='function')
def load_schema():
    schemas_paths_dict = {
        'get_all_product_list': os.path.join(schemas_dir, 'schemas_get_all_products_list.json'),
        'post_search_product': os.path.join(schemas_dir, 'schema_post_search_product.json'),
        'get_user_account_detail': os.path.join(schemas_dir, 'schema_get_user_account_detail.json'),
        'get_brands_list': os.path.join(schemas_dir, 'schema_get_brands_list.json')
    }

    return schemas_paths_dict


@pytest.fixture(scope='function')
def update_user_params(create_user):
    new_name = 'Test'
    new_last_name = 'Test2'
    param_dict = {
        'firstname': new_name,
        'lastname': new_last_name,
        'email': create_user.email,
        'password': create_user.password
    }
    return param_dict


@pytest.fixture(scope='function')
def search_param():
    return {'search_product': 'blue top'}


@pytest.fixture(scope='function')
def no_valid_search_param():
    return {'bad_param': None}


@pytest.fixture(scope='function')
def not_found_user(create_user):
    return {'email': create_user.email, 'password': create_user.password}


@pytest.fixture(scope='function')
def product_content():
    return {
        "id": 1,
        "name": "Blue Top",
        "price": "Rs. 500",
        "brand": "Polo",
        "category": {
            "usertype": {
                "usertype": "Women"
            },
            "category": "Tops"
        }
    }


# def telebot_send_message():
#     os.system("allure generate allure-results --clean")
#     bot_token = os.getenv("BOT_TOKEN")
#     group_id = os.getenv("TELEGRAM_GROUP_ID")
#     user = os.getenv("USER_NAME")
#     notifications_path = os.path.dirname(os.path.dirname(__file__))
#     telegram_dict = {
#         "base": {
#             "project": "automation_exercise",
#             "environment": "grade project",
#             "comment": user,
#             "reportLink": "",
#             "language": "ru",
#             "allureFolder": "allure-report",
#             "enableChart": True,
#         },
#         "telegram": {"token": bot_token,
# 					 "chat": group_id,
# 					 "replyTo": ""},
#     }
#
#     with open(
#             os.path.join(notifications_path, "notifications", "telegram.json"),
#             "w",
#             encoding="utf-8",
#     ) as file:
#         file.write(json.dumps(telegram_dict))
#
#     os.system(
#         'java "-DconfigFile=./notifications/telegram.json" -jar ./notifications/allure-notifications-4.11.0.jar'
#     )
#     with open(
#             os.path.join(notifications_path, "notifications", "telegram.json"),
#             "w",
#             encoding="utf-8",
#     ) as file:
#         print(f"{file} - file clear")
