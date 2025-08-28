import pytest
from allure import step

from automation_exercise.utils.base_test_request import BaseTestRequests
from automation_exercise.utils.helpers import switch_search_param_case
from automation_exercise.utils.static_values import StatusMessage
from tests.conftest import api_application


class TestProductsList(BaseTestRequests):
    @pytest.mark.xfail(reason='Метод находится в разработке')
    def test_valid_status_code(self, api_application):
        response_info = api_application.post.product_list()
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


class TestVerifyLogin(BaseTestRequests):

    def test_valid_status_code(self, api_application, create_account):
        response_info = api_application.post.verify_login(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

    def test_verify_user_exists(self, api_application, create_account):
        with step(f'Выполняем запрос c {create_account}'):
            response_info = api_application.post.verify_login(create_account)
        self.check_response_status_and_message_business_code(response_info, 200, 200)

        with step(f'Проверяем, что сообщение в ответе = {StatusMessage.post_verify_user_exists.value}'):
            assert response_info.get('response').get('message') == StatusMessage.post_verify_user_exists.value

    def test_verify_user_not_found(self, api_application, not_found_user):
        with step(f'Выполняем запрос c {not_found_user}'):
            response_info = api_application.post.verify_login(not_found_user)
        self.check_response_status_and_message_business_code(response_info, 200, 404)

        with step(f'Проверяем, что сообщение в ответе = {StatusMessage.user_not_found.value}'):
            assert response_info.get('response').get('message') == StatusMessage.user_not_found.value

    def test_without_email(self, api_application, create_account):
        create_account.pop('email')
        with step(f'Выполняем запрос c {create_account}'):
            response_info = api_application.post.verify_login(create_account)

        self.check_response_status_and_message_business_code(response_info, 200, 400)

        with step(f'Проверяем, что сообщение в ответе = {StatusMessage.post_verify_user_exists.value}'):
            assert response_info.get('response').get('message') == StatusMessage.post_bad_request.value

    def test_without_password(self, api_application, create_account):
        create_account.pop('password')
        with step(f'Выполняем запрос c {create_account}'):
            response_info = api_application.post.verify_login(create_account)

        self.check_response_status_and_message_business_code(response_info, 200, 400)

        with step(f'Проверяем, что сообщение в ответе = {StatusMessage.post_verify_user_exists.value}'):
            assert response_info.get('response').get('message') == StatusMessage.post_bad_request.value


class TestCreateAccount(BaseTestRequests):

    def test_successful_account_creation(self, api_application, create_user):
        with step('Создаем аккаунт через API'):
            response_info = api_application.post.create_account(create_user.info)
        with step(f'Выполняем запрос c {create_account}'):
            response_info = api_application.post.create_account(create_account)

        with step('Проверяем статус код 201'):
            assert response_info.get('status_code') == 201

        with step('Проверяем код ответа и сообщение'):
            assert response_info.get('response').get('responseCode') == 201
            assert response_info.get('response').get('message') == StatusMessage.post_user_created.value

        # Очистка - удаляем созданный аккаунт
        api_application.delete.user_account(create_user.email, create_user.password)

    def test_account_creation_existing_email(self, api_application, create_account, create_user):
        with step('Пытаемся создать аккаунт с существующим email'):
            response_info = api_application.post.create_account(create_user)

        with step('Проверяем статус код 400'):
            assert response_info.get('status_code') == 400

        with step('Проверяем код ответа и сообщение об ошибке'):
            assert response_info.get('response').get('responseCode') == 400
            assert response_info.get('response').get('message') == StatusMessage.email_exists.value

    def test_account_creation_missing_required_field(self, api_application, create_user):
        """Тест создания аккаунта без обязательного поля"""
        # Удаляем обязательное поле (email)
        create_user.email = None

        with step('Пытаемся создать аккаунт без email'):
            response_info = api_application.post.create_account(create_user)

        with step('Проверяем статус код 400'):
            assert response_info.get('status_code') == 400

        with step('Проверяем наличие сообщения об ошибке'):
            # Конкретное сообщение может варьироваться в зависимости от API
            assert 'email' in response_info.get('response').get('message').lower()

    def test_account_creation_invalid_email_format(self, api_application, create_user):
        """Тест создания аккаунта с некорректным форматом email"""
        create_user.email = 'invalid-email-format'

        with step('Пытаемся создать аккаунт с некорректным email'):
            response_info = api_application.post.create_account(create_user)

        with step('Проверяем статус код 400'):
            assert response_info.get('status_code') == 400

        with step('Проверяем сообщение об ошибке формата email'):
            assert 'email' in response_info.get('response').get('message').lower()
            assert 'valid' in response_info.get('response').get('message').lower()

    def test_account_creation_short_password(self, api_application, create_user):
        """Тест создания аккаунта с слишком коротким паролем"""
        create_user.password = '123'

        with step('Пытаемся создать аккаунт с коротким паролем'):
            response_info = api_application.post.create_account(create_user)

        with step('Проверяем статус код 400'):
            assert response_info.get('status_code') == 400

        with step('Проверяем сообщение об ошибке пароля'):
            assert 'password' in response_info.get('response').get('message').lower()

    @pytest.mark.parametrize('field', ['first_name', 'last_name', 'country'])
    def test_account_creation_missing_optional_field(self, api_application, create_user, field):
        """Тест создания аккаунта без необязательных полей"""
        # Устанавливаем необязательное поле в None
        setattr(create_user, field, None)

        with step(f'Пытаемся создать аккаунт без поля {field}'):
            response_info = api_application.post.create_account(create_user)

        with step('Проверяем успешное создание аккаунта (статус 201)'):
            assert response_info.get('status_code') == 201

        # Очистка - удаляем созданный аккаунт
        delete_account(create_user.email, create_user.password)

    def test_account_creation_verify_schema(self, api_application, create_user, load_schema):
        """Тест проверки схемы ответа при создании аккаунта"""
        with step('Создаем аккаунт и проверяем схему ответа'):
            response_info = api_application.post.create_account(create_user)
            self.validate_response_schema(
                load_schema.get('post_create_account'),
                response_info.get('response')
            )

        # Очистка - удаляем созданный аккаунт
        delete_account(create_user.email, create_user.password)