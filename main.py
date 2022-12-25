import config
import browser
from marketplaces.mvideo_base import Mvideo
import time

# For MVIDEO marketplace
driver = browser.open(config.url_mvideo.format(8))
mvideo = Mvideo(driver)

for i in range(1, 20): # 25
    print(i)
    mvideo.open_product_mv(i)
    mvideo.get_features_mv()

print('closing ----------')
browser.close(driver=driver)
