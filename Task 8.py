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

def check_exists_by_xpath(driver, xpath):
    assert len(driver.find_elements_by_xpath(xpath)) > 0

def test_example(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/en/")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "box-most-popular")))
    check_exists_by_xpath(driver, "//div[contains(@class, 'sticker new')]")
    check_exists_by_xpath(driver, "//div[contains(@class, 'sticker sale')]")

