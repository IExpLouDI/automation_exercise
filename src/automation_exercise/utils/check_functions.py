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


@step(f'Проверяем соответствие схеме {{schema_path}}')
def validate_response_schema(schema_path, response:dict) -> None:
    with open(schema_path, 'r', encoding='utf-8') as file:
        schema = json.loads(file.read())

    validate(instance=response, schema=schema)


def check_response_content(response:dict, valid_content:dict) -> None:
    for key in valid_content.keys():
        with step(f'Проверяем, что {key} = {valid_content.get(key)}'):
            assert response.get('user').get(key) == valid_content.get(key)


def check_response_status_and_message_business_code(response: dict,
                                                    wait_status_code:int,
                                                    wait_business_code:int = None) -> None:
    with step(f'Проверка статуса ответа = {wait_status_code}'):
        assert response.get('status_code') == wait_status_code

    if wait_business_code is not None:
        with step(f'Проверка бизнес кода ответа = {wait_business_code}'):
            assert response.get('response').get('responseCode') == wait_business_code
