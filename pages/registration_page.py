from selene import browser, have
from selene.support.shared.jquery_style import s


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def remove_banners(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

    def fill_name(self, first_name, last_name):
        s('#firstName').type(first_name)
        s('#lastName').type(last_name)
        return self

    def fill_email(self, email):
        s('#userEmail').type(email)
        return self

    def select_gender(self, gender):
        s(f'[for="gender-radio-{gender}"]').click()
        return self

    def fill_phone(self, phone):
        s('#userNumber').type(phone)
        return self

    def select_date_of_birth(self, day, month, year):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').click().s(f'[value="{month - 1}"]').click()
        s('.react-datepicker__year-select').click().s(f'[value="{year}"]').click()
        s(f'.react-datepicker__day--{day:03d}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subjects(self, subjects):
        for subject in subjects:
            s('#subjectsInput').type(subject).press_enter()
        return self

    def select_hobbies(self, hobbies):
        for hobby in hobbies:
            s(f'[for="hobbies-checkbox-{hobby}"]').click()
        return self

    def upload_picture(self, file_path):
        s('#uploadPicture').send_keys(file_path)
        return self

    def fill_address(self, address, state, city):
        s('#currentAddress').type(address)
        s('#state').click().s(f'#react-select-3-option-0').click()
        s('#city').click().s(f'#react-select-4-option-0').click()
        return self

    def submit(self):
        s('#submit').click()
        return self

    def should_have_registered(self, user):
        result_table = s('.table-responsive')
        result_table.should(have.text(user.first_name))
        result_table.should(have.text(user.last_name))
        result_table.should(have.text(user.email))
        result_table.should(have.text(user.gender))
        result_table.should(have.text(user.phone))
        # Преобразование даты в нужный формат
        result_table.should(have.text(user.birth_date.strftime('%d %B,%Y')))
        result_table.should(have.text(', '.join(user.subjects)))
        result_table.should(have.text(', '.join(user.hobbies)))
        result_table.should(have.text(user.picture))
        result_table.should(have.text(user.address))
        result_table.should(have.text(f'{user.state} {user.city}'))
