from selenium.webdriver.common.by import By

# Поиск элемента страницы
first_element_loc = (By.XPATH, '//ol[@class="products list items product-items"]/descendant::div[1]/descendant::strong')
compare_product_loc = (By.XPATH, '//*[@aria-labelledby="block-compare-heading"]/descendant::li/child::strong')

# Поиск элемента кнопок
button_add_to_compair_loc = (By.XPATH, '//div[@class="product-item-inner"]/descendant::div[3]/child::a[2]')
