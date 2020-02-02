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
    countries = []
    zones = []
    for i in range(2, 240):
        str_selector = "tr:nth-child(" + str(i) + ") td:nth-child(5)"
        country_element = driver.find_element_by_css_selector(str_selector)
        country_text = country_element.get_attribute("textContent")
        countries.append(country_text)
        str_selector = "tr:nth-child(" + str(i) + ") td:nth-child(6)"
        zone_element = driver.find_element_by_css_selector(str_selector)
        zone_text = zone_element.get_attribute("textContent")
        zones.append(int(zone_text))
    sorted_countries = countries[:]
    sorted_countries.sort()
    assert countries == sorted_countries

    for i_zones_number in zones:
        if i_zones_number > 0:
            str_selector = "tr:nth-child(" + str(zones.index(i_zones_number) + 2) + ") td:nth-child(5) a"
            country_element = driver.find_element_by_css_selector(str_selector)
            edit_country_href = country_element.get_attribute("href")
            driver.get(str(edit_country_href))
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.ID, "table-zones")))

            a_zones = driver.find_elements_by_css_selector("#table-zones tr td:nth-child(3)")
            current_zone_texts = []
            for current_zone in a_zones:
                current_zone_text = current_zone.get_attribute("textContent")
                if len(current_zone_text) != 0:
                    current_zone_texts.append(current_zone_text)
            sorted_current_zone_texts = current_zone_texts[:]
            sorted_current_zone_texts.sort()
            assert current_zone_texts == sorted_current_zone_texts
            driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")


    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    countries = driver.find_elements_by_css_selector("#content tr.row")
    for i_country_number in range(2, len(countries)+2):
        current_country = driver.find_element_by_css_selector("#content tr:nth-child(" + str(i_country_number) + ") td:nth-child(3) a")
        current_country.click()
        zones = driver.find_elements_by_css_selector("#table-zones tr")
        zones_country = []
        for i in range(2, len(zones)):
            str_selector = "#table-zones tr:nth-child(" + str(i) + ") td:nth-child(3) option[selected=selected]"
            zone_element = driver.find_element_by_css_selector(str_selector)
            zone_text = zone_element.get_attribute("textContent")
            zones_country.append(zone_text)
        sorted_zones = zones_country[:]
        sorted_zones.sort()
        assert zones_country == sorted_zones
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")



