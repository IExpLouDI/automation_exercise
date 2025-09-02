import allure
from allure_commons.types import Severity



@allure.id('01_HOME_PAGE')
@allure.tag('UI', 'HOME_PAGE')
@allure.severity(Severity.CRITICAL)
@allure.parent_suite('UI')
@allure.suite('HOME_PAGE')
@allure.label('owner', 'vssuchkov')
@allure.link('https://www.automationexercise.com', name='Testing UI')
def test_verify_subscription_in_home_page(setup_remote_browser, application):
    application.home_page.scroll_down_to_footer()
    (application.footer
     .enter_email('f@ff.tt')
     .press_button()
     )
    application.footer.verify_success_subscribe()
