from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.locators import collections_eco_friendly_locators as loc
from time import sleep


class CollectionsEcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    # Добавление первого товара для сравнения
    def add_to_first_compare(self):
        first_element = self.find(loc.first_element_loc)
        button_add_to_compare = self.find(loc.button_add_to_compair_loc)
        ActionChains(self.driver).move_to_element(first_element).click(button_add_to_compare).perform()

    # Переход к подвкладке Shorts во вкладке Men
    def element_men_bottom_shorts(self):
        element_men = self.wait_for_element(locator=loc.men_loc,
                                            condition=EC.visibility_of_element_located,
                                            timeout=None)
        element_men_bottoms = self.find(loc.men_bottoms_loc)
        element_men_bottoms_shorts = self.find(loc.men_bottoms_shorts_loc)
        self.actions.move_to_element(element_men)
        sleep(2)
        self.actions.move_to_element(element_men_bottoms)
        sleep(2)
        self.actions.click(element_men_bottoms_shorts)
        self.actions.perform()
