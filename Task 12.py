import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import os

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector("li#app-:nth-child(2)").click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.button:nth-child(2)")))
    driver.find_element_by_css_selector("a.button:nth-child(2)").click()
    driver.find_element_by_css_selector("[type=radio]").click()
    driver.find_element_by_css_selector("[name^=name]").send_keys("armchair")
    driver.find_element_by_css_selector("[name=code]").send_keys("78634")
    driver.find_element_by_css_selector("tr:nth-child(7) tr:nth-child(4) input").click()
    driver.find_element_by_css_selector("tr:nth-child(7) tr:nth-child(4) input").click()
    driver.find_element_by_css_selector("[name=quantity]").clear()
    driver.find_element_by_css_selector("[name=quantity]").send_keys("1")
    driver.find_element_by_css_selector("[name=date_valid_from]").send_keys(Keys.HOME + "01.01.2001")
    driver.find_element_by_css_selector("[name=date_valid_from]").send_keys("29.01.2020")
    driver.find_element_by_css_selector("[name=date_valid_to]").send_keys(Keys.HOME + "01.01.2001")
    driver.find_element_by_css_selector("[name=date_valid_to]").send_keys("29.02.2020")

    base_path = os.getcwd()
    image_relative_path  = "\images\\armchair.jpg"
    image_absolute_path = base_path + image_relative_path
    driver.find_element_by_css_selector("div#tab-general tr:nth-child(9) input").send_keys(image_absolute_path)

    driver.find_element_by_css_selector("td#content li:nth-child(2) a").click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.NAME, "manufacturer_id")))
    driver.find_element_by_name("manufacturer_id").click()
    select1 = Select(driver.find_element_by_name("manufacturer_id"))
    select1.select_by_visible_text("ACME Corp.")
    driver.find_element_by_name("keywords").send_keys("furniture")
    driver.find_element_by_css_selector("#tab-information tr:nth-child(4) input").send_keys("blue armchair")
    driver.find_element_by_css_selector("div.trumbowyg-editor").send_keys("An armchair is a comfortable, cushioned chair with a support on each side, where you can rest your arms while you sit")
    driver.find_element_by_css_selector("#tab-information tr:nth-child(6) input").send_keys("Exclusive armchairs")
    driver.find_element_by_css_selector("#tab-information tr:nth-child(7) input").send_keys("Exclusive velvet blue armchair")

    driver.find_element_by_css_selector("td#content li:nth-child(4) a").click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "tab-prices")))
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys("225")
    driver.find_element_by_name("purchase_price_currency_code").click()
    select1 = Select(driver.find_element_by_name("purchase_price_currency_code"))
    select1.select_by_visible_text("Euros")
    driver.find_element_by_css_selector("div#tab-prices tr:nth-child(2) td:nth-child(2) input").clear()
    driver.find_element_by_css_selector("div#tab-prices tr:nth-child(2) td:nth-child(2) input").send_keys("270")
    driver.find_element_by_css_selector("div#tab-prices tr:nth-child(3) td:nth-child(2) input").clear()
    driver.find_element_by_css_selector("div#tab-prices tr:nth-child(3) td:nth-child(2) input").send_keys("240")
    driver.find_element_by_css_selector("button[name=save]").click()

    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    a = driver.find_element_by_css_selector("#content tr:nth-child(4) td:nth-child(3) a")
    text = a.get_attribute("textContent")
    assert text == "armchair"





