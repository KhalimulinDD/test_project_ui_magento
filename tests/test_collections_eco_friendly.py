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
        text_element_loc1=loc.first_element_loc,
        text_element_loc2=loc.compare_product_loc
    )


@allure.feature('Navigate to the Shorts subtab')
@allure.story('Man tab navigation')
@allure.title('Переход на подвкладку Shorts')
@allure.description('Данный тест выполняет переход и нажатие на подвкладку Shorts')
@pytest.mark.regression
def test_men_bottoms_shorts(collections_eco_friendly_page):

    # Открытие страницы в браузере
    collections_eco_friendly_page.open_page()

    # Поиск и нажатие на элемент Shorts
    collections_eco_friendly_page.element_men_bottom_shorts()

    # Проверка текста заголовка
    collections_eco_friendly_page.check_create_alert_text_is(locator=loc.text_shorts_loc, expected_text='Shorts')


@allure.feature('Sort by ascending order')
@allure.story('Checking the sorting of goods')
@allure.title('Сортировка товаров по возрастанию')
@allure.description('Данный тест выполняет сортировку товара по возрастанию')
@pytest.mark.regression
def test_sort_by_ascending_order(collections_eco_friendly_page):

    # Открытие страницы в браузере
    collections_eco_friendly_page.open_page()

    # Выбор сортировки по Price
    collections_eco_friendly_page.sort_by_price()

    # Проверка сортировки по возрастанию
    collections_eco_friendly_page.check_prices_sorted_ascending(price_locator=loc.sorted_goods_loc)
