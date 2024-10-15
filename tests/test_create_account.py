import os
import pytest
import allure
import dotenv
from faker import Faker
from pages.create_account import CreateAccount as CA

# Создаем объект Faker
fake = Faker()

# Используем dotenv
dotenv.load_dotenv()


@allure.feature('Create account')
@allure.story('Create New Customer Account')
@allure.title('Создание аккаунта')
@allure.description('Данный тест выполняет создание аккаунта с заполнением всех полей валидными данными')
@pytest.mark.smoke
def test_correct_create_account(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_customer_form(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=os.getenv('PASSWORD'),
        confirm_password=os.getenv('PASSWORD')
    )
    create_account_page.check_create_alert_text_is(
        'Thank you for registering with Main Website Store.'
    )


@allure.feature('Create account')
@allure.story('Create New Customer Account - Negative Tests')
@allure.title('Негативные тесты для создания аккаунта')
@allure.description('Этот тест проверяет создание аккаунта при отсутствии обязательных полей')
@pytest.mark.smoke
@pytest.mark.parametrize(
    "field, first_name, last_name, email, password, confirm_password, error_message", CA.get_negative_test_data())
def test_create_account_missing_fields(create_account_page, field, first_name,
                                       last_name, email, password, confirm_password, error_message):

    # Открытие страницы в браузере
    create_account_page.open_page()

    # Заполнение формы, где одно поле пропущено
    create_account_page.fill_customer_form(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        confirm_password=confirm_password
    )

    # Проверяем, что сообщение об ошибке отображается для конкретного поля
    create_account_page.check_field_error_is_displayed(field, error_message)
