import allure
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import collections_eco_friendly_locators as loc


class CollectionsEcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def __init__(self, driver: WebDriver, timeout: int = 10):
        super().__init__(driver, timeout)  # Наследование от родительского класса
        self.text_button_shorts_text = None

    @allure.step('Adding the first product for comparison')
    def add_to_first_compare(self):
        first_element = self.find(loc.first_element_loc)
        button_add_to_compare = self.find(loc.button_add_to_compair_loc)
        self.actions.move_to_element(first_element).click(button_add_to_compare).perform()

    # Свойство для получения элемента первого товара
    @property
    def first_product(self):
        self.wait_for_element(loc.first_element_loc, EC.visibility_of_element_located)
        return self.find(loc.first_element_loc)

    # Свойство для получения элемента товара в сравнении
    @property
    def product_in_comparison(self):
        self.wait_for_element(loc.compare_product_loc, EC.visibility_of_element_located)
        return self.find(loc.compare_product_loc)

    @allure.step('Go to the Shorts subtab in the Men tab')
    def click_the_button_and_search_for_the_element_shorts(self):
        element_men = self.wait_for_element(locator=loc.men_loc, condition=EC.visibility_of_element_located)
        element_men_bottoms = self.find(loc.men_bottoms_loc)
        element_men_bottoms_shorts = self.find(loc.men_bottoms_shorts_loc)

        self.text_button_shorts_text = self.text_extraction(loc.men_bottoms_shorts_loc)

        self.actions.move_to_element(element_men)
        self.actions.move_to_element(element_men_bottoms)
        self.actions.click(element_men_bottoms_shorts)
        self.actions.perform()

    # Свойство для передачи текста нажатой кнопки
    @property
    def text_button_shorts(self):
        return self.text_button_shorts_text

    # Свойство для получения элемента Shorts на новой открытой странице
    @property
    def text_shorts_is_open_page(self):
        self.wait_for_element(loc.text_shorts_loc, EC.visibility_of_element_located)
        return self.find(loc.text_shorts_loc)

    @allure.step('Search and click to sort in ascending order')
    def sort_by_price(self):
        self.select_by_value(select_locator=loc.sort_by_loc, value_locator=loc.sort_by_price_loc)

    # Свойство для получения всех цен на странице
    @property
    def text_price(self):
        self.wait_for_element(loc.sorted_goods_price_loc, EC.visibility_of_element_located)
        return self.find_all(loc.sorted_goods_price_loc)
