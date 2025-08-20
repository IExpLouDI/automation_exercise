from dataclasses import dataclass
from src.automation_exercise.utils.static_values import Country, Months


@dataclass
class Person:
    first_name: str
    last_name: str
    gender: str
    day: str
    month: Months
    year: str
    country: Country
    city: str
    state: str
    first_address: str
    zipcode: str
    mobile_number: str
    second_address: str


@dataclass
class User(Person):
    nick_name: str
    password: str
    email: str
    company_name: str = None
    want_newslater: bool = True
    want_special_offer: bool = True
    __name_card: str = None
    __card_number: str = None
    __cvc: str = None
    __expiration_month: str = None
    __expiration_year: str = None

    @property
    def get_user_param(self):
        user_gender = 'Mr.' if self.gender == 'male' else 'Mrs.'
        params_list = [
            f'{user_gender} {self.first_name} {self.last_name}',
            self.company_name,
            self.first_address,
            self.second_address,
            f'{self.city} {self.state} {self.zipcode}',
            self.country.value,
            self.mobile_number
        ]

        return params_list

    def add_user_card(self, card_name, card_number, cvc_code, expiration_month, expiration_year):
        self.__cvc = cvc_code
        self.__name_card = card_name
        self.__card_number = card_number
        self.__expiration_month = expiration_month
        self.__expiration_year = expiration_year