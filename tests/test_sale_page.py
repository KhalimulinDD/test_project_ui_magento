import pytest
import allure
from pages.locators import sale_page_locators as loc


@allure.feature('Adding a product to the cart')
@allure.story('Adding a product')
@allure.title('Добавление товара в корзину')
@allure.description('Этот тест добавляет товар в корзину и проверяет что товар добавлен')
@pytest.mark.smoke
def test_adding_a_product_to_the_cart(sale_page):

    # Открытие страницы в браузере
    sale_page.open_page()

    # Добавление и открытие корзины
    sale_page.adding_product_to_cart()

    # Сравниваем текст выбранного товара и товара в корзине
    sale_page.compare_element_texts(
        text_element_loc1=loc.sixth_product_loc,
        text_element_loc2=loc.text_product_in_basket_loc
    )


@allure.feature('Checking if the cart is empty')
@allure.story('Checking the basket')
@allure.title('Проверка пустой корзины')
@allure.description('Этот тест проверяет отображение соответствующего текста в пустой корзине')
@pytest.mark.regression
def test_checking_if_the_cart_is_empty(sale_page):

    # Открытие страницы в браузере
    sale_page.open_page()

    # Добавление и открытие корзины
    sale_page.text_in_empty_basket()

    # Проверка соответствующего текста в пустой корзине
    sale_page.check_create_alert_text_is(
        locator=loc.empty_basket_text_loc,
        expected_text='You have no items in your shopping cart.'
    )


@allure.feature('Open link pants in new tab')
@allure.story('Open link')
@allure.title('Открытие ссылки Pants в новой вкладке')
@allure.description(
    'Этот тест проверяет открытие ссылки Pants в новой вкладке, переход на новую вкладку и проверку текста'
)
@pytest.mark.regression
def test_open_link_pants(sale_page):

    # Открытие страницы в браузере
    sale_page.open_page()

    # Открытие ссылки в новой вкладке
    sale_page.open_link_pants_new_tab()

    # Проверка соответствующего текста на новой вкладке
    sale_page.check_create_alert_text_is(
        locator=loc.pants_text_new_tab_loc,
        expected_text='Pants'
    )