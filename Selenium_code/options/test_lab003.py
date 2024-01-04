import time

from selenium import webdriver


def test_open_login():
    # driver = webdriver.Chrome()  # fresh chrome which doesn't have anything
    chrome_options = webdriver.ChromeOptions()
    # extension_path = "Y:\\7_Python_Webautomation\\Py1xWebAutomation\\adblocker.crx"
    extension_path = r"Y:\7_Python_Webautomation\Py1xWebAutomation\adblocker.crx"
    # extension_path = "Y:/7_Python_Webautomation/Py1xWebAutomation/adblocker.crx"
    # use double backward \\ slash or single forward / slash
    chrome_options.add_extension(extension_path)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)  # fresh chrome which doesn't have anything
    driver.get("https://google.com")  # Navigate to URL with GET
    # driver.maximize_window()
    print(driver.title)  # GET request

    time.sleep(20)
    driver.quit() # quit the browser and close all the windows. Session ID = null
