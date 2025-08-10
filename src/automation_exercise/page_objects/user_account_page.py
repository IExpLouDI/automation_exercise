import allure
from selene import browser, be


class UserAccountPage:
    def __init__(self):
        self.male_gender = browser.element('#id_gender1')
        self.female_gender = browser.element('#id_gender2')
        self.nick_name = browser.element("[data-qa='name']")
        self.email = browser.element("[data-qa='email']")
        self.password = browser.element("[data-qa='password']")
        self.user_birth_day = browser.element("[data-qa='days']")
        self.user_birth_month = browser.element("[data-qa='days']")
        self.user_birth_year = browser.element("[data-qa='years']")
        self.news_later = browser.element('#uniform-newsletter input')
        self.special_offers = browser.element('#optin')
        self.first_name = browser.element("[data-qa='first_name']")
        self.last_name = browser.element("[data-qa='last_name']")
        self.company_name = browser.element("[data-qa='company']")
        self.first_address = browser.element("[data-qa='address']")
        self.second_address = browser.element("[data-qa='address2']")
        self.country = browser.element("[data-qa='country']")
        self.state = browser.element("[data-qa='state']")
        self.city = browser.element("[data-qa='city']")
        self.zipcode = browser.element("[data-qa='zipcode']")
        self.mobile_number = browser.element("[data-qa='mobile_number']")
        self.button_create_account = browser.element("[data-qa='create-account']")


    def set_gender(self, value:str):
        with allure.step(f'Устанавливаем пол пользователя - {value}'):
            self.male_gender.click() \
                if value.lower() == 'male' \
                else self.female_gender.click()

        return self

    def enter_nick_name(self, value):
        with allure.step(f'Устанавливаем никнейм пользователя - {value}'):
            self.nick_name.type(value)

        return self

    def enter_email(self, value):
        with allure.step(f'Устанавливаем email пользователя - {value}'):
            self.email.type(value)

        return self

    def enter_password(self, value):
        with allure.step(f'Устанавливаем пароль - {value}'):
            self.password.type(value)

        return self

    def set_birthday(self, us_day, us_month, us_year):
        with allure.step(f'Устанавливаем день рождения - {us_year}-{us_month}-{us_day}'):
            self.user_birth_day.click()
            browser.element(f"#uniform-days option[value='{us_day}']").click()

            self.user_birth_month.click()
            browser.element(f"#uniform-months option[value='{us_month}']").click()

            self.user_birth_month.click()
            browser.element(f"#uniform-months option[value='{us_month}']").click()

        return self

    def press_newslatter_check_box(self):
        with allure.step('Нажимаем на чек бокс newslatter'):
            self.news_later.click()

        return self

    def press_special_offer_check_box(self):
        with allure.step('Нажимаем на чек бокс special offer'):
            self.special_offers.click()

        return self

    def enter_first_name(self, value:str):
        with allure.step(f'Ввод имени пользователя - {value}'):
            self.first_name.type(value)

        return self

    def enter_last_name(self, value:str):
        with allure.step(f'Ввод фамилии пользователя - {value}'):
            self.last_name.type(value)

        return self

    def enter_company(self, value:str):
        with allure.step(f'Ввод названия компании - {value}'):
            self.company_name.type(value)

        return self

    def enter_first_address(self, value:str):
        with allure.step(f'Ввод первого адреса - {value}'):
            self.first_address.type(value)

        return self

    def enter_second_address(self, value:str):
        with allure.step(f'Ввод второго адреса - {value}'):
            self.second_address.type(value)

        return self

    def set_country(self, value):
        with allure.step(f"Выбираем страну - {value}"):
            browser.element("[data-qa='country']").click()
            browser.element(f"option[value='{value}']").click()

        return self

    def enter_state(self, value:str):
        with allure.step(f"Вводим область - {value}"):
           self.state.type(value)

        return self

    def enter_city(self, value:str):
        with allure.step(f"Вводим город - {value}"):
           self.city.type(value)

        return self

    def enter_zip_code(self, value:str):
        with allure.step(f"Вводим индекс - {value}"):
           self.zipcode.type(value)

        return self

    def enter_mobile_number(self, value:str):
        with allure.step(f"Вводим индекс - {value}"):
           self.mobile_number.type(value)

        return self

    def press_button_create_account(self):
        with allure.step(f"Нажимаем кнопку CREATE-ACCOUNT"):
            self.button_create_account.click()

    def scroll_page(self, step:int):
        browser.execute_script(f"window.scrollBy(0, {step});")

        return self

    def should_user_account_page_is_open(self):
        browser.element('h2.title').should(be.visible)
