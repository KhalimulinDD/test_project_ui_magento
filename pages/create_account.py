from utils import project_ec
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from selenium.webdriver.support.wait import WebDriverWait


class CreateAccount(BasePage):
    page_url = '/customer/account/create'

    def fill_customer_form(self, first_name, last_name, email, password):

        # Поиск элементов анкеты создания
        first_name_field = self.find(loc.first_name_field_loc)
        last_name_field = self.find(loc.last_name_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        confirm_password_field = self.find(loc.confirm_password_field_loc)
        button = self.find(loc.button_loc)

        # Указание данных в поля
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        button.click()

    def check_create_alert_text_is(self, text):
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(loc.create_locator))

        create_alert = self.driver.find_element(*loc.create_locator)
        assert create_alert.text == text
