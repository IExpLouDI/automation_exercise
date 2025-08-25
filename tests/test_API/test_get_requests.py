import json
from jsonschema import validate


def test_get_all_product_valid_shema(api_application, load_schema):
    response = api_application.get.get_all_product()
    with open(load_schema['get_all_product_list'], 'r', encoding='utf-8') as file:
        schema = json.loads(file.read())
    validate(instance=response, schema=schema)


def test_get_all_product_valid_status_code(api_application, load_schema):
    response = api_application.get.get_all_product()
    assert response['status_code'] == 200

