from explicit import waiter
from explicit import ID, CSS
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://github.com/this/doesntexist")

    username_field = waiter.find_element(driver, "login_field", by=ID)
    username_field.click()
    username_field.send_keys("my_username")

    password_field = waiter.find_element(driver, "password", by=ID)
    password_field.click()
    password_field.send_keys("my_password")

    login_button = waiter.find_element(driver, "input.btn-primary", by=CSS)
    login_button.click()
finally:
    driver.quit()