import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def get_alert_text(driver):
    alert = Alert(driver)
    text = alert.text
    alert.accept()
    return text

# Test 1: Empty username
def test_empty_username(setup_teardown):
    driver = setup_teardown
    driver.get("file:///C:/12c6%20devops/week%2012/templates/register.html")  # update path

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
    alert_text = get_alert_text(driver)
    assert alert_text == "Name should not be empty"

# Test 2: Empty password
def test_empty_password(setup_teardown):
    driver = setup_teardown
    driver.get("file:///C:/12c6%20devops/week%2012/templates/register.html")  # update path

    driver.find_element(By.ID, "username").send_keys("Tisha")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
    alert_text = get_alert_text(driver)
    assert alert_text == "Password should not be empty"

# Test 3: Password too short
def test_short_password(setup_teardown):
    driver = setup_teardown
    driver.get("file:///C:/12c6%20devops/week%2012/templates/register.html")  # update path

    driver.find_element(By.ID, "username").send_keys("Tisha")
    driver.find_element(By.ID, "password").send_keys("abc1")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
    alert_text = get_alert_text(driver)
    assert alert_text == "Password must be at least 6 characters long"

# Test 4: Valid input
def test_valid_input(setup_teardown):
    driver = setup_teardown
    driver.get("file:///C:/12c6%20devops/week%2012/templates/register.html")  # update path

    driver.find_element(By.ID, "username").send_keys("Tisha")
    driver.find_element(By.ID, "password").send_keys("abc123")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
    alert_text = get_alert_text(driver)
    assert alert_text == "Form submitted successfully!"
