import allure
from allure import step
from allure_commons.types import Severity

from src.automation_exercise.utils.check_functions import check_account_is_create, check_account_is_deleted


@allure.id('01_PLACE_ORDER')
@allure.tag('UI', 'PLACE_ORDER')
@allure.severity(Severity.BLOCKER)
@allure.parent_suite('UI')
@allure.suite('PLACE_ORDER')
@allure.label('owner', 'vssuchkov')
@allure.link('https://www.automationexercise.com', name='Testing UI')
def test_registration_order_while_checkout(setup_remote_browser, application, products_list, create_user):
    with step(f'Открываем страницу товаров и добавляем в корзину {products_list[0]}'):
        application.navigation_bar.open_products_page()
        application.stable_elements.scroll_page(500)
        application.products.add_wanted_product_in_cart(products_list[0].product_id)

    with step(f'Переходим в корзину и далее к оформлению заказа '):
        application.products.click_view_cart_page()
        application.cart_page.press_button_proceed_to_checkout()

    with step(f'Выполняем регистрацию пользователя {create_user}'):
        application.cart_page.click_register_or_login_link()
        application.signup_login_page.type_email(create_user.email)
        application.signup_login_page.type_sign_up_name(create_user.nick_name)
        application.signup_login_page.pres_button_signup()
        application.user_account_page.fill_user_personal_data(create_user)
        application.user_account_page.press_button_create_account()

    with step('Проверяем появление окна успешного создания пользователя'):
        check_account_is_create()

    with step('Проверяем, что пользователь залогинен после создания'):
        application.navigation_bar.check_user_is_login(create_user.nick_name)

    with step('Повторно переходим в корзину и далее к оформлению заказа'):
        application.navigation_bar.open_cart_page()
        application.cart_page.press_button_proceed_to_checkout()

    with step('Проверяем открытие страницы оформления заказа'):
        application.check_out_page.verify_checkout_page_open()
        application.stable_elements.scroll_page(200)

    with step('Проверяем параметры заказа и добавляем сопроводительный комментарий'):
        application.check_out_page.check_delivery_address_params(create_user)
        application.check_out_page.check_billing_address_params(create_user)
        application.stable_elements.scroll_page(200)

        application.check_out_page.verify_order_list([products_list[0]])
        application.stable_elements.scroll_page(300)

        application.check_out_page.enter_order_message('Успех приходит к тем, кто умеет применять свои знания, '
                                                       'а не к тому кто просто ими владеет!')

        application.check_out_page.press_button_place_order()

    with step('Переходим к заполнению данных для оплаты'):
        application.stable_elements.scroll_page(200)

        application.payment_page.fill_card_details_from_user_card(create_user.card)
        application.payment_page.press_pay_button()

    with step('Проверяем что заказ сформирован'):
        application.payment_page.verify_order_is_placed()

    with step('Удаляем пользователя'):
        application.navigation_bar.click_delete_user()

        check_account_is_deleted()


@allure.id('02_PLACE_ORDER')
@allure.tag('UI', 'PLACE_ORDER')
@allure.severity(Severity.BLOCKER)
@allure.parent_suite('UI')
@allure.suite('PLACE_ORDER')
@allure.label('owner', 'vssuchkov')
@allure.link('https://www.automationexercise.com', name='Testing UI')
def test_create_order_after_user_registration(setup_remote_browser, application, products_list, create_user):

    with step(f'Выполняем регистрацию пользователя {create_user}'):
        application.navigation_bar.open_login_page()
        application.signup_login_page.type_email(create_user.email)
        application.signup_login_page.type_sign_up_name(create_user.nick_name)
        application.signup_login_page.pres_button_signup()
        application.user_account_page.fill_user_personal_data(create_user)
        application.user_account_page.press_button_create_account()

    with step('Проверяем появление окна успешного создания пользователя'):
        check_account_is_create()

    with step('Проверяем, что пользователь залогинен после создания'):
        application.navigation_bar.check_user_is_login(create_user.nick_name)

    with step(f'Открываем страницу товаров и добавляем в корзину {products_list[0]}'):
        application.navigation_bar.open_products_page()
        application.stable_elements.scroll_page(500)
        application.products.add_wanted_product_in_cart(products_list[0].product_id)

    with step(f'Переходим в корзину и далее к оформлению заказа'):
        application.products.click_view_cart_page()
        application.cart_page.press_button_proceed_to_checkout()

    with step('Проверяем параметры заказа и добавляем сопроводительный комментарий'):
        application.check_out_page.check_delivery_address_params(create_user)
        application.check_out_page.check_billing_address_params(create_user)
        application.stable_elements.scroll_page(200)

        application.check_out_page.verify_order_list([products_list[0]])
        application.stable_elements.scroll_page(300)

        application.check_out_page.enter_order_message('Успех приходит к тем, кто умеет применять свои знания, '
                                                       'а не к тому кто просто ими владеет!')

        application.check_out_page.press_button_place_order()

    with step('Переходим к заполнению данных для оплаты'):
        application.stable_elements.scroll_page(200)

        application.payment_page.fill_card_details_from_user_card(create_user.card)
        application.payment_page.press_pay_button()

    with step('Проверяем что заказ сформирован'):
        application.payment_page.verify_order_is_placed()

    with step('Удаляем пользователя'):
        application.navigation_bar.click_delete_user()

        check_account_is_deleted()


@allure.id('03_PLACE_ORDER')
@allure.tag('UI', 'PLACE_ORDER')
@allure.severity(Severity.BLOCKER)
@allure.parent_suite('UI')
@allure.suite('PLACE_ORDER')
@allure.label('owner', 'vssuchkov')
@allure.link('https://www.automationexercise.com', name='Testing UI')
def test_create_order_after_user_login(setup_remote_browser, application, products_list, create_user_account, create_user):

    with step(f'Выполняем вход пользователем {create_user}'):
        application.navigation_bar.open_login_page()
        application.signup_login_page.type_email(create_user.email, is_login=True)
        application.signup_login_page.type_password(create_user.password)
        application.signup_login_page.type_sign_up_name(create_user.nick_name)
        application.signup_login_page.pres_button_login()

    with step('Проверяем, что пользователь залогинен после входа'):
        application.navigation_bar.check_user_is_login(create_user.nick_name)

    with step(f'Открываем страницу товаров и добавляем в корзину {products_list[0]}'):
        application.navigation_bar.open_products_page()
        application.stable_elements.scroll_page(500)
        application.products.add_wanted_product_in_cart(products_list[0].product_id)

    with step(f'Переходим в корзину и далее к оформлению заказа'):
        application.products.click_view_cart_page()
        application.cart_page.press_button_proceed_to_checkout()

    with step('Проверяем параметры заказа и добавляем сопроводительный комментарий'):
        application.check_out_page.check_delivery_address_params(create_user)
        application.check_out_page.check_billing_address_params(create_user)
        application.stable_elements.scroll_page(200)

        application.check_out_page.verify_order_list([products_list[0]])
        application.stable_elements.scroll_page(300)

        application.check_out_page.enter_order_message('Успех приходит к тем, кто умеет применять свои знания, '
                                                       'а не к тому кто просто ими владеет!')

        application.check_out_page.press_button_place_order()

    with step('Переходим к заполнению данных для оплаты'):
        application.stable_elements.scroll_page(200)

        application.payment_page.fill_card_details_from_user_card(create_user.card)
        application.payment_page.press_pay_button()

    with step('Проверяем что заказ сформирован'):
        application.payment_page.verify_order_is_placed()
