from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc
from selenium.webdriver.common.keys import Keys


class SalePage(BasePage):
    page_url = '/sale.html'

    # Добавление товара в корзину и открытие корзины
    def adding_product_to_cart(self):
        self.find(loc.button_shop_women_deals_loc).click()

        self.scroll(loc.sixth_product_loc)

        element_sixth_product = self.find(loc.sixth_product_loc)
        element_sixth_product_size = self.find(loc.sixth_product_size_loc)
        element_sixth_product_color = self.find(loc.sixth_product_color_loc)
        element_sixth_product_button = self.find(loc.sixth_product_button_loc)

        self.actions.move_to_element(element_sixth_product)
        self.actions.click(element_sixth_product_size)
        self.actions.click(element_sixth_product_color)
        self.actions.click(element_sixth_product_button)
        self.actions.perform()

        self.scroll(loc.basket_loc)

        self.wait_for_element_not_to_have_text_in_attribute(locator=loc.basket_loc, attribute='class', text='loading')
        self.find(loc.button_basket_loc).click()

    # Проверка текста в пустой корзине
    def text_in_empty_basket(self):
        self.find(loc.button_basket_ff_loc).click()

    # Открытие ссылки Pants в новой вкладке и проверка текста
    def open_link_pants_new_tab(self):
        link_pants = self.find(loc.pants_link_loc)
        self.actions.key_down(Keys.CONTROL).click(link_pants).key_up(Keys.CONTROL).perform()
        self.switch_to_new_tab()
