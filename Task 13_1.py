import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://litecart.stqa.ru/en/")

    for i in range(1, 4):
        driver.find_element_by_css_selector("#box-most-popular li:nth-child(1) div.image-wrapper").click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.NAME, "add_cart_product")))
        selects = driver.find_elements_by_css_selector("#box-product tr:nth-child(1) select")
        if len(selects) != 0:
            driver.find_element_by_css_selector("#box-product tr:nth-child(1) select").click()
            select1 = Select(driver.find_element_by_css_selector("#box-product tr:nth-child(1) select"))
            select1.select_by_visible_text("Small")
        driver.find_element_by_name("add_cart_product").click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(i)))
        driver.get("http://litecart.stqa.ru/en/")


    driver.find_element_by_css_selector("#cart a.link").click()
    # Ожидаем пока анимация (движение картинок) подгрузится, чтобы можно было сделать клик на картинке
    time.sleep(2)
    a = driver.find_elements_by_css_selector("#box-checkout-cart li.shortcut img")
    # Делаем клик на левую нижнюю картинку, чтобы остановить анимацию (иначе далее проблема с кликом на кнопке удаления)
    a[0].click()
    products = driver.find_elements_by_css_selector("#order_confirmation-wrapper tr td.item")
    current_product_amount = len(products)
    # Поочередно удаляем все товары из корзины
    for i in range(1, len(products)+1):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#box-checkout-cart button[name=remove_cart_item]")))
        driver.find_element_by_css_selector("#box-checkout-cart button[name=remove_cart_item]").click()
        current_product_amount -= 1
        max_wait_time = 10
        current_time = 0
        result = False
        # Ожидаем пока количество товаров в таблице не уменьшится на один
        while current_time < max_wait_time:
            time.sleep(1)
            current_products = driver.find_elements_by_css_selector("#order_confirmation-wrapper tr td.item")
            if current_product_amount == len(current_products):
                result = True
                break
            current_time += 1
        assert result


