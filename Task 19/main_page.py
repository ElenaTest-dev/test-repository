import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://litecart.stqa.ru/en/")
        return self

    def click_on_first_duck(self):
        self.driver.find_element_by_css_selector("#box-most-popular li:nth-child(1) div.image-wrapper").click()
        return self

    def click_on_checkout(self):
        self.driver.find_element_by_css_selector("#cart a.link").click()
        return self


