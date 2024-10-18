from selenium.webdriver.common.by import By

first_name_field_loc = (By.ID, 'firstname')
last_name_field_loc = (By.ID, 'lastname')
email_field_loc = (By.ID, 'email_address')
password_field_loc = (By.ID, 'password')
confirm_password_field_loc = (By.ID, 'password-confirmation')
button_loc = (By.CSS_SELECTOR, '[title="Create an Account"]')
create_locator = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
first_name_error_loc = (By.ID, 'firstname-error')
last_name_error_loc = (By.ID, 'lastname-error')
email_error_loc = (By.ID, 'email_address-error')
password_error_loc = (By.ID, 'password-error')
confirm_password_error_loc = (By.ID, 'password-confirmation-error')
