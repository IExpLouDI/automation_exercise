import json
from allure import step
from jsonschema import validate
from selene import browser, be


@step('Проверяем, что открыт сайт https://www.automationexercise.com')
def check_website_is_open():
    browser.element("[alt='Website for automation practice']").should(be.visible)


def check_account_is_create():
    browser.element("[data-qa='account-created']").should(be.visible)
    browser.element("[data-qa='continue-button']").click()


@step('Аккаунт успешно удалён')
def check_account_is_deleted():
    browser.element("[data-qa='account-deleted']").should(be.visible)
    browser.element("[data-qa='continue-button']").click()


def check_response_content(response:dict, valid_content:dict) -> None:
    for key in valid_content.keys():
        with step(f'Проверяем, что {key} = {valid_content.get(key)}'):
            assert response.get('user').get(key) == valid_content.get(key)
