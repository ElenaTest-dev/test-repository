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

def check_header_exists(driver):
    input_header_xpath = "//td[@id='content']//h1"
    check_exists_by_xpath(driver, input_header_xpath)

def test_example(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    strings = dict()
    strings[1] = ["li#doc-template", "li#doc-logotype"]
    strings[2] = ["li#doc-catalog", "li#doc-product_groups", "li#doc-option_groups", "li#doc-manufacturers", "li#doc-suppliers", "li#doc-delivery_statuses", "li#doc-sold_out_statuses", "li#doc-quantity_units", "li#doc-csv"]
    strings[3] = []
    strings[4] = []
    strings[5] = ["li#doc-customers", "li#doc-csv", "li#doc-newsletter"]
    strings[6] = []
    strings[7] = ["li#doc-languages", "li#doc-storage_encoding"]
    strings[8] = ["li#doc-jobs", "li#doc-customer", "li#doc-shipping", "li#doc-payment", "li#doc-order_total", "li#doc-order_success", "li#doc-order_action"]
    strings[9] = ["li#doc-orders", "li#doc-order_statuses"]
    strings[10] = []
    strings[11] = ["li#doc-monthly_sales", "li#doc-most_sold_products", "li#doc-most_shopping_customers"]
    strings[12] = ["li#doc-store_info", "li#doc-defaults", "li#doc-general", "li#doc-listings", "li#doc-images", "li#doc-checkout", "li#doc-advanced", "li#doc-security"]
    strings[13] = []
    strings[14] = ["li#doc-tax_classes", "li#doc-tax_rates"]
    strings[15] = ["li#doc-search", "li#doc-scan", "li#doc-csv"]
    strings[16] = []
    strings[17] = ["li#doc-vqmods"]
    entries = driver.find_elements_by_css_selector("#app-")
    for i in range(len(entries)):
        i = i + 1
        driver.find_element_by_css_selector("li#app-:nth-child(" + str(i) + ")").click()
        for i_string in strings[i]:
            driver.find_element_by_css_selector("li#app-:nth-child(" + str(i) + ") " +  i_string).click()
            check_header_exists(driver)

