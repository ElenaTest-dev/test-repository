import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

from main_page import MainPage
from product_page import ProductPage
from cart_page import CartPage

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_add_and_remove_products(driver):
    main_page = MainPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    put_products_into_cart(main_page, product_page)
    remove_products_from_cart(main_page, cart_page)

def put_products_into_cart(main_page, product_page):
    main_page.open()
    for i in range(1, 4):
        main_page.click_on_first_duck()
        product_page.get_duck_size_values_from_list()
        if len(product_page.selects) != 0:
            product_page.choose_duck_size_from_list()
        product_page.add_to_cart_product_and_check_quantity(i)
        main_page.open()

def remove_products_from_cart(main_page, cart_page):
    main_page.click_on_checkout()
    cart_page.turn_off_product_animation()
    cart_page.get_current_products_from_table()
    products = cart_page.current_products
    current_product_amount = len(products)
    # Поочередно удаляем все товары из корзины
    for i in range(1, len(products)+1):
        cart_page.remove_product()
        current_product_amount -= 1
        check_result = cart_page.check_product_was_removed(current_product_amount)
        assert check_result

