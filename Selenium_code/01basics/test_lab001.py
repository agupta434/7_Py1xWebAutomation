from selenium import webdriver


def test_open_login():
    driver = webdriver.Chrome()  # Create a session (new browser) with POST request
    driver.get("https://google.com")  # Navigate to URL with GET
    driver.maximize_window()
    print(driver.title)  # GET request
    print(driver.current_url)
    driver.quit()
