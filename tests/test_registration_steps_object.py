import os
from datetime import date

from model.user import User
from pages.registration_page import RegistrationPage


def test_form_submission():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(current_dir, '..', 'resources', 'pic.png'))

    assert os.path.exists(file_path), f"File not found at path: {file_path}"

    user = User(
        first_name='Sonic',
        last_name='Syndicate',
        email='test@mail.ru',
        gender='Male',
        phone='9939993388',
        birth_date=date(1960, 3, 3),
        subjects=['Maths'],
        hobbies=['Sports', 'Music'],
        picture='pic.png',
        address='Moscow 5',
        state='NCR',
        city='Delhi'
    )

    registration_page = RegistrationPage()
    registration_page.open() \
        .remove_banners() \
        .fill_name(user.first_name, user.last_name) \
        .fill_email(user.email) \
        .select_gender(1) \
        .fill_phone(user.phone) \
        .select_date_of_birth(user.birth_date.day, user.birth_date.month, user.birth_date.year) \
        .fill_subjects(user.subjects) \
        .select_hobbies([1, 3]) \
        .upload_picture(file_path) \
        .fill_address(user.address, user.state, user.city) \
        .submit()

    registration_page.should_have_registered(user)
