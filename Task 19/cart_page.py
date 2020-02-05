import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def turn_off_product_animation(self):
        # Ожидаем пока анимация (движение картинок) подгрузится, чтобы можно было сделать клик на картинке
        time.sleep(2)
        small_product_pictures = self.driver.find_elements_by_css_selector("#box-checkout-cart li.shortcut img")
        # Делаем клик на левую нижнюю картинку, чтобы остановить анимацию (иначе далее проблема с кликом на кнопке удаления)
        small_product_pictures[0].click()
        return self

    def remove_product(self):
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#box-checkout-cart button[name=remove_cart_item]")))
        self.driver.find_element_by_css_selector("#box-checkout-cart button[name=remove_cart_item]").click()
        return self

    def get_current_products_from_table(self):
         self.current_products = self.driver.find_elements_by_css_selector("#order_confirmation-wrapper tr td.item")
         return self


    def check_product_was_removed(self, expected_products_amount):
        max_wait_time = 10
        current_time = 0
        result = False
        # Ожидаем пока количество товаров в таблице не уменьшится на один
        while current_time < max_wait_time:
            time.sleep(1)
            self.get_current_products_from_table()
            if expected_products_amount == len(self.current_products):
                result = True
                break
            current_time += 1
        return result
    
    

