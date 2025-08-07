from selene import browser, be


def test_available():
    # setTimeout(function() {debugger;}, 5000)
    browser.open('https://www.automationexercise.com')
    browser.element("h2.title").should(be.present)

def test_case_1(setup_browser):
    browser.open('/')
    browser.element("[alt='Website for automation practice']").should(be.visible)

    browser.element("//a[text()=' Signup / Login']").click()
    browser.element("//h2[text()='New User Signup!']").should(be.visible)

    browser.element("[data-qa='signup-name']").type('Name')
    browser.element("[data-qa='signup-email']").type('email@t.com')
    browser.element("[data-qa='signup-button']").click()

    browser.element('h2.title').should(be.visible)

    browser.element('#id_gender2').click()

    browser.execute_script("window.scrollBy(0, 300);")

    browser.element("[data-qa='days']").click()
    browser.element("#uniform-days option[value='3']").click()

    browser.element("[data-qa='months']").click()
    browser.element("#uniform-months option[value='3']").click()

    browser.element("[data-qa='years']").click()
    browser.element("#uniform-years option[value='2000']").click()

    browser.element('#uniform-newsletter input').click()
    browser.element('#optin').click()


