from enum import Enum


class Country(Enum):
    singapore = 'Singapore'
    us = 'United States'
    canada = 'Canada'
    australia = 'Australia'
    israel = 'Israel'
    new_zealand = 'New Zealand'
    india = 'India'


class Months(Enum):
    january = '1',
    february = '2',
    march = '3',
    april = '4',
    may = '5',
    june = '6',
    july = '7',
    august = '8',
    september = '9',
    october = '10',
    november = '11',
    december = '12'


class StatusMessage(Enum):
    get_account_not_found = 'Account not found with this email, try another email!'
    put_user_update = 'User updated!'
    put_account_not_found = 'Account not found!'
    del_account_deleted = 'Account deleted!'
    user_not_found = 'User not found!'
    post_missing_search_param = 'Bad request, search_product parameter is missing in POST request.'
    post_verify_user_exists = 'User exists!'
    post_bad_request = 'Bad request, email or password parameter is missing in POST request.'
    email_exists = 'Email already exists!'
    post_user_created = 'User created!'

    @classmethod
    def bad_request_missing_email(cls, method:str) -> str:
        return f'Bad request, email parameter is missing in {method.upper()} request.'

    @classmethod
    def bad_request_missing_password(cls, method:str) -> str:
        return f'Bad request, password parameter is missing in {method.upper()} request.'
