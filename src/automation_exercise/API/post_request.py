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

    def create_account(self, user_info: Dict[str, any]) -> Dict[str, any]:
        payload = {}

        # Обработка поля gender
        if 'gender' in user_info and user_info['gender']:
            payload['title'] = 'Mr' if user_info['gender'].lower() == 'male' else 'Mrs'

        # Маппинг полей из user_info в payload
        field_mapping = {
            'nick_name': 'name',
            'password': 'password',
            'email': 'email',
            'day': 'birth_date',
            'month': 'birth_month',
            'year': 'birth_year',
            'first_name': 'firstname',
            'last_name': 'lastname',
            'company_name': 'company',
            'first_address': 'address1',
            'second_address': 'address2',
            'country': 'country',
            'state': 'state',
            'city': 'city',
            'zipcode': 'zipcode',
            'mobile_number': 'mobile_number'
        }

        # Добавляем поля в payload, если они существуют в user_info
        for user_attr, payload_key in field_mapping.items():
            if user_attr in user_info and user_info[user_attr] is not None:
                payload[payload_key] = user_info[user_attr]

        # Обработка флагов (со значениями по умолчанию, если не указаны)
        payload['newsletter'] = '1' if user_info.get('want_newslater', True) else '0'
        payload['optin'] = '1' if user_info.get('want_special_offer', True) else '0'

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
