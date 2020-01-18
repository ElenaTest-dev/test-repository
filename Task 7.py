import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def check_exists_by_xpath(driver, xpath):
    assert len(driver.find_elements_by_xpath(xpath)) > 0

def test_example(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector("li#app-:nth-child(1)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(1) li#doc-template").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(1) li#doc-logotype").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2) li#doc-catalog").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2) li#doc-product_groups").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2) li#doc-option_groups").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2) li#doc-manufacturers").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2) li#doc-suppliers").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2) li#doc-delivery_statuses").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2) li#doc-sold_out_statuses").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2) li#doc-quantity_units").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(2) li#doc-csv").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(3)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(4)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(5)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(5) li#doc-customers").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(5) li#doc-csv").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(5) li#doc-newsletter").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(6)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(7)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(7) li#doc-languages").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(7) li#doc-storage_encoding").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(8)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(8) li#doc-jobs").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(8) li#doc-customer").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(8) li#doc-shipping").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(8) li#doc-payment").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(8) li#doc-order_total").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(8) li#doc-order_success").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(8) li#doc-order_action").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(9)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(9) li#doc-orders").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(9) li#doc-order_statuses").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(10)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(11)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(11) li#doc-monthly_sales").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(11) li#doc-most_sold_products").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(11) li#doc-most_shopping_customers").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(12)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(12) li#doc-store_info").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(12) li#doc-defaults").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(12) li#doc-general").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(12) li#doc-listings").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(12) li#doc-images").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(12) li#doc-checkout").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(12) li#doc-advanced").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(12) li#doc-security").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(13)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(14)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(14) li#doc-tax_classes").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(14) li#doc-tax_rates").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(15)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(15) li#doc-search").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(15) li#doc-scan").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(15) li#doc-csv").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(16)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(17)").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")
    driver.find_element_by_css_selector("li#app-:nth-child(17) li#doc-vqmods").click()
    check_exists_by_xpath(driver, "//td[@id='content']//h1")