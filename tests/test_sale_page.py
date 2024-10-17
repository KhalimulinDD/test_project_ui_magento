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