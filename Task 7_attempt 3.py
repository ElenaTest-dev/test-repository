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
    entries = driver.find_elements_by_css_selector("#app-")
    for i in range(len(entries)):
        i = i + 1
        app_list_selector = "li#app-:nth-child(" + str(i) + ")"
        driver.find_element_by_css_selector(app_list_selector).click()
        doc_entries = driver.find_elements_by_css_selector("[id^=doc-]")
        for y in range(len(doc_entries)):
            y = y + 1
            doc_list_selector = "[id^=doc-]:nth-child(" + str(y) + ")"
            driver.find_element_by_css_selector(doc_list_selector).click()
            check_header_exists(driver)



