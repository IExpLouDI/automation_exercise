from dataclasses import dataclass
from automation_exercise.utils.static_values import Country, Months


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
