import re


def camel_to_snake_case(key_name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', key_name).lower()
