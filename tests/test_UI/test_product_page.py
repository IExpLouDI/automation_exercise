import allure
import pytest
from allure_commons.types import Severity


@allure.id('01_PRODUCT_PAGE')
@allure.tag('UI', 'PRODUCT_PAGE')
@allure.severity(Severity.CRITICAL)
@allure.parent_suite('UI')
@allure.suite('PRODUCT_PAGE')
@allure.label('owner', 'vssuchkov')
@allure.link('https://www.automationexercise.com', name='Testing UI')
@pytest.mark.skip(reason='Тест в разработке')
def test_verify_product_page_and_product_detail_page(setup_remote_browser, application):
	application.navigation_bar.open_products_page()
	application.products.verify_open_products_page()
	application.products.scroll_page(100)
	application.products.open_product_deatail()
	application.products.verify_product_detail_is_open()
	application.products.check_product_detail_is_visible()


@allure.id('02_PRODUCT_PAGE')
@allure.tag('UI', 'PRODUCT_PAGE')
@allure.severity(Severity.CRITICAL)
@allure.parent_suite('UI')
@allure.suite('PRODUCT_PAGE')
@allure.label('owner', 'vssuchkov')
@allure.link('https://www.automationexercise.com', name='Testing UI')
@pytest.mark.skip(reason='Тест в разработке')
def test_search_product(setup_remote_browser, application):
	application.navigation_bar.open_products_page()
	application.products.search_product('Tshirt')
	application.products.verify_searched_products_is_visible()
	application.products.verify_all_products_are_visible()
