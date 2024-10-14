from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    # Метод инициализации драйвера
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Метод для открытия страницы
    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    # Метод использования одного найденного элемента
    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    # Метод использования нескольких найденных элементов
    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    # Метод скролла до нужного элемента
    def scroll(self, locator: tuple):
        self.driver.execute_script("arguments[0].scrollIntoView();", *locator)
