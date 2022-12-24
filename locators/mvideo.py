from selenium.webdriver.common.by import By

product_from_list = (By.XPATH, '//*[contains(@class, "product-title__text")]')
all_features = (By.XPATH, '//*[contains(@class, "characteristics-link")]')

# need features!
# ...

priceNow = (By.XPATH, '//*[@class="price__main-value"]')
priceOriginal = (By.XPATH, '//*[contains(@class, "price__sale-value")]')

guarantee = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Гарантия"]]//*[@class="item-with-dots__value"]')
country = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Страна"]]//*[@class="item-with-dots__value"]')

series = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Серия"]]//*[@class="item-with-dots__value"]')
os = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Операционная "]]//dd')
os_windows = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Windows"]]//dd')

processor_cores = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="ядер"]]//*[@class="item-with-dots__value"]')
processor_model = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Модель "] and descendant::*[text()="процессора"]]//*[@class="item-with-dots__value"]')
processor_type = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Тип "] and descendant::*[text()="процессора"]]//*[@class="item-with-dots__value"]')
processor_frequency = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Частота "] and descendant::*[text()="процессора"]]//*[@class="item-with-dots__value"]')

gpu_manufacturer = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Производитель "] and descendant::*[text()="видеопроцессора"]]//*[@class="item-with-dots__value"]')
gpu_controller = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Графический "] and descendant::*[text()="контроллер"]]//*[@class="item-with-dots__value"]')
gpu_capacity = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Объем "] and descendant::*[text()="видеопамяти"]]//*[@class="item-with-dots__value"]')

screen_size = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Диагональ "] and descendant::*[text()="экрана"]]//*[@class="item-with-dots__value"]')
screen_frequency = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Частота "] and descendant::*[text()="обновления"]]//*[@class="item-with-dots__value"]')

ssd_size = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Объем "] and descendant::*[text()="SSD"]]//*[@class="item-with-dots__value"]')
ram = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Оперативная память "]]//*[@class="item-with-dots__value"]')

ram_type = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Тип оперативной "] and descendant::*[text()="памяти"]]//*[@class="item-with-dots__value"]')

hdmi = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Выход "] and descendant::*[text()="HDMI"]]//*[@class="item-with-dots__text"]')
material = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Материал "] and descendant::*[text()="корпуса"]]//*[@class="item-with-dots__value"]')
battery = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Работа от "] and descendant::*[text()="аккумулятора"]]//*[@class="item-with-dots__value"]')
weight = (By.XPATH, '//mvideo-item-with-dots[descendant::*[text()="Вес"]]//*[@class="item-with-dots__value"]')

