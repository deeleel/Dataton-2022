import config
import browser
from marketplaces.mvideo_base import Mvideo
import time

# Example

page = 1

driver = browser.open(config.url_mvideo.format(page))
mvideo = Mvideo(driver)

for i in range(1, 25):
    print(i)
    mvideo.open_product_mv(i)
    mvideo.get_features_mv()

print('closing ----------')
browser.close(driver=driver)