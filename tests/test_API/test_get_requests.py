from automation_exercise.utils.check_functions import validate_response_schema, check_response_content, \
    check_response_status_and_message_business_code
from allure import step


def test_get_all_product_valid_shema(api_application, load_schema):
    response_info = api_application.get.get_all_product()
    validate_response_schema(load_schema['get_all_product_list'], response_info.get('response'))


def test_get_all_product_valid_status_code(api_application):
    response_info = api_application.get.get_all_product()

    check_response_status_and_message_business_code(response_info, 200, 200)


def test_get_all_brand_list_valid_shema(api_application, load_schema):
    response_info = api_application.get.get_all_brand_list()
    validate_response_schema(load_schema['get_brands_list'], response_info.get('response'))


def test_get_all_brand_list_valid_status_code(api_application):
    response_info = api_application.get.get_all_brand_list()

    check_response_status_and_message_business_code(response_info, 200, 200)


def test_get_user_account_detail_valid_schema(api_application, load_schema, create_user, create_account):
    response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
    validate_response_schema(load_schema['get_user_account_detail'], response_info.get('response'))


def test_get_user_account_detail_valid_status_code(api_application, create_user, create_account):
    response_info = api_application.get.get_user_account_detail_by_email(create_user.email)
    check_response_status_and_message_business_code(response_info, 200, 200)
    # with step(f'Проверка статуса ответа = 200'):
    #     assert response_info.get('response') == 200
    # with step(f'Проверка бизнес кода ответа = 200'):
    #     assert response_info.get('response').get('responseCode') == 200


def test_get_user_account_detail_with_not_exist_email(api_application, create_user):
    response_info = api_application.get.get_user_account_detail_by_email(create_user.email)

    check_response_status_and_message_business_code(response_info, 200, 404)
    # with step(f'Проверка статуса ответа = 200'):
    #     assert response_info.get('status_code') == 200
    # with step(f'Проверка бизнес кода ошибки = 404'):
    #     assert response_info.get('response').get('responseCode') == 404

    with step('Проверка текста бизнес ошибки = Account not found with this email, try another email!'):
        assert response_info.get('response').get('message') == 'Account not found with this email, try another email!'


def test_get_user_account_detail_with_check_content(api_application, create_user, create_account):
    response_info = api_application.get.get_user_account_detail_by_email(create_user.email)

    check_response_status_and_message_business_code(response_info, 200, 200)

    with step(f'Проверка контента ответа на совпадение с данными пользователя {create_user}'):
        check_response_content(response_info.get('response'), create_user.info)
