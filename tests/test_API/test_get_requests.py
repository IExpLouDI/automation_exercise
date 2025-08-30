from automation_exercise.utils.base_test_request import BaseTestRequests
from automation_exercise.utils.check_functions import check_response_content
from allure import step

from automation_exercise.utils.static_values import StatusMessage


class TestAllProducts(BaseTestRequests):

    def test_valid_schema(self, api_application, load_schema):
        response_info = api_application.get.all_product()
        self.validate_response_schema(load_schema['get_all_product_list'], response_info.get('response'))

    def test_valid_status_code(self, api_application):
        response_info = api_application.get.all_product()
        self.check_response_status_and_message_business_code(response_info, 200, 200)


class TestAllBrands(BaseTestRequests):

    def test_valid_schema(self, api_application, load_schema):
        response_info = api_application.get.all_brand_list()
        self.validate_response_schema(load_schema.get('get_brands_list'), response_info.get('response'))

    def test_valid_status_code(self, api_application):
        response_info = api_application.get.all_brand_list()
        self.check_response_status_and_message_business_code(response_info, 200, 200)


class TestUserAccountDetail(BaseTestRequests):

    def test_valid_schema(self, api_application, load_schema, create_user, create_user_account):
        response_info = api_application.get.user_account_detail_by_email(create_user.email)
        self.validate_response_schema(load_schema['get_user_account_detail'], response_info.get('response'))

    def test_valid_status_code(self, api_application, create_user, create_user_account):
        response_info = api_application.get.user_account_detail_by_email(create_user.email)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

    def test_with_not_exist_email(self, api_application, create_user):
        response_info = api_application.get.user_account_detail_by_email(create_user.email)
        self.check_response_status_and_message_business_code(response_info, 200, 404)

        with step(f'Проверка текста бизнес ошибки = {StatusMessage.get_account_not_found.value}'):
            assert response_info.get('response').get(
                'message') == StatusMessage.get_account_not_found.value

    def test_with_check_content(self, api_application, create_user, create_user_account):
        response_info = api_application.get.user_account_detail_by_email(create_user.email)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step(f'Проверка контента ответа на совпадение с данными пользователя {create_user}'):
            check_response_content(response_info.get('response'), create_user.info)
