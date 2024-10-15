import pytest
from time import sleep
from selenium import webdriver
from pages.create_account import CreateAccount
from selenium.webdriver.chrome.options import Options

options = Options()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def driver():
    """Фикстура для открытия браузера  с опциями"""
    options.add_argument('start-maximized')
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome(options=options)
    sleep(3)
    return chrome_driver
