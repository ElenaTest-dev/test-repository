import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_duck_size_values_from_list(self):
        element = self.wait.until(EC.element_to_be_clickable((By.NAME, "add_cart_product")))
        self.selects = self.driver.find_elements_by_css_selector("#box-product tr:nth-child(1) select")
        return self

    def choose_duck_size_from_list(self):
        self.driver.find_element_by_css_selector("#box-product tr:nth-child(1) select").click()
        select1 = Select(self.driver.find_element_by_css_selector("#box-product tr:nth-child(1) select"))
        select1.select_by_visible_text("Small")
        return self

    def add_to_cart_product_and_check_quantity(self, quantity):
        self.driver.find_element_by_name("add_cart_product").click()
        element = self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(quantity)))
        return self
