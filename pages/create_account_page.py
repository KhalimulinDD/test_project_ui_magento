import allure
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from selenium.webdriver.support import expected_conditions as EC


class CreateAccount(BasePage):
    page_url = '/customer/account/create'

    @allure.step('Successful account registration')
    def fill_customer_form(self, first_name, last_name, email, password, confirm_password):
        """Поиск полей, подстановка данных в поля, ввод данных"""
        first_name_field = self.find(loc.first_name_field_loc)
        last_name_field = self.find(loc.last_name_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        confirm_password_field = self.find(loc.confirm_password_field_loc)
        button = self.find(loc.button_loc)

        if first_name:
            first_name_field.send_keys(first_name)
        if last_name:
            last_name_field.send_keys(last_name)
        if email:
            email_field.send_keys(email)
        if password:
            password_field.send_keys(password)
        if confirm_password:
            confirm_password_field.send_keys(confirm_password)

        button.click()

    # Свойство для получения элемента текста после создания аккаунта
    @property
    def search_text_after_account_creation(self):
        self.wait_for_element(loc.text_create_locator, EC.visibility_of_element_located)
        return self.find(loc.text_create_locator)

    # Свойство для передачи текста, который отображается после создания аккаунта
    @property
    def text_to_check_the_created_account(self):
        return 'Thank you for registering with Main Website Store.'

    @allure.step('Checking error messages for specific fields')
    def check_field_error_is_displayed(self, field, error_message):
        """Проверка сообщений об ошибке для конкретных полей"""
        if field == 'first_name':
            error_element = self.find(loc.first_name_error_loc)
        elif field == 'last_name':
            error_element = self.find(loc.last_name_error_loc)
        elif field == 'email':
            error_element = self.find(loc.email_error_loc)
        elif field == 'password':
            error_element = self.find(loc.password_error_loc)
        elif field == 'confirm_password':
            error_element = self.find(loc.confirm_password_error_loc)
        else:
            raise ValueError(f"Unknown field: {field}")

        # Проверка, что сообщение об ошибке соответствует ожидаемому
        assert error_message in error_element.text

    @staticmethod
    def get_test_data_no_required_fields():
        """Варианты заполнения полей"""

        message_error_field = 'This is a required field.'

        return [
            # Отсутствует имя
            ("first_name", None, "Doe", "john.doe@example.com",
             "Password123!", "Password123!", f"{message_error_field}"),

            # Отсутствует фамилия
            ("last_name", "John", None, "john.doe@example.com",
             "Password123!", "Password123!", f"{message_error_field}"),

            # Отсутствует email
            ("email", "John", "Doe", None, "Password123!",
             "Password123!", f"{message_error_field}"),

            # Отсутствует пароль
            ("password", "John", "Doe", "john.doe@example.com",
             None, "Password123!", f"{message_error_field}"),

            # Отсутствует повторный пароль
            ("confirm_password", "John", "Doe", "john.doe@example.com",
             'Password123!', None, f"{message_error_field}"),
        ]
