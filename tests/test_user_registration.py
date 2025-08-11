import allure
from selene import browser, be

from automation_exercise.app import Application
from automation_exercise.utils.check_functions import check_website_is_open, check_account_is_create, check_account_is_deleted


def test_available():
    # setTimeout(function() {debugger;}, 5000)
    browser.open('https://www.automationexercise.com')
    browser.element("h2.title").should(be.present)

def test_case_1(setup_browser, create_user):
    app = Application()

    check_website_is_open()

    with allure.step('Нажимаем в навигации на форму регистрации/входа'):
        app.navigation_bar.open_login_page()

    with allure.step('Проверяем открытие формы регистрации/входа'):
        app.signup_login_page.check_signup_and_login_page_is_open()
        # browser.element("//h2[text()='New User Signup!']").should(be.visible)

    with allure.step('Регистрируем пользователя'):
        (app.signup_login_page
         .type_sign_up_name(create_user.nick_name)
         .type_email(create_user.email)
         .pres_button_signup()
         )

    with allure.step('Проверяем открытие формы с данными пользователя'):
        app.user_account_page.should_user_account_page_is_open()

    with (allure.step('Заполняем данные пользователя')):
        (app.user_account_page
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

    with allure.step('Проверяем форму успешного создания пользователя'):
        check_account_is_create()

    with allure.step('Проверяем, что пользователь залогинен после создания'):
        app.navigation_bar.check_user_is_login(create_user.nick_name)

    with allure.step('Удаляем созданного пользователя'):
        app.navigation_bar.click_delete_user()
        check_account_is_deleted()
