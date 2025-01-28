from selene import browser, have
from selene.api import s


class RegistrationPage:

    def __init__(self):
        self.first_name = s('#firstName')
        self.last_name = s('#lastName')
        self.email = s('#userEmail')
        self.gender_male = s('[for="gender-radio-1"]')
        self.phone_number = s('#userNumber')
        self.date_of_birth_input = s('#dateOfBirthInput')
        self.month_select = s('.react-datepicker__month-select')
        self.year_select = s('.react-datepicker__year-select')
        self.subject_input = s('#subjectsInput')
        self.hobby_sports = s('[for="hobbies-checkbox-1"]')
        self.hobby_music = s('[for="hobbies-checkbox-3"]')
        self.upload_picture = s('#uploadPicture')
        self.address = s('#currentAddress')
        self.state = s('#state')
        self.city = s('#city')
        self.submit_button = s('#submit')
        self.results_table = s('.table-responsive')

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

    def fill_first_name(self, name):
        self.first_name.type(name)
        return self

    def fill_last_name(self, surname):
        self.last_name.type(surname)
        return self

    def fill_email(self, email):
        self.email.type(email)
        return self

    def select_gender_male(self):
        self.gender_male.click()
        return self

    def fill_phone_number(self, number):
        self.phone_number.type(number)
        return self

    def set_date_of_birth(self, month, year, day):
        self.date_of_birth_input.click()
        self.month_select.s(f'[value="{month}"]').click()
        self.year_select.s(f'[value="{year}"]').click()
        s(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def add_subject(self, subject):
        self.subject_input.type(subject).press_enter()
        return self

    def select_hobbies(self, sports=False, music=False):
        if sports:
            self.hobby_sports.click()
        if music:
            self.hobby_music.click()
        return self

    def upload_file(self, file_path):
        self.upload_picture.send_keys(file_path)
        return self

    def fill_address(self, address):
        self.address.type(address)
        return self

    def select_state_and_city(self, state, city):
        self.state.click().s(f'//*[text()="{state}"]').click()
        self.city.click().s(f'//*[text()="{city}"]').click()
        return self

    def submit(self):
        self.submit_button.click()
        return self

    def should_have_registered(self, *expected_values):
        for value in expected_values:
            self.results_table.should(have.text(value))
        return self
