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

def test_choose_password_area_properties(driver):
    wait = WebDriverWait(driver, 10)
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]#password')))
    confirm_password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]#confirm_password')))
    submit_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button#submit_password')))
 password_placeholder = password_input.get_attribute("placeholder")
    confirm_password_placeholder = confirm_password_input.get_attribute("placeholder")
    submit_button_text = submit_button.text
assert password_placeholder == "Enter your password", f"Expected placeholder 'Enter your password', but got {password_placeholder}"
    assert confirm_password_placeholder == "Confirm your password", f"Expected placeholder 'Confirm your password', but got {confirm_password_placeholder}"
    assert submit_button_text == "Submit", f"Expected button text 'Submit', but got {submit_button_text}"
password_width = password_input.size['width']
    confirm_password_width = confirm_password_input.size['width']
    submit_button_color = submit_button.value_of_css_property("background-color")

    assert password_width == 300, f"Expected password input width 300, but got {password_width}"
    assert confirm_password_width == 300, f"Expected confirm password input width 300, but got {confirm_password_width}"
    assert submit_button_color == "rgba(0, 123, 255, 1)", f"Expected submit button color 'rgba(0, 123, 255, 1)', but got {submit_button_color}"   