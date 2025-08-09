import allure
from selene import browser, be, have

from automation_exercise.app import Application


def test_available():
    # setTimeout(function() {debugger;}, 5000)
    browser.open('https://www.automationexercise.com')
    browser.element("h2.title").should(be.present)

def test_case_1(setup_browser):
    app = Application()

    browser.element("[alt='Website for automation practice']").should(be.visible)

    with allure.step('Нажимаем в навигации на форму регистрации/входа'):
        app.navigation_bar.open_login_page()
    # browser.element("//a[text()=' Signup / Login']").click()

    with allure.step('Проверяем открытие формы регистрации/входа'):
        browser.element("//h2[text()='New User Signup!']").should(be.visible)

    # browser.element("[data-qa='signup-name']").type('Name')
    # browser.element("[data-qa='signup-email']").type('email@t.com')
    # browser.element("[data-qa='signup-button']").click()
    with allure.step('Регестрируем пользователя'):
        (app.signup_login_page
         .type_sign_up_name('Name')
         .type_email('email@ttest.com')
         .pres_button_signup()
         )

    with allure.step('Проверяем открытие формы с данными пользователя'):
        browser.element('h2.title').should(be.visible)

    with (allure.step('Заполняем данные пользователя')):
        (app.user_account_page
         .set_gender('male')
         .enter_password('Qwe123')
         .scroll_page(300)
         .set_birthday('3','3','2000')
         .press_newslatter_check_box()
         .press_special_offer_check_box()
         .scroll_page(300)
         .enter_first_name('T1')
         .enter_last_name('T2')
         .enter_company('T3')
         .scroll_page(300)
         .enter_first_address('AA1')
         .enter_second_address('AA3')
         .scroll_page(100)
         .set_country('India')
         .enter_state('T4')
         .enter_city('T5')
         .enter_zip_code('T6')
         .enter_mobile_number('T7')
        .scroll_page(200)
         .press_button_create_account()
         )
        with allure.step('Проверяем форму успешного созданиы пользователя'):
            browser.element("[data-qa='account-created']").should(be.visible)
            browser.element("[data-qa='continue-button']").click()

        with allure.step('Проверяем, что пользователь залогинен после создания'):
            browser.element("//a[contains(text(), 'Logged')]").should(have.text(f'Logged in as {"Name"}'))

        with allure.step('Удаляем созданного пользователя'):
            app.navigation_bar.click_delete_user()
            browser.element("[data-qa='account-deleted']").should(be.visible)
            browser.element("[data-qa='continue-button']").click()
    # browser.element('h2.title').should(be.visible)
    #
    # browser.element('#id_gender2').click()
    # browser.element("[data-qa='password']").type('Qwe123')
    #
    # browser.execute_script("window.scrollBy(0, 300);")
    #
    # browser.element("[data-qa='days']").click()
    # browser.element("#uniform-days option[value='3']").click()
    #
    # browser.element("[data-qa='months']").click()
    # browser.element("#uniform-months option[value='3']").click()
    #
    # browser.element("[data-qa='years']").click()
    # browser.element("#uniform-years option[value='2000']").click()
    #
    # browser.element('#uniform-newsletter input').click()
    # browser.element('#optin').click()
    #
    # browser.execute_script("window.scrollBy(0, 300);")
    #
    # browser.element("[data-qa='first_name']").type('Frederick')
    # browser.element("[data-qa='last_name']").type('Hommers')
    # browser.element("[data-qa='company']").type('Testersvallers')
    #
    # browser.execute_script("window.scrollBy(0, 300);")
    #
    # browser.element("[data-qa='address']").type('Testersvallers')
    # browser.element("[data-qa='address2']").type('Testersvallers')
    #
    # browser.execute_script("window.scrollBy(0, 100);")
    #
    # browser.element("[data-qa='country']").click()
    # browser.element("option[value='India']").click()
    #
    # browser.element("[data-qa='state']").type('Alasksa')
    # browser.element("[data-qa='city']").type('Alasksa')
    # browser.element("[data-qa='zipcode']").type('2333221')
    # browser.element("[data-qa='mobile_number']").type('2333221')
    #
    # browser.execute_script("window.scrollBy(0, 200);")
    #
    # browser.element("[data-qa='create-account']").click()
    #
    # browser.element("[data-qa='account-created']").should(be.visible)

    # browser.element("[data-qa='continue-button']").click()
    #
    # browser.element("//a[contains(text(), 'Logged')]").should(have.text(f'Logged in as {"Name"}'))

    # browser.element("//a[text()=' Delete Account']").click()
    # browser.element("[data-qa='account-deleted']").should(be.visible)

    # browser.element("[data-qa='continue-button']").click()
