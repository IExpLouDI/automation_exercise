import requests
from src.automation_exercise.data.user import User


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
