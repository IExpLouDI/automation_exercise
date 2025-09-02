import allure
import pytest
from allure import step
from allure_commons.types import Severity

from automation_exercise.utils.base_test_request import BaseTestRequests
from automation_exercise.utils.check_functions import check_response_message_content
from automation_exercise.utils.static_values import StatusMessage


class TestAllBrandList(BaseTestRequests):
	@allure.id('01_PUT_REQUEST')
	@allure.tag('API', 'PUT')
	@allure.severity(Severity.NORMAL)
	@allure.parent_suite('API')
	@allure.suite('PUT')
	@allure.label('owner', 'vssuchkov')
	@allure.link('https://www.automationexercise.com', name='Testing API')
	@pytest.mark.xfail(reason='Метод находится в разработке')
	def test_valid_status_code(self, api_application):
		response_info = api_application.put.all_brand_list()
		self.check_response_status_and_message_business_code(response_info, 200, 200)


class TestUpdateUserAccount(BaseTestRequests):

	@allure.id('02_PUT_REQUEST')
	@allure.tag('API', 'PUT')
	@allure.severity(Severity.NORMAL)
	@allure.parent_suite('API')
	@allure.suite('PUT')
	@allure.label('owner', 'vssuchkov')
	@allure.link('https://www.automationexercise.com', name='Testing API')
	def test_valid_status_code(self, api_application, create_user, update_user_params, create_user_account):
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)
		self.check_response_status_and_message_business_code(response_info, 200, 200)

	@allure.id('03_PUT_REQUEST')
	@allure.tag('API', 'PUT')
	@allure.severity(Severity.NORMAL)
	@allure.parent_suite('API')
	@allure.suite('PUT')
	@allure.label('owner', 'vssuchkov')
	@allure.link('https://www.automationexercise.com', name='Testing API')
	def test_verify_response_message(self, api_application, create_user, update_user_params, create_user_account):
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 200)

		with step(f'Проверка текста сообщения успешного обновления = {StatusMessage.put_user_update.value}'):
			assert response_info.get('response').get(
					'message') == StatusMessage.put_user_update.value

	@allure.id('04_PUT_REQUEST')
	@allure.tag('API', 'PUT')
	@allure.severity(Severity.CRITICAL)
	@allure.parent_suite('API')
	@allure.suite('PUT')
	@allure.label('owner', 'vssuchkov')
	@allure.link('https://www.automationexercise.com', name='Testing API')
	def test_check_user_after_update(self, api_application, create_user, update_user_params, create_user_account):
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 200)

		with step(f'Выполняем запрос get на получение информации о пользователе'):
			account_info = api_application.get.user_account_detail_by_email(create_user.email)

		with step('Проверяем изменённые параметры пользователя'):
			check_response_message_content(account_info, update_user_params)

	@allure.id('05_PUT_REQUEST')
	@allure.tag('API', 'PUT')
	@allure.severity(Severity.BLOCKER)
	@allure.parent_suite('API')
	@allure.suite('PUT')
	@allure.label('owner', 'vssuchkov')
	@allure.link('https://www.automationexercise.com', name='Testing API')
	def test_update_without_email(self, api_application, create_user, update_user_params, create_user_account):
		update_user_params.pop('email')
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 400)

		with step(f'Проверка текста бизнес ошибки = {StatusMessage.bad_request_missing_email("put")}'):
			assert response_info.get('response').get(
					'message') == StatusMessage.bad_request_missing_email("put")


	@allure.id('06_PUT_REQUEST')
	@allure.tag('API', 'PUT')
	@allure.severity(Severity.BLOCKER)
	@allure.parent_suite('API')
	@allure.suite('PUT')
	@allure.label('owner', 'vssuchkov')
	@allure.link('https://www.automationexercise.com', name='Testing API')
	def test_update_without_password(self, api_application, create_user, update_user_params, create_user_account):
		update_user_params.pop('password')
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 400)

		with step(f'Проверка текста бизнес ошибки = {StatusMessage.bad_request_missing_password("put")}'):
			assert response_info.get('response').get(
					'message') == StatusMessage.bad_request_missing_password("put")


	@allure.id('07_PUT_REQUEST')
	@allure.tag('API', 'PUT')
	@allure.severity(Severity.CRITICAL)
	@allure.parent_suite('API')
	@allure.suite('PUT')
	@allure.label('owner', 'vssuchkov')
	@allure.link('https://www.automationexercise.com', name='Testing API')
	def test_with_not_exist_email(self, api_application, update_user_params):
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 404)

		with step(f'Проверка текста бизнес ошибки = {StatusMessage.put_account_not_found.value}'):
			assert response_info.get('response').get(
				'message') == StatusMessage.put_account_not_found.value


	@allure.id('08_PUT_REQUEST')
	@allure.tag('API', 'PUT')
	@allure.severity(Severity.BLOCKER)
	@allure.parent_suite('API')
	@allure.suite('PUT')
	@allure.label('owner', 'vssuchkov')
	@allure.link('https://www.automationexercise.com', name='Testing API')
	def test_without_update_params(self, api_application, create_user, update_user_params, create_user_account):
		with step(f'Оставляем обязательные параметры для идентификации пользователя'):
			for key in update_user_params.copy().keys():
				if key in ['email', 'password']:
					continue
				update_user_params.pop(key)

		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 200)

		with step(f'Выполняем запрос get на получение информации о пользователе'):
			account_info = api_application.get.user_account_detail_by_email(create_user.email)

		with step('Проверяем неизменность информации о пользователе'):
			check_response_message_content(account_info, create_user.info)
