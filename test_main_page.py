from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_check_add_to_basket_button(browser):
    browser.implicitly_wait(20)
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR ,"button:nth-child(3)")
    assert button is not None, "Web-page contains 'Add to basket' button "
    time.sleep(30)