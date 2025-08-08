from selene import browser, be, have


def test_available():
    # setTimeout(function() {debugger;}, 5000)
    browser.open('https://www.automationexercise.com')
    browser.element("h2.title").should(be.present)

def test_case_1(setup_browser):
    browser.open('https://www.automationexercise.com')
    browser.element("[alt='Website for automation practice']").should(be.visible)

    browser.element("//a[text()=' Signup / Login']").click()
    browser.element("//h2[text()='New User Signup!']").should(be.visible)

    browser.element("[data-qa='signup-name']").type('Name')
    browser.element("[data-qa='signup-email']").type('email@t.com')
    browser.element("[data-qa='signup-button']").click()

    browser.element('h2.title').should(be.visible)

    browser.element('#id_gender2').click()
    browser.element("[data-qa='password']").type('Qwe123')

    browser.execute_script("window.scrollBy(0, 300);")

    browser.element("[data-qa='days']").click()
    browser.element("#uniform-days option[value='3']").click()

    browser.element("[data-qa='months']").click()
    browser.element("#uniform-months option[value='3']").click()

    browser.element("[data-qa='years']").click()
    browser.element("#uniform-years option[value='2000']").click()

    browser.element('#uniform-newsletter input').click()
    browser.element('#optin').click()

    browser.execute_script("window.scrollBy(0, 300);")

    browser.element("[data-qa='first_name']").type('Frederick')
    browser.element("[data-qa='last_name']").type('Hommers')
    browser.element("[data-qa='company']").type('Testersvallers')

    browser.execute_script("window.scrollBy(0, 300);")

    browser.element("[data-qa='address']").type('Testersvallers')
    browser.element("[data-qa='address2']").type('Testersvallers')

    browser.execute_script("window.scrollBy(0, 100);")

    browser.element("[data-qa='country']").click()
    browser.element("option[value='India']").click()

    browser.element("[data-qa='state']").type('Alasksa')
    browser.element("[data-qa='city']").type('Alasksa')
    browser.element("[data-qa='zipcode']").type('2333221')
    browser.element("[data-qa='mobile_number']").type('2333221')

    browser.execute_script("window.scrollBy(0, 200);")

    browser.element("[data-qa='create-account']").click()

    browser.element("[data-qa='account-created']").should(be.visible)

    browser.element("[data-qa='continue-button']").click()

    browser.element("//a[contains(text(), 'Logged')]").should(have.text(f'Logged in as {"Name"}'))

    browser.element("//a[text()=' Delete Account']").click()
    browser.element("[data-qa='account-deleted']").should(be.visible)

    browser.element("[data-qa='continue-button']").click()
