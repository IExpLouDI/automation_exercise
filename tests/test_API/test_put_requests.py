import pytest

from automation_exercise.utils.base_test_request import BaseTestRequests


class TestAllBrandList(BaseTestRequests):

	@pytest.mark.xfail(reason='Метод находится в разработке')
	def test_valid_status_code(self, api_application):
		response_info = api_application.put.all_brand_list()

		self.check_response_status_and_message_business_code(response_info, 200, 405)