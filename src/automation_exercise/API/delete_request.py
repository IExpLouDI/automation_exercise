from typing import Dict

import requests

from src.automation_exercise.API.automation_exercise_api import AutomationExerciseAPI


class DeleteRequest(AutomationExerciseAPI):
    METHOD_NAME = "DELETE"

    def user_account(self, payload:Dict[str, any]) -> Dict[str, any]:

        return self._make_request(self.METHOD_NAME, 'deleteAccount', data=payload)

    def verify_login(self):
        return self._make_request(self.METHOD_NAME, 'verifyLogin')


def delete_account(user_email, user_password) -> Dict[str, any]:
    api_url = "https://automationexercise.com/api/deleteAccount"

    payload = (f'email={user_email}&'
               f'password={user_password}')

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("DELETE", api_url, headers=headers, data=payload)

    if response.status_code == 200:
        return True

    return False
