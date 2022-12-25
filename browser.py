from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import config
from fake_useragent import UserAgent


def get_userAgent():
    ua = UserAgent() #browsers=['chrome']
    userAgent = ua.random
    print(userAgent)
    return userAgent


def open(url):
    options = Options()
    ua = get_userAgent()
    options.add_argument(f'user-agent={ua}')
    # options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(executable_path=config.webdriver_path, options=options)
    driver.get(url)
    driver.maximize_window()

    return driver

def close(driver):
    time.sleep(5)
    driver.close()