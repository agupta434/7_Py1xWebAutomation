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
    LOGGER.info(driver.current_url)
    assert driver.title == "CURA Healthcare Service", "Wrong Title"

    #################
    # make_appointment_btn=driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']" ) # fast xpath
    ########################################################
    # make_appointment_btn=driver.find_element(By.XPATH, "//*[@id='btn-make-appointment']" ) # slow xpath
    # * is wild card. in this find id = btn-make-appointment in all tag name
    ####################################    TEXT
    # make_appointment_btn = driver.find_element(By.XPATH, "//a[text()='Make Appointment']")
    ################ partial Text
    make_appointment_btn = driver.find_element(By.XPATH, "//a[text()='Make Appointment']")
    ############ List of element
    list_of_element_ptag = driver.find_elements(By.XPATH, "//p[contains(text(),'A')]")
    for i in list_of_element_ptag:
        print(i.text)


    make_appointment_btn.click()



    time.sleep(5)
    driver.quit()