from selenium import webdriver

driver = webdriver.Chrome()
"""
The Explicit package abstracts away the complexities associated with explicit waits
 by wrapping commonly used functionality in an easy to use API.

Consider this example: You want to use Selenium to log into Github from the 404 page. 
You write a script like this to fill in the login credentials and click the login button:
"""

try:
    driver.get("https://github.com/this/doesntexist")

    username_field = driver.find_element_by_id("login_field")
    username_field.click()
    username_field.send_keys("my_username")

    password_field = driver.find_element_by_id("password")
    password_field.click()
    password_field.send_keys("my_password")

    login_button = driver.find_element_by_css_selector("input.btn-primary")
    login_button.click()

finally:
    driver.quit()

"""
(.venv35) ➜  explicit ✗ python example.py
Traceback (most recent call last):
File "example.py", line 9, in <module>
    username_field = driver.find_element_by_id("login_field")
<...>
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: 
Unable to locate element: {"method":"id","selector":"login_field"}

The reason for the execption, which might not be readily apparent, is that the login modal on that page 
loads in after the page loads. 
When the script runs it attempts to immediately find the field element after control is returned 
from the driver.get call. 
Since the element isn’t in the DOM yet, Selenium throws the NoSuchElementException.
"""