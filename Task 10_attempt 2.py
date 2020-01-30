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

def get_rgb_channel_values(css_string):
    splitted_str = []
    splitted_str = css_string.split("(")
    rgb_part = splitted_str[1]
    rgb_part = rgb_part[0:-1]
    rgb_part_no_spaces = rgb_part.split()
    rgb_part_no_spaces = ''.join(rgb_part_no_spaces)
    channel_values = rgb_part_no_spaces.split(",")
    return channel_values

def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    a = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) div.name")
    text1 = a.get_attribute("textContent")
    element = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) s.regular-price")
    name1 = element.get_attribute("textContent")
    dec1 = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) s.regular-price").value_of_css_property("text-decoration")
    is_line_through = dec1.find('line-through') != -1
    assert is_line_through
    rgb_values = get_rgb_channel_values(dec1)
    assert rgb_values[0] == rgb_values[1] == rgb_values[2]
    size1 = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) s.regular-price").size
    h1 = size1.get('height')
    w1 = size1.get('width')


    element = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) strong.campaign-price")
    name2 = element.get_attribute("textContent")
    weight2 = int(driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) strong.campaign-price").value_of_css_property("font-weight"))
    assert weight2 >= 700
    color2 = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) strong.campaign-price").value_of_css_property("color")
    rgb_values = get_rgb_channel_values(color2)
    assert rgb_values[1] == rgb_values[2]
    size2 = driver.find_element_by_css_selector("div#box-campaigns li:nth-child(1) strong.campaign-price").size
    h2 = size2.get('height')
    w2 = size2.get('width')


    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")
    b = driver.find_element_by_css_selector("h1.title")
    text2 = b.get_attribute("textContent")
    element = driver.find_element_by_css_selector("div.information s.regular-price")
    name3 = element.get_attribute("textContent")
    dec3 = driver.find_element_by_css_selector("div.information s.regular-price").value_of_css_property("text-decoration")
    is_line_through = dec3.find('line-through') != -1
    assert is_line_through
    rgb_values = get_rgb_channel_values(dec3)
    assert rgb_values[0] == rgb_values[1] == rgb_values[2]
    size3 = driver.find_element_by_css_selector("div.information s.regular-price").size
    h3= size3.get('height')
    w3 = size3.get('width')

    element = driver.find_element_by_css_selector("div.information strong.campaign-price")
    name4 = element.get_attribute("textContent")
    color4 = driver.find_element_by_css_selector("div.information strong.campaign-price").value_of_css_property("color")
    rgb_values = get_rgb_channel_values(color4)
    assert rgb_values[1] == rgb_values[2]
    weight4 = int(driver.find_element_by_css_selector("div.information strong.campaign-price").value_of_css_property("font-weight"))
    assert weight4 >= 700
    size4 = driver.find_element_by_css_selector("div.information strong.campaign-price").size
    h4 = size4.get('height')
    w4 = size4.get('width')

    assert text1 == text2
    assert name1 == name3
    assert name2 == name4
    assert h2 > h1 and w2 > w1
    assert h4 > h3 and w4 > w3




