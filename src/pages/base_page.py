from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
import random
import string


class BasePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.username = 'khoinguyennickapp@gmail.com'
        self.password = 'overloadOndream@'

    def get_list_elements_by_xpath(self, locator):
        list_element = self.driver.find_elements(By.XPATH, locator)
        return list_element

    def get_web_element_by_xpath(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element
