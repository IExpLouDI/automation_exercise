from selene import browser, be
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dotenv import load_dotenv
import os


def test_available():
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
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f'https://{SELENOID_LOGIN}:{SELENOID_PASSWORD}@{SELENOID_HOST}',
        options=options,
    )
    browser.config.driver = driver

    browser.open('https://www.automationexercise.com/test_cases')
    browser.element("h2.title").should(be.present)
