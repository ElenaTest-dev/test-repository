import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

    we1 = "900"
    we2 = "700"
    text_dec1 = "line-through rgb(119, 119, 119)"
    text_dec3 = "line-through rgb(102, 102, 102)"
    color = "rgb(204, 0, 0)"

    driver.get("http://localhost/litecart/en/")
    a = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) div.name")
    text1 = a.get_attribute("textContent")
    element = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) s.regular-price")
    name1 = element.get_attribute("textContent")
    dec1 = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) s.regular-price").value_of_css_property("text-decoration")
    size1 = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) s.regular-price").size
    h1 = size1.get('height')
    w1 = size1.get('width')

    element = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) strong.campaign-price")
    name2 = element.get_attribute("textContent")
    weight2 = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) strong.campaign-price").value_of_css_property("font-weight")
    color2 = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) strong.campaign-price").value_of_css_property("color")
    size2 = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) strong.campaign-price").size
    h2 = size2.get('height')
    w2 = size2.get('width')

    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")
    b = driver.find_element_by_css_selector("h1.title")
    text2 = b.get_attribute("textContent")
    element = driver.find_element_by_css_selector("div.information s.regular-price")
    name3 = element.get_attribute("textContent")
    dec3 = driver.find_element_by_css_selector("div.information s.regular-price").value_of_css_property("text-decoration")
    size3 = driver.find_element_by_css_selector("div.information s.regular-price").size
    h3= size3.get('height')
    w3 = size3.get('width')

    element = driver.find_element_by_css_selector("div.information strong.campaign-price")
    name4 = element.get_attribute("textContent")
    color4 = driver.find_element_by_css_selector("div.information strong.campaign-price").value_of_css_property("color")
    weight4 = driver.find_element_by_css_selector("div.information strong.campaign-price").value_of_css_property("font-weight")
    size4 = driver.find_element_by_css_selector("div.information strong.campaign-price").size
    h4 = size4.get('height')
    w4 = size4.get('width')

    assert text1 == text2
    assert name1 == name3
    assert name2 == name4
    assert we1 == weight2
    assert we2 == weight4
    assert text_dec1 == dec1
    assert text_dec3 == dec3
    assert color == color2 == color4
    assert h2 > h1 and w2 > w1
    assert h4 > h3 and w4 > w3




