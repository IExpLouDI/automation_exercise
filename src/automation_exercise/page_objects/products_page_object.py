from selene import browser, be, have
from allure import step


class ProductsPage:
    def __init__(self):
        self.page_name = browser.element('h2.title')
        self.scroll_up = browser.element('#scrollUp')

    def verify_open_products_page(self):
        with step('Проверяем, что открылась вкладка с товарами'):
            self.page_name.should(be.present)
        with step('Проверяем, что текст - ALL PRODUCTS'):
            self.page_name.should(have.exact_text('ALL PRODUCTS'))

    def click_scroll_up_button(self):
        with step('Нажимаем кнопку scroll_up'):
            self.scroll_up.click()

    def scroll_products_page(self, scroll_step:int):
        browser.execute_script(f"window.scrollBy(0, {scroll_step});")

        return self

    def find_wanted_product(self, product_id):
        with step(f'Прокручиваем каталог продуктов, пока не будет виден товар - {product_id}'):
            while not browser.element(f"[data-product-id='{product_id}']").matching(be.visible):
                self.scroll_products_page(100)
