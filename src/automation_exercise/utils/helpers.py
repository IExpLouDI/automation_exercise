def switch_req_key_to_resp_key(key_name):
    """Мапинг ключа из запроса, на ключ из ответа"""
    switch_key = {
        'firstname': 'first_name',
        'lastname': 'last_name'
    }
    return switch_key.get(key_name, key_name)
