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

    def open_page(self):
        """Метод для открытия страницы"""
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    # Метод использования одного найденного элемента
    def find(self, locator: tuple):
        """Метод использования одного элемента"""
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        """Метод использования нескольких элементов"""
        return self.driver.find_elements(*locator)

    def scroll(self, locator: tuple):
        """Метод скроллинга до нужного элемента"""
        element = self.find(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def compare_element_texts(self, element_loc1: tuple[str, str], element_loc2: tuple[str, str]):
        """Сравнение текста двух элементов с возможным ожиданием появления"""
        # Ожидание появления элементов
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_loc1))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_loc2))

        # Извлекаем тексты и выполняем проверку
        element1 = self.find(element_loc1)
        element1_text = element1.text.strip()

        element2 = self.find(element_loc2)
        element2_text = element2.text.strip()

        assert element1_text == element2_text

    def wait_for_element(self, locator: tuple[str, str], condition: EC, timeout: int = None):
        """Метод явного ожидания элемента"""
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def check_create_alert_text_is(self, locator: tuple, expected_text: str):
        """Метод для проверки текста элемента на странице"""

        # Явное ожидание, пока текст элемента не станет непустым
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(locator))

        # Поиск элемента по переданному локатору
        element = self.driver.find_element(*locator)

        # Проверка, что текст элемента соответствует ожидаемому
        actual_text = element.text.strip()
        assert actual_text == expected_text

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
