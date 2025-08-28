from typing import Dict

import requests

from src.automation_exercise.API.automation_exercise_api import AutomationExerciseAPI
from src.automation_exercise.data.user import User


class PostRequest(AutomationExerciseAPI):
    METHOD_NAME = 'POST'


    def product_list(self):
        """Method is not supported."""
        return self._make_request(self.METHOD_NAME, 'productsList')

    def search_product(self, payload:Dict[str, any]) -> Dict[str, any]:
        return self._make_request(self.METHOD_NAME, 'searchProduct', data=payload)

    def verify_login(self, payload:Dict[str, any]) -> Dict[str, any]:
        return  self._make_request(self.METHOD_NAME, 'verifyLogin', data=payload)

    def create_account(self, user_info:User) -> Dict[str, any]:
        map_gender = 'Mr' if user_info.gender.lower() == 'male' else 'Mrs'

        payload = {
            'title': map_gender,
            'name': user_info.nick_name,
            'password': user_info.password,
            'birth_date': user_info.day,
            'birth_month': user_info.month,
            'birth_year': user_info.year,
            'newsletter': '1',
            'optin': '1',
            'firstname': user_info.first_name,
            'lastname': user_info.last_name,
            'company': user_info.company_name,
            'address1': user_info.first_address,
            'address2': user_info.second_address,
            'country': user_info.country,
            'state': user_info.state,
            'city': user_info.city,
            'zipcode': user_info.zipcode,
            'mobile_number': user_info.mobile_number,
            'email': user_info.email
        }

        return self._make_request("POST", "createAccount", data=payload)

def post_create_account(user_info:User):
    url = "https://automationexercise.com/api/createAccount"

    map_gender = 'Mr' if user_info.gender == 'male' else 'Mrs'

    payload = (f'title={map_gender}&'
             f'name={user_info.nick_name}&'
             f'password={user_info.password}&'
             f'birth_date={user_info.day}&'
             f'birth_month={user_info.month}&'
             f'birth_year={user_info.year}&'
             f'newsletter=1&'
             f'optin=1&'
             f'firstname={user_info.first_name}&'
             f'lastname={user_info.last_name}&'
             f'company={user_info.company_name}&'
             f'address1={user_info.first_address}&'
             f'address2={user_info.second_address}&'
             f'country={user_info.country}&'
             f'state={user_info.state}&'
             f'city={user_info.city}&'
             f'zipcode={user_info.zipcode}&'
             f'mobile_number={user_info.mobile_number}&'
             f'email={user_info.email}')

    headers = {
        'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 201:
        return {'email': user_info.email,
                'password': user_info.password,
                'nick_name': user_info.nick_name,
                'status': 'create'
                }

    return {'email': user_info.email,
            'password': user_info.password,
            'nick_name': user_info.nick_name,
            'status': 'exists'
            }
