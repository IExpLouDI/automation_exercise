from typing import Dict

from src.automation_exercise.API.automation_exercise_api import AutomationExerciseAPI


class GetRequests(AutomationExerciseAPI):
    METHOD_NAME = "GET"

    def all_product(self) -> Dict[str, any]:
        return self._make_request(self.METHOD_NAME, 'productsList')

    def all_brand_list(self) -> Dict[str, any]:
        return self._make_request(self.METHOD_NAME, 'brandsList')

    def user_account_detail_by_email(self, user_email:str) -> Dict[str, any]:
        return self._make_request(self.METHOD_NAME, f'getUserDetailByEmail?email={user_email}')
