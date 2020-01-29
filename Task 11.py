import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://litecart.stqa.ru/en/create_account")
    driver.find_element_by_css_selector("tr:nth-child(1) td:nth-child(1) [name=tax_id]").send_keys("87319")
    driver.find_element_by_css_selector("tr:nth-child(1) td:nth-child(2) [name=company]").send_keys("Piterstar")
    driver.find_element_by_css_selector("tr:nth-child(2) td:nth-child(1) [name=firstname]").send_keys("Anna")
    driver.find_element_by_css_selector("tr:nth-child(2) td:nth-child(2) [name=lastname]").send_keys("Kolegova")
    driver.find_element_by_css_selector("tr:nth-child(3) td:nth-child(1) [name=address1]").send_keys("960 Sterling Pl Brooklyn, NY 11213")
    driver.find_element_by_css_selector("tr:nth-child(4) td:nth-child(1) [name=postcode]").send_keys("63837")
    driver.find_element_by_css_selector("tr:nth-child(4) td:nth-child(2) [name=city]").send_keys("New York")
    driver.find_element_by_css_selector("span.select2-selection__arrow").click()
    select1 = Select(driver.find_element_by_css_selector("select.select2-hidden-accessible"))
    select1.select_by_visible_text("United States")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"tr:nth-child(5) td:nth-child(2) select")))
    driver.find_element_by_css_selector("tr:nth-child(5) td:nth-child(2) select").click()
    select_zone = Select(driver.find_element_by_css_selector("tr:nth-child(5) td:nth-child(2) select"))
    select_zone.select_by_visible_text("Alaska")
    driver.find_element_by_css_selector("tr:nth-child(6) td:nth-child(1) [name=email]").send_keys("annakolegova@laf78.com")
    driver.find_element_by_css_selector("tr:nth-child(6) td:nth-child(2) [name=phone]").send_keys("+79117621690")
    driver.find_element_by_css_selector("tr:nth-child(8) td:nth-child(1) [name=password]").send_keys("204trolo2a")
    driver.find_element_by_css_selector("tr:nth-child(8) td:nth-child(2) [name=confirmed_password]").send_keys("204trolo2a")
    driver.find_element_by_css_selector("tr:nth-child(9) button").click()
    driver.get("http://litecart.stqa.ru/en/")
    driver.find_element_by_css_selector("div#box-account li:nth-child(4) a").click()
    driver.find_element_by_css_selector("div.content [name=email]").send_keys("annakolegova@laf78.com")
    driver.find_element_by_css_selector("div.content [name=password]").send_keys("204trolo2a")
    driver.find_element_by_css_selector("tr:nth-child(4) button").click()
    driver.find_element_by_css_selector("div#box-account li:nth-child(4) a").click()

