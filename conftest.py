from selenium import webdriver
from pages.create_account import CreateAccount
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    sleep(3)
    return chrome_driver


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)
