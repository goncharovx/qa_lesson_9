from pages.high_level_steps import User, RegistrationPage
from datetime import date
from pages.high_level_steps import Hobby


def test_register_student():
    # Создаем пользователя
    student = User(
        first_name='Sonic',
        last_name='Syndicate',
        email='test@mail.ru',
        gender='Male',
        phone='9939993388',
        birth_date=date(1960, 3, 3),
        subjects=['Maths'],
        hobbies=[Hobby.SPORTS, Hobby.MUSIC],
        picture_path='resources/pic.png',
        address='Moscow 5',
        state='NCR',
        city='Delhi'
    )

    # Используем high-level step objects
    registration_page = RegistrationPage()
    registration_page.open().register(student).should_have_registered(student)