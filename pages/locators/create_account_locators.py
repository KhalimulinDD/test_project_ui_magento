from selenium.webdriver.common.by import By

# Поиск элементов полей создания аккаунта
first_name_field_loc = (By.ID, 'firstname')
last_name_field_loc = (By.ID, 'lastname')
email_field_loc = (By.ID, 'email_address')
password_field_loc = (By.ID, 'password')
confirm_password_field_loc = (By.ID, 'password-confirmation')
button_loc = (By.CSS_SELECTOR, '[title="Create an Account"]')

# Поиск текста успешного создания аккаунта
create_locator = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')

# Поиск текста ошибки валидации полей
first_name_error_loc = (By.ID, 'firstname-error')
last_name_error_loc = (By.ID, 'lastname-error')
email_error_loc = (By.ID, 'email_address-error')
password_error_loc = (By.ID, 'password-error')
confirm_password_error_loc = (By.ID, 'password-confirmation-error')
