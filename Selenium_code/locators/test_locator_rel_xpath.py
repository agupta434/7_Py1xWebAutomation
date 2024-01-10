import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    rel_xpath_email = driver.find_element(By.XPATH, "//div/input[@type='email']")
    rel_xpath_email.send_keys("augtest_040823@idrive.com")
    rel_xpath_password = driver.find_element(By.XPATH, "//div/input[@type='password']")
    rel_xpath_password.send_keys("augtest_040823@idrive.com")
    rel_xpath_submit_btn = driver.find_element(By.XPATH, "//div/button[@type='submit']")
    rel_xpath_submit_btn.click()

    time.sleep(5)
    driver.quit()
