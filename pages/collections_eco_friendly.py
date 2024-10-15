from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from pages.locators import collections_eco_friendly_locators as loc


class CollectionsEcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    # Добавление товара для сравнения
    def add_to_first_compare(self):
        """Поиск элементов, наведение на элемент и нажатие кнопки"""
        first_element = self.find(loc.first_element_loc)
        button_add_to_compare = self.find(loc.button_add_to_compair_loc)
        ActionChains(self.driver).move_to_element(first_element).click(button_add_to_compare).perform()
