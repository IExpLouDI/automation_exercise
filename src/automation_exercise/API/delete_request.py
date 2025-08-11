import requests

def delete_account(user_email, user_password):
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
