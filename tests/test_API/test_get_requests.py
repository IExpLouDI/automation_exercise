import json
import os
from jsonschema import validate
from automation_exercise.utils.check_functions import validate_response_schema, check_response_content
from allure import step


class BaseTestGetRequests:

    # def verify_response_schema(self, response, schema_path):
    #     validate_response_schema(schema_path, response)

    def validate_response_schema(self,schema_path, response: dict) -> None:
        with step(f'Проверяем соответствие схеме {os.path.basename(schema_path)}'):
            with open(schema_path, 'r', encoding='utf-8') as file:
                schema = json.loads(file.read())

            validate(instance=response, schema=schema)

    def check_response_status_and_message_business_code(self,
                                                        response: dict,
                                                        wait_status_code: int,
                                                        wait_business_code: int = None) -> None:

        with step(f'Проверка статуса ответа = {wait_status_code}'):
            assert response.get('status_code') == wait_status_code

        if wait_business_code is not None:
            with step(f'Проверка бизнес кода ответа = {wait_business_code}'):
                assert response.get('response').get('responseCode') == wait_business_code


class TestGetAllProducts(BaseTestGetRequests):

    def test_valid_schema(self, api_application, load_schema):
        response_info = api_application.get.get_all_product()
        self.validate_response_schema(load_schema['get_all_product_list'], response_info.get('response'))
        # self.verify_response_schema(response_info, load_schema['get_all_product_list'])

    def test_valid_status_code(self, api_application):
        response_info = api_application.get.get_all_product()
        self.check_response_status_and_message_business_code(response_info, 200, 200)


class TestGetAllBrands(BaseTestGetRequests):

    def test_valid_schema(self, api_application, load_schema):
        response_info = api_application.get.get_all_brand_list()
        self.validate_response_schema(load_schema['get_brands_list'], response_info.get('response'))

    def test_valid_status_code(self, api_application):
        response_info = api_application.get.get_all_brand_list()
        self.check_response_status_and_message_business_code(response_info, 200, 200)


class TestGetUserAccountDetail(BaseTestGetRequests):

    def test_valid_schema(self, api_application, load_schema, create_user, create_account):
        response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
        self.validate_response_schema(load_schema['get_user_account_detail'], response_info.get('response'))

    def test_valid_status_code(self, api_application, create_user, create_account):
        response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

    def test_with_not_exist_email(self, api_application, create_user):
        response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
        self.check_response_status_and_message_business_code(response_info, 200, 404)

        with step('Проверка текста бизнес ошибки = Account not found with this email, try another email!'):
            assert response_info.get('response').get(
                'message') == 'Account not found with this email, try another email!'

    def test_with_check_content(self, api_application, create_user, create_account):
        response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step(f'Проверка контента ответа на совпадение с данными пользователя {create_user}'):
            check_response_content(response_info.get('response'), create_user.info)


#
# def test_get_all_product_valid_shema(api_application, load_schema):
#     response_info = api_application.get.get_all_product()
#     validate_response_schema(load_schema['get_all_product_list'], response_info.get('response'))
#
#
# def test_get_all_product_valid_status_code(api_application):
#     response_info = api_application.get.get_all_product()
#
#     check_response_status_and_message_business_code(response_info, 200, 200)
#
#
# def test_get_all_brand_list_valid_shema(api_application, load_schema):
#     response_info = api_application.get.get_all_brand_list()
#     validate_response_schema(load_schema['get_brands_list'], response_info.get('response'))
#
#
# def test_get_all_brand_list_valid_status_code(api_application):
#     response_info = api_application.get.get_all_brand_list()
#     check_response_status_and_message_business_code(response_info, 200, 200)
#
#
# def test_get_user_account_detail_valid_schema(api_application, load_schema, create_user, create_account):
#     response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
#     validate_response_schema(load_schema['get_user_account_detail'], response_info.get('response'))
#
#
# def test_get_user_account_detail_valid_status_code(api_application, create_user, create_account):
#     response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
#     check_response_status_and_message_business_code(response_info, 200, 200)
#
#
# def test_get_user_account_detail_with_not_exist_email(api_application, create_user):
#     response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
#     check_response_status_and_message_business_code(response_info, 200, 404)
#
#     with step('Проверка текста бизнес ошибки = Account not found with this email, try another email!'):
#         assert response_info.get('response').get('message') == 'Account not found with this email, try another email!'
#
#
# def test_get_user_account_detail_with_check_content(api_application, create_user, create_account):
#     response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
#     check_response_status_and_message_business_code(response_info, 200, 200)
#
#     with step(f'Проверка контента ответа на совпадение с данными пользователя {create_user}'):
#         check_response_content(response_info.get('response'), create_user.info)
