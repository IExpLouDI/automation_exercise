import allure
from allure import step
from src.automation_exercise.utils.check_functions import check_website_is_open, check_account_is_create
from src.automation_exercise.utils.check_functions import check_account_is_deleted


def test_user_registration(setup_remote_browser, create_user, application):

    check_website_is_open()

    with step('Открываем форму авторизации/регистрации'):
        application.navigation_bar.open_login_page()

    with step('Проверяем открытие формы регистрации/входа'):
        application.signup_login_page.check_signup_and_login_page_is_open()

    with step('Регистрируем пользователя'):
        (application.signup_login_page
         .type_sign_up_name(create_user.nick_name)
         .type_email(create_user.email)
         .pres_button_signup()
         )

    with step('Проверяем открытие формы ввода данных пользователя'):
        application.user_account_page.should_user_account_page_is_open()

    with (step('Заполняем данные пользователя')):
        (application.user_account_page
         .set_gender(create_user.gender)
         .enter_password(create_user.password)
         .scroll_page(300)
         .set_birthday(create_user.day,
                       create_user.month,
                       create_user.year)
         .press_newslatter_check_box()
         .press_special_offer_check_box()
         .scroll_page(300)
         .enter_first_name(create_user.first_name)
         .enter_last_name(create_user.last_name)
         .enter_company(create_user.company_name)
         .scroll_page(300)
         .enter_first_address(create_user.first_address)
         .enter_second_address(create_user.second_address)
         .scroll_page(100)
         .set_country(create_user.country)
         .enter_state(create_user.state)
         .enter_city(create_user.city)
         .enter_zip_code(create_user.zipcode)
         .enter_mobile_number(create_user.mobile_number)
         .scroll_page(200)
         .press_button_create_account()
         )

    with step('Проверяем появление окна успешного создания пользователя'):
        check_account_is_create()

    with step('Проверяем, что пользователь залогинен после создания'):
        application.navigation_bar.check_user_is_login(create_user.nick_name)

    with step('Удаляем созданного пользователя'):
        application.navigation_bar.click_delete_user()
        check_account_is_deleted()


def test_registration_user_with_existing_email(setup_remote_browser, create_user, create_account, application):

    with step('Открываем форму авторизации/регистрации'):
        application.navigation_bar.open_login_page()

    with step('Вводим в форму регистрации данные существующего пользователя'):
        (application.signup_login_page
         .type_sign_up_name(create_user.nick_name)
         .type_email(create_user.email)
         .pres_button_signup()
         )

    with step('Проверяем появление ошибки'):
        application.signup_login_page.verify_enter_existing_email()


def test_registration_while_checkout(setup_remote_browser, application, products_list, create_user):
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

        application.check_out_page.verify_order_list(list(products_list[0]))
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
        application.payment_page.press_continue()

    with step('Удаляем пользователя'):
        application.navigation_bar.click_delete_user()

        check_account_is_deleted()
