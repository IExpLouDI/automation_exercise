from typing import Dict

from src.automation_exercise.API.automation_exercise_api import AutomationExerciseAPI


class PutRequest(AutomationExerciseAPI):
    METHOD_NAME = "PUT"

    def put_all_brand_list(self) -> Dict[str, any]:
        """Method is not supported"""
        return self._make_request(self.METHOD_NAME, 'brandsList')

    def put_update_user_account(self, update_fields:Dict[str, any]) -> Dict[str, any]:
        payload = update_fields.copy()

        return self._make_request(self.METHOD_NAME, 'updateAccount', data=payload)
