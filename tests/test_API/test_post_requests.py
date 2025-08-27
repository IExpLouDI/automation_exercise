import pytest
from allure import step

from automation_exercise.utils.base_test_request import BaseTestRequests
from automation_exercise.utils.helpers import switch_search_param_case
from automation_exercise.utils.static_values import StatusMessage


class TestProductsList(BaseTestRequests):
    @pytest.mark.xfail(reason='Метод находится в разработке')
    def test_valid_status_code(self, api_application):
        response_info = api_application.post.product_list
        self.check_response_status_and_message_business_code(response_info, 200, 200)


class TestSearchProduct(BaseTestRequests):

    def test_valid_status_code(self, api_application, search_param):
        with step(f'Выполняем запрос'):
            response_info = api_application.post.search_product(search_param)
        self.check_response_status_and_message_business_code(response_info, 200, 200)


    def test_verify_response_schema(self, api_application, load_schema, search_param):
        with step(f'Выполняем запрос'):
            response_info = api_application.post.search_product(search_param)
        self.validate_response_schema(load_schema.get('post_search_product'), response_info.get('response'))


    def test_without_search_param(self, api_application, no_valid_search_param):
        with step(f'Выполняем запрос'):
            response_info = api_application.post.search_product(no_valid_search_param)

        self.check_response_status_and_message_business_code(response_info, 200, 400)

        with step(f'Проверка текста бизнес ошибки = {StatusMessage.post_missing_search_param.value}'):
            assert response_info.get('response').get(
                'message') == StatusMessage.post_missing_search_param.value


    def test_parameter_is_not_case_sensitive(self, api_application, search_param):
        with step(f'Выполняем запрос c {search_param}'):
            response_info = api_application.post.search_product(search_param)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step(f'Выполняем запрос c {switch_search_param_case(search_param)}'):
            response_info_switch = api_application.post.search_product(search_param)
        self.check_response_status_and_message_business_code(response_info_switch, 200, 200)

        with step(f'Проверка, что количество записей в ответе не изменилось'):
            assert len(
                response_info.get('response').get('products')
            ) == len(
                response_info_switch.get('response').get('products')
            )

        with step('Проверка неизменности контента'):
            assert response_info == response_info_switch
