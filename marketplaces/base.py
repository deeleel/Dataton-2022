from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import config
import csv
import time
import json

CLICK_RETRY = 3

class BaseFunctions:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 4
        return WebDriverWait(self.driver, timeout=timeout)
    
    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 500)", "")

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    
    def click(self, locator, timeout=5):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                time.sleep(1)
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def go_back(self):
        self.driver.execute_script("window.history.go(-1)")

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)


    def is_visible(self, locator):
        return EC.visibility_of(locator)


    def write_to_file(self, data):
        with open('data.csv', 'a', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames = config.headers)
            # writer.writeheader()
            writer.writerow(data)

    def found(self, locator):
        try:
            self.find(locator=locator)
        except TimeoutException:
            return False
        return self.find(locator=locator)
