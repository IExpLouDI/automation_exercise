import allure
import pytest
from allure import step
from allure_commons.types import Severity

from automation_exercise.utils.base_test_request import BaseTestRequests
from src.automation_exercise.utils.static_values import StatusMessage


class TestUserAccount(BaseTestRequests):

    @allure.id('01_DELETE_REQUEST')
    @allure.tag('API', 'DELETE')
    @allure.severity(Severity.MINOR)
    @allure.parent_suite('API')
    @allure.suite('DELETE')
    @allure.label('owner', 'vssuchkov')
    @allure.link('https://www.automationexercise.com', name='Testing API')
    def test_valid_status_code(self, api_application, create_user_account):
        response_info = api_application.delete.user_account(create_user_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

    @allure.id('02_DELETE_REQUEST')
    @allure.tag('API', 'DELETE')
    @allure.severity(Severity.NORMAL)
    @allure.parent_suite('API')
    @allure.suite('DELETE')
    @allure.label('owner', 'vssuchkov')
    @allure.link('https://www.automationexercise.com', name='Testing API')
    def test_verify_response_message(self, api_application, create_user_account):
        response_info = api_application.delete.user_account(create_user_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step(f'Проверка текста сообщения успешного удаления = {StatusMessage.del_account_deleted.value}'):
            assert response_info.get('response').get(
                'message') == StatusMessage.del_account_deleted.value

    @allure.id('03_DELETE_REQUEST')
    @allure.tag('API', 'DELETE')
    @allure.severity(Severity.CRITICAL)
    @allure.parent_suite('API')
    @allure.suite('DELETE')
    @allure.label('owner', 'vssuchkov')
    @allure.link('https://www.automationexercise.com', name='Testing API')
    def test_check_user_after_delete(self, api_application, create_user_account):
        response_info = api_application.delete.user_account(create_user_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step(f'Выполняем запрос на проверку существования пользователя'):
            user_deleted_info = api_application.post.verify_login(create_user_account)

        with step(f'Проверяем что пользователь не существует'):
            assert user_deleted_info.get('response').get(
                'message') == StatusMessage.user_not_found.value

    @allure.id('04_DELETE_REQUEST')
    @allure.tag('API', 'DELETE')
    @allure.severity(Severity.CRITICAL)
    @allure.parent_suite('API')
    @allure.suite('DELETE')
    @allure.label('owner', 'vssuchkov')
    @allure.link('https://www.automationexercise.com', name='Testing API')
    def test_delete_without_email(self, api_application, create_user_account):
        create_user_account.pop('email')
        response_info = api_application.delete.user_account(create_user_account)
        self.check_response_status_and_message_business_code(response_info, 200, 400)

        with step(f'Проверка текста бизнес ошибки = {StatusMessage.bad_request_missing_email("DELETE")}'):
            assert response_info.get('response').get(
					'message') == StatusMessage.bad_request_missing_email("DELETE")

    @allure.id('05_DELETE_REQUEST')
    @allure.tag('API', 'DELETE')
    @allure.severity(Severity.CRITICAL)
    @allure.parent_suite('API')
    @allure.suite('DELETE')
    @allure.label('owner', 'vssuchkov')
    @allure.link('https://www.automationexercise.com', name='Testing API')
    def test_delete_without_password(self, api_application, create_user_account):
        create_user_account.pop('password')
        response_info = api_application.delete.user_account(create_user_account)
        self.check_response_status_and_message_business_code(response_info, 200, 400)

        with step(f'Проверка текста бизнес ошибки = {StatusMessage.bad_request_missing_password("DELETE")}'):
            assert response_info.get('response').get(
					'message') == StatusMessage.bad_request_missing_password("DELETE")


class TestVerifyLogin(BaseTestRequests):

    @allure.id('06_DELETE_REQUEST')
    @allure.tag('API', 'DELETE')
    @allure.severity(Severity.NORMAL)
    @allure.parent_suite('API')
    @allure.suite('DELETE')
    @allure.label('owner', 'vssuchkov')
    @allure.link('https://www.automationexercise.com', name='Testing API')
    @pytest.mark.xfail(reason='Метод находится в разработке')
    def test_valid_status_code(self, api_application):
        response_info = api_application.delete.verify_login()
        self.check_response_status_and_message_business_code(response_info, 200, 200)
