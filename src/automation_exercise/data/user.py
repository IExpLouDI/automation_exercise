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
class UserCard:
    name: str
    number: str
    cvc: str
    expiration_month: str
    expiration_year: str

    @property
    def masked_number(self) -> str:
        return f"**** **** **** {self.number[-4:]}"

    def __repr__(self):
        return f'user - {self.name}. card - {self.masked_number}'


@dataclass
class User(Person):
    nick_name: str
    password: str
    email: str
    company_name: str = None
    want_newslater: bool = True
    want_special_offer: bool = True
    card: UserCard = None

    @property
    def short_info(self):
        user_gender = 'Mr.' if self.gender == 'male' else 'Mrs.'
        params_list = [
            f'{user_gender} {self.first_name} {self.last_name}',
            self.company_name,
            self.first_address,
            self.second_address,
            f'{self.city} {self.state} {self.zipcode}',
            self.country,
            self.mobile_number
        ]

        return params_list

    @property
    def info(self):
        user_gender = 'Mr' if self.gender == 'male' else 'Mrs'
        dict_info = {
            "name": self.nick_name,
            "email": self.email,
            "title": user_gender,
            "birth_day": self.day,
            "birth_month": self.month,
            "birth_year": self.year,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company": self.company_name,
            "address1": self.first_address,
            "address2": self.second_address,
            "country": self.country,
            "state": self.state,
            "city": self.city,
            "zipcode": self.zipcode
        }

        return dict_info

    def add_card(self, card_data: UserCard):
        self.card = card_data

    def __repr__(self):
        return f'nickname - {self.nick_name}, email - {self.email}'
