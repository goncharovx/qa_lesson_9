from pages.registration_page import RegistrationPage
import os


def test_form_submission_with_page_object():
    registration_page = RegistrationPage()

    current_dir = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(current_dir, '..', 'resources', 'pic.png'))

    registration_page.open() \
        .fill_first_name('Sonic') \
        .fill_last_name('Syndicate') \
        .fill_email('test@mail.ru') \
        .select_gender_male() \
        .fill_phone_number('9939993388') \
        .set_date_of_birth('2', '1960', '03') \
        .add_subject('Maths') \
        .select_hobbies(sports=True, music=True) \
        .upload_file(file_path) \
        .fill_address('Moscow 5') \
        .select_state_and_city('NCR', 'Delhi') \
        .submit() \
        .should_have_registered(
        'Sonic Syndicate',
        'test@mail.ru',
        'Male',
        '9939993388',
        '03 March,1960',
        'Maths',
        'Sports',
        'Music',
        'pic.png',
        'Moscow 5',
        'NCR Delhi'
    )