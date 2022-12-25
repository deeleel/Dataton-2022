import config
import browser
from marketplaces.mvideo_base import Mvideo
import time

# For MVIDEO marketplace

for j in range(1, 24):

    driver = browser.open(config.url_mvideo.format(j))
    mvideo = Mvideo(driver)

    for i in range(1, 25):
        print(i, j)
        mvideo.get_name(i)

    print('closing ----------')
    browser.close(driver=driver)
