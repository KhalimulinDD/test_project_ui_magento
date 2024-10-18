from selenium.webdriver.common.by import By

first_element_loc = (By.XPATH, '//ol[@class="products list items product-items"]/descendant::div[1]/descendant::strong')
compare_product_loc = (By.XPATH, '//*[@aria-labelledby="block-compare-heading"]/descendant::li/child::strong')
men_loc = (By.ID, 'ui-id-5')
men_bottoms_loc = (By.ID, 'ui-id-18')
men_bottoms_shorts_loc = (By.ID, 'ui-id-24')
text_shorts_loc = (By.ID, 'page-title-heading')
sort_by_loc = (By.XPATH, '//*[@class="column main"]/descendant::select[@id="sorter"][1]')
sort_by_price_loc = (
    By.XPATH, '//*[@class="column main"]/descendant::select[@id="sorter"][1]/child::option[@value="price"]'
)
sorted_goods_loc = (By.XPATH, '//*[@class="product details product-item-details"]/descendant::span[@class="price"]')
button_add_to_compair_loc = (By.XPATH, '//div[@class="product-item-inner"]/descendant::div[3]/child::a[2]')
