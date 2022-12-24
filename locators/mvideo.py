from selenium.webdriver.common.by import By

product_from_list = (By.XPATH, '//*[contains(@class, "product-title__text")]')
all_features = (By.XPATH, '//*[contains(@class, "characteristics-link")]')

# need features!
# ...

guarantee = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Гарантия"]]//*[@class="item-with-dots__text ng-star-inserted"]')
country = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Страна"]]//*[@class="item-with-dots__text"]')

series = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Серия"]]//*[@class="item-with-dots__text"][last()]')
os = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Операционная "]]//*[@class="item-with-dots__text"]')

