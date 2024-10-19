from utils import project_ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver, timeout: int = 10):
        """Инициализация драйвера и ActionChains"""
        self.driver = driver
        self.timeout = timeout
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, timeout)

    def open_page(self):
        """Метод для открытия страницы"""
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple):
        """Метод использования одного элемента"""
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        """Метод использования нескольких элементов"""
        return self.driver.find_elements(*locator)

    def scroll(self, locator: tuple):
        """Метод скроллинга до нужного элемента и возвращения этого элемента"""
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def text_extraction(self, locator: tuple):
        """Метод для извлечения текста из элемента, найденного по локатору"""
        element = self.find(locator)
        text = self.driver.execute_script("return arguments[0].textContent;", element)
        return text.strip()

    # def compare_element_texts(self, text_element_loc1: tuple[str, str], text_element_loc2: tuple[str, str]):
    #     """Сравнение текста двух элементов с возможным ожиданием появления"""
    #     # Ожидание появления элементов
    #     text_element1 = self.wait_for_element(text_element_loc1, EC.visibility_of_element_located)
    #     text_element2 = self.wait_for_element(text_element_loc2, EC.visibility_of_element_located)
    #
    #     # Извлекаем тексты и выполняем проверку
    #     element1_text = text_element1.text.strip()
    #     element2_text = text_element2.text.strip()
    #
    #     assert element1_text == element2_text

    @staticmethod
    def compare_element_texts(element_1, element_2):
        """Сравнение текста двух уже найденных элементов или строк"""

        # Если элемент передан как WebElement, извлекаем текст, иначе используем текст напрямую
        element_1_text = element_1.text if hasattr(element_1, 'text') else element_1
        element_2_text = element_2.text if hasattr(element_2, 'text') else element_2

        print(f'Первый элемент: {element_1_text}')
        print(f'Второй элемент: {element_2_text}')

        # Сравнение текстов
        assert element_1_text == element_2_text

    def wait_for_element(self, locator: tuple[str, str], condition: EC):
        """Метод явного ожидания элемента"""
        return self.wait.until(condition(locator))

    def wait_for_element_not_to_have_text_in_attribute(self, locator: tuple[str, str], attribute: str, text: str):
        """Метод ожидания, пока атрибут элемента не будет содержать текст"""
        by, value = locator

        return self.wait.until_not(
            EC.text_to_be_present_in_element_attribute((by, value), attribute, text)
        )

    # def check_create_alert_text_is(self, locator: tuple, expected_text: str):
    #     """Метод для проверки текста элемента на странице"""
    #
    #     # Явное ожидание, пока текст элемента не станет непустым
    #     self.wait.until(project_ec.text_is_not_empty_in_element(locator))
    #
    #     # Поиск элемента по переданному локатору
    #     element = self.driver.find_element(*locator)
    #
    #     # Проверка, что текст элемента соответствует ожидаемому
    #     actual_text = element.text.strip()
    #     assert actual_text == expected_text

    def select_by_value(self, select_locator: tuple, value_locator: tuple):
        """Метод для выбора элемента из выпадающего списка с использованием локаторов"""

        # Находим элемент select по локатору (кортежу)
        select_element = self.find(select_locator)

        # Инициализируем объект Select
        dropdown = Select(select_element)

        # Находим элемент, который нужно выбрать по переданному локатору для значения
        value_element = self.find(value_locator)

        # Получаем значение атрибута 'value' элемента
        value = value_element.get_attribute("value")

        # Выбираем элемент в select по значению
        dropdown.select_by_value(value)

    # def check_prices_sorted_ascending(self, price_locator: tuple):
    #     """Метод для проверки, что цены товаров отсортированы по возрастанию"""
    #
    #     # Находим все элементы с ценами
    #     price_elements = self.find_all(price_locator)
    #
    #     # Извлекаем текст цены и преобразуем его в числа (предположим, цены с символом валюты)
    #     prices = []
    #     for price_element in price_elements:
    #         # Убираем символы валюты и лишние пробелы, преобразуем в float
    #         price_text = price_element.text.replace('$', '').replace(',', '').strip()
    #         prices.append(float(price_text))
    #
    #     # Проверяем, что список цен отсортирован по возрастанию
    #     assert prices == sorted(prices)

    @staticmethod
    def check_prices_sorted_ascending(price_elements):
        """Метод для проверки, что цены товаров отсортированы по возрастанию"""

        prices = []
        for price_element in price_elements:
            # Убираем символы валюты и лишние пробелы, преобразуем в float
            price_text = price_element.text.replace('$', '').replace(',', '').strip()
            prices.append(float(price_text))
            print(prices)

        # Проверяем, что список цен отсортирован по возрастанию
        assert prices == sorted(prices)

    def switch_to_new_tab(self):
        """Метод для переключения на новую вкладку"""
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
