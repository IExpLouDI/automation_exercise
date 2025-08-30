from json import JSONDecodeError
from typing import Optional, Dict
import requests


class AutomationExerciseAPI:
    BASE_URL = 'https://automationexercise.com/api'

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        )

    def _make_request(self, method: str, end_point:str, data: Optional[Dict[str, any]] = None) -> dict:
        url = f'{self.BASE_URL}/{end_point}'

        try:
            response = self.session.request(method, url, data=data)

            try:
               return {'response': response.json(),
                       'status_code': response.status_code
                       }

            except JSONDecodeError:
                return {'response': response.text,
                        'status_code': response.status_code
                        }

        except requests.exceptions.RequestException as err:
            response = getattr(err, 'response', None)
            return {'response': str(err),
                    'status_code': getattr(response, 'status_code', None)
                    }
