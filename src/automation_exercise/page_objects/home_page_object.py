from allure import step
from selene import browser

from src.automation_exercise.page_objects.stable_pages_object import StableObject


class HomePage(StableObject):
    def __init__(self):
        super().__init__()


    def click_view_product(self, product_id):
        with step(f'Открывает страницу продукта - {product_id}'):
            browser.element(f"[href='/product_details/{product_id}']").click()

