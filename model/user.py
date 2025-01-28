from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    birth_date: date
    subjects: List[str]
    hobbies: List[str]
    picture: str
    address: str
    state: str
    city: str
