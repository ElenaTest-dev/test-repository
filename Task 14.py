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
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_css_selector("#content tr:nth-child(3) td:nth-child(5) a").click()
    a_elements = driver.find_elements_by_css_selector("#content table:nth-child(2) a[target=_blank]")
    for i_element in a_elements:
        main_window = driver.current_window_handle
        i_element.click()
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.number_of_windows_to_be(2))
        all_windows = driver.window_handles
        for i_window in all_windows:
            if i_window != main_window:
                driver.switch_to_window(i_window)
                driver.close()
                driver.switch_to_window(main_window)

