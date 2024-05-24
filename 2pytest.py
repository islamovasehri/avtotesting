import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def driver():
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")
    yield driver
    driver.quit()

def test_login_area_properties(driver):
    wait = WebDriverWait(driver, 10)
     username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#username')))
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#password')))
    login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button#login')))
    username_placeholder = username_input.get_attribute("placeholder")
    password_placeholder = password_input.get_attribute("placeholder")
    login_button_text = login_button.text
    
    assert username_placeholder == "Enter your username", f"Expected placeholder 'Enter your username', but got {username_placeholder}"
    assert password_placeholder == "Enter your password", f"Expected placeholder 'Enter your password', but got {password_placeholder}"
    assert login_button_text == "Login", f"Expected button text 'Login', but got {login_button_text}"username_width = username_input.size['width']
    password_width = password_input.size['width']
    login_button_color = login_button.value_of_css_property("background-color")
    
    assert username_width == 300, f"Expected username input width 300, but got {username_width}"
    assert password_width == 300, f"Expected password input width 300, but got {password_width}"
    assert login_button_color == "rgba(0, 123, 255, 1)", f"Expected login button color 'rgba(0, 123, 255, 1)', but got {login_button_color}"