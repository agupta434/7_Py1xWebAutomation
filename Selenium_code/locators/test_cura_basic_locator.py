import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

# quit and close
def test_open_login():
    driver = webdriver.Chrome()  # Create a session (new browser) with POST request
    LOGGER = logging.getLogger(__name__)
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Navigate to URL with GET
    driver.maximize_window()
    # print(driver.title)
    LOGGER.info(driver.title)

    make_appointment_btn = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_btn.click()
    # In case of space use . and before while serching -->  btn btn-dark btn - lg --> btn.btn-dark.btn-lg
    # make_appointment_btn = driver.find_elements(By.CLASS_NAME, "btn.btn-dark.btn-lg")
    # make_appointment_btn[1].click()

    print(driver.current_url)
    # verification of url and assert
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Error - Wrong URL"

    username = driver.find_element(By.NAME, "username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")

    submit_btn = driver.find_element(By.ID, "btn-login")
    submit_btn.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Error - Wrong URL"



    time.sleep(5)
    driver.quit()  # quit the browser and close all the windows. Session ID = null
