import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/en/")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "box-most-popular")))

    box_element_names = ["div#box-most-popular", "div#box-campaigns", "div#box-latest-products"]

    for i_box_element_name in box_element_names:
        duck_elements = driver.find_elements_by_css_selector(i_box_element_name + " li.product.column.shadow.hover-light")
        for i in range(len(duck_elements)):
            i = i + 1
            found_sticker_sale = False
            found_sticker_new = False

            str_selector = (i_box_element_name + " li.product.column.shadow.hover-light:nth-child(" + str(i) +") div.sticker.sale")
            sticker_sale_elements = driver.find_elements_by_css_selector(str_selector)
            if len(sticker_sale_elements) == 1:
                found_sticker_sale = True

            str_selector = (i_box_element_name + " li.product.column.shadow.hover-light:nth-child(" + str(i) +") div.sticker.new")
            sticker_new_elements = driver.find_elements_by_css_selector(str_selector)
            if len(sticker_new_elements) == 1:
                found_sticker_new = True

            result = False
            if found_sticker_sale or found_sticker_new:
                if not (found_sticker_sale and found_sticker_new):
                    result = True
            assert(result)

