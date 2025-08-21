import allure
from selene import browser, be


@allure.step('Проверяем, что открыт сайт https://www.automationexercise.com')
def check_website_is_open():
    browser.element("[alt='Website for automation practice']").should(be.visible)

def check_account_is_create():
    browser.element("[data-qa='account-created']").should(be.visible)
    browser.element("[data-qa='continue-button']").click()

@allure.step('Аккаунт успешно удалён')
def check_account_is_deleted():
    browser.element("[data-qa='account-deleted']").should(be.visible)
    browser.element("[data-qa='continue-button']").click()
