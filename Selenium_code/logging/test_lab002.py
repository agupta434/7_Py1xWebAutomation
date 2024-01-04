from selenium import webdriver
import logging

def test_open_login():
    driver = webdriver.Chrome()  # Create a session (new browser) with POST request
    LOGGER = logging.getLogger(__name__)
    driver.get("https://google.com")  # Navigate to URL with GET
    driver.maximize_window()
    # print(driver.title)  # GET request
    LOGGER.info(driver.title)
    driver.quit()
