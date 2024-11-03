import pytest
from selenium import webdriver
from pages.sale_page import SalePage
from pages.create_account_page import CreateAccount
from pages.collections_eco_friendly_page import CollectionsEcoFriendly
from selenium.webdriver.chrome.options import Options

options = Options()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def collections_eco_friendly_page(driver):
    return CollectionsEcoFriendly(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def driver():
    """Фикстура для открытия браузера  с опциями"""
    # options.add_argument('start-maximized')
    # options.add_experimental_option('detach', True)
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver
