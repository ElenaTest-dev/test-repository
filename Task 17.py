import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    for i in range(5, 10):
        str_selector = "#content tr:nth-child(" + str(i) + ") td:nth-child(3) a"
        driver.find_element_by_css_selector(str_selector).click()
        for l in driver.get_log("browser"):
            assert False
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
