from typing import Dict


def switch_req_key_to_resp_key(key_name):
    """Мапинг ключа из запроса, на ключ из ответа"""
    switch_key = {
        'firstname': 'first_name',
        'lastname': 'last_name'
    }
    return switch_key.get(key_name, key_name)


def switch_resp_key_to_req_key(key_name):
    """Мапинг ключа из запроса, на ключ из ответа"""
    switch_key = {
        'first_name': 'firstname',
        'last_name': 'lastname',
        'nick_name': 'name',
        'first_address': 'address1'
    }
    return switch_key.get(key_name, key_name)


def switch_search_param_case(payload:Dict[str, str])->Dict[str, str]:
    param = payload.get('search_product')
    if param[0].islower():
        payload.update({'search_product': param.upper()})
    else:
        payload.update({'search_product': param.lower()})

    return payload
