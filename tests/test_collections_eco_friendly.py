import pytest
import allure
from pages.locators import collections_eco_friendly_locators as loc


@allure.feature('Add the first item to compare')
@allure.story('Add to compare')
@allure.title('Добавление первого товара для сравнения')
@allure.description('Данный тест выполняет добавление первого товара для сравнения')
@pytest.mark.smoke
def test_add_the_first_compare(collections_eco_friendly_page):

    # Открытие страницы в браузере
    collections_eco_friendly_page.open_page()

    # Добавление первого товара для сравнения
    collections_eco_friendly_page.add_to_first_compare()

    # Сравниваем текст первого товара и товара в списке сравнения
    collections_eco_friendly_page.compare_element_texts(
        element_loc1=loc.first_element_loc,
        element_loc2=loc.compare_product_loc
    )
