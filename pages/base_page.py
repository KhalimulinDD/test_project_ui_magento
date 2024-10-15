from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        """Метод инициализации драйвера"""
        self.driver = driver

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
