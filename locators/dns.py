from selenium.webdriver.common.by import By

# product_from_list = (By.XPATH, '//*[contains(@class, "catalog-product__name ui-link ui-link_black")]')
product_from_list = (By.XPATH, '(//*[contains(@class, "catalog-product__name ui-link ui-link_black")])[{}]')
all_features = (By.XPATH, '//*[contains(@class, "button-ui button-ui_white product-characteristics__expand")]')


priceNow = (By.XPATH, '//*[contains(@class, "product-buy__price product-buy__price_active")]')
priceOriginal = (By.XPATH, '//*[contains(@class, "product-buy__prev")]')
priceMain = (By.XPATH, '(//*[contains(@class, "product-buy__price")])[last()]') 

guarantee = (By.XPATH, '//*[@class="product-characteristics" and descendant::*[contains(text(), " Гарантия от производителя ")]]//*[@class="product-characteristics__spec-value"]')
guarantee_mac = (By.XPATH, '//*[@class="product-characteristics" and descendant::*[contains(text(), " Гарантия от продавца ")]]//*[@class="product-characteristics__spec-value"]')
 
# country  нет в  DNS
series = (By.XPATH, '//*[@class="product-characteristics__spec" and descendant::*[contains(text(), " Модель ")]]//*[@class="product-characteristics__spec-value"]')
os = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Операционная система ")]]//*[@class="product-characteristics__spec-value"]')
# os_windows нет отдельного параметра в DNS
processor_cores = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Общее количество ядер ")]]//*[@class="product-characteristics__spec-value"]')
processor_cores_pr = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Количество производительных ядер ")]]//*[@class="product-characteristics__spec-value"]')


processor_model = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Модель процессора ")]]//*[@class="product-characteristics__spec-value"]')
# processor нет отдельного параметра в DNS
# processor_type нет отдельного параметра в DNS
processor_frequency = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Частота процессора ")]]//*[@class="product-characteristics__spec-value"]')
# gpu_manufacturer нет отдельного параметра в DNS (все в контроллере сразу)
gpu_controller = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Модель встроенной видеокарты ")]]//*[@class="product-characteristics__spec-value"]')
gpu_capacity = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Объем видеопамяти ")]]//*[@class="product-characteristics__spec-value"]')
screen_size = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Диагональ экрана (дюйм) ")]]//*[@class="product-characteristics__spec-value"]')
# diagonal - not
screen_frequency = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Максимальная частота обновления экрана ")]]//*[@class="product-characteristics__spec-value"]')
ssd_size = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Общий объем твердотельных накопителей (SSD) ")]]//*[@class="product-characteristics__spec-value"]')
ram = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Объем оперативной памяти ")]]//*[@class="product-characteristics__spec-value"]')
ram_type = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Тип оперативной памяти ")]]//*[@class="product-characteristics__spec-value"]')
hdmi = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Видеоразъемы ")]]//*[@class="product-characteristics__spec-value"]')
material = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Материал корпуса ")]]//*[@class="product-characteristics__spec-value"]')
# battery not
weight = (By.XPATH, '//*[@class="product-characteristics__spec product-characteristics__ovh" and descendant::*[contains(text(), " Вес ")]]//*[@class="product-characteristics__spec-value"]')


