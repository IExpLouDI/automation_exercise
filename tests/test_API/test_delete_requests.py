from allure import step

from automation_exercise.utils.base_test_request import BaseTestRequests


class TestUserAccount(BaseTestRequests):

    def test_valid_status_code(self, api_application, create_account):
        response_info = api_application.delete.user_account(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

    def test_verify_response_message(self, api_application, create_account):
        response_info = api_application.delete.user_account(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step('Проверка текста сообщения успешного удаления = Account deleted!'):
            assert response_info.get('response').get(
                'message') == 'Account deleted!'

    def test_check_user_after_delete(self, api_application, create_account):
        response_info = api_application.delete.user_account(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step(f'Выполняем запрос на проверку существования пользователя'):
            user_deleted_info = api_application.post.verify_login(create_account)

        with step(f'Проверяем что пользователь не существует'):
            assert user_deleted_info.get('response').get(
                'message') == 'User not found!'