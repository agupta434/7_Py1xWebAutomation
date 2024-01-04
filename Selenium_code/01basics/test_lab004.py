import time

from selenium import webdriver

# quit and close
def test_open_login():
    driver = webdriver.Chrome()  # Create a session (new browser) with POST request
    driver.get("https://www.google.com")  # Navigate to URL with GET
    # driver.maximize_window()
    print(driver.title)  # GET request


    # driver.print_page()
    driver.back()
    driver.get("https://www.bing.com")
    print(driver.title)
    driver.refresh()
    driver.forward()
    driver.get("https://www.gmail.com")
    print(driver.title)

    # driver.close() # close teh current window not other tab
    # also session ID != null (invalid)


    driver.quit()  # quit the browser and close all the windows. Session ID = null
    time.sleep(20)