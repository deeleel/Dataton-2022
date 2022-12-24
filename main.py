import config
import browser
from marketplaces.mvideo_base import Mvideo

# For MVIDEO marketplace
driver = browser.open(config.url_mvideo)
mvideo = Mvideo(driver)

mvideo.open_product_mv(2)
mvideo.get_features_mv()

print('closing ----------')
browser.close(driver=driver)
