import pytest
from allure import step
from automation_exercise.utils.base_test_request import BaseTestRequests
from automation_exercise.utils.check_functions import check_response_message_content


class TestAllBrandList(BaseTestRequests):

	@pytest.mark.xfail(reason='Метод находится в разработке')
	def test_valid_status_code(self, api_application):
		response_info = api_application.put.all_brand_list()
		self.check_response_status_and_message_business_code(response_info, 200, 200)


class TestUpdateUserAccount(BaseTestRequests):

	def test_valid_status_code(self, api_application, create_user, update_user_params, create_account):
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)
		self.check_response_status_and_message_business_code(response_info, 200, 200)

	def test_verify_response_message(self, api_application, create_user, update_user_params, create_account):
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 200)

		with step('Проверка текста сообщения успешного обновления = User updated!'):
			assert response_info.get('response').get(
					'message') == 'User updated!'

	def test_check_user_after_update(self, api_application, create_user, update_user_params, create_account):
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 200)

		with step(f'Выполняем запрос get на получение информации о пользователе'):
			account_info = api_application.get.user_account_detail_by_email(create_user.email)

		with step('Проверяем изменённые параметры пользователя'):
			check_response_message_content(account_info, update_user_params)

	def test_update_without_email(self, api_application, create_user, update_user_params, create_account):
		update_user_params.pop('email')
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 400)

		with step('Проверка текста бизнес ошибки = Bad request, email parameter is missing in PUT request.'):
			assert response_info.get('response').get(
					'message') == 'Bad request, email parameter is missing in PUT request.'

	def test_update_without_password(self, api_application, create_user, update_user_params, create_account):
		update_user_params.pop('password')
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 400)

		with step('Проверка текста бизнес ошибки = Bad request, password parameter is missing in PUT request.'):
			assert response_info.get('response').get(
					'message') == 'Bad request, password parameter is missing in PUT request.'

	def test_with_not_exist_email(self, api_application, update_user_params):
		with step(f'Выполняем запрос'):
			response_info = api_application.put.update_user_account(update_user_params)

		self.check_response_status_and_message_business_code(response_info, 200, 404)

		with step('Проверка текста бизнес ошибки = Account not found!'):
			assert response_info.get('response').get(
				'message') == 'Account not found!'

	def test_without_update_params(self, api_application, create_user, update_user_params, create_account):
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
