import json
import os

from allure import step
from jsonschema import validate


class BaseTestRequests:

    def validate_response_schema(self,schema_path, response: dict) -> None:
        with step(f'Проверяем соответствие схеме {os.path.basename(schema_path)}'):
            with open(schema_path, 'r', encoding='utf-8') as file:
                schema = json.loads(file.read())

            validate(instance=response, schema=schema)

    def check_response_status_and_message_business_code(self,
                                                        response: dict,
                                                        wait_status_code: int,
                                                        wait_business_code: int = None) -> None:

        with step(f'Проверка статуса ответа = {wait_status_code}'):
            assert response.get('status_code') == wait_status_code

        if wait_business_code is not None:
            with step(f'Проверка бизнес кода ответа = {wait_business_code}'):
                assert response.get('response').get('responseCode') == wait_business_code
