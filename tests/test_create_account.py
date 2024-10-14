import pytest
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.mark.smoke
def test_correct_create_account(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_customer_form(
        first_name=os.getenv('FIRST_NAME'),
        last_name=os.getenv('LAST_NAME'),
        email=os.getenv('EMAIL'),
        password=os.getenv('PASSWORD')
    )
    create_account_page.check_create_alert_text_is(
        'Thank you for registering with Main Website Store.'
    )
