import pytest
from allure import step

from automation_exercise.utils.base_test_request import BaseTestRequests
from src.automation_exercise.utils.static_values import StatusMessage


class TestUserAccount(BaseTestRequests):

    def test_valid_status_code(self, api_application, create_account):
        response_info = api_application.delete.user_account(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

    def test_verify_response_message(self, api_application, create_account):
        response_info = api_application.delete.user_account(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step(f'Проверка текста сообщения успешного удаления = {StatusMessage.del_account_deleted.value}'):
            assert response_info.get('response').get(
                'message') == StatusMessage.del_account_deleted.value

    def test_check_user_after_delete(self, api_application, create_account):
        response_info = api_application.delete.user_account(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step(f'Выполняем запрос на проверку существования пользователя'):
            user_deleted_info = api_application.post.verify_login(create_account)

        with step(f'Проверяем что пользователь не существует'):
            assert user_deleted_info.get('response').get(
                'message') == StatusMessage.user_not_found.value

    def test_delete_without_email(self, api_application, create_account):
        create_account.pop('email')
        response_info = api_application.delete.user_account(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 400)

        with step(f'Проверка текста бизнес ошибки = {StatusMessage.bad_request_missing_email("DELETE")}'):
            assert response_info.get('response').get(
					'message') == StatusMessage.bad_request_missing_email("DELETE")

    def test_delete_without_password(self, api_application, create_account):
        create_account.pop('password')
        response_info = api_application.delete.user_account(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 400)

        with step(f'Проверка текста бизнес ошибки = {StatusMessage.bad_request_missing_password("DELETE")}'):
            assert response_info.get('response').get(
					'message') == StatusMessage.bad_request_missing_password("DELETE")


class TestVerifyLogin(BaseTestRequests):

    @pytest.mark.xfail(reason='Метод находится в разработке')
    def test_valid_status_code(self, api_application):
        response_info = api_application.delete.verify_login()
        self.check_response_status_and_message_business_code(response_info, 200, 200)
