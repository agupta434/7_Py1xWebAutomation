
Important Library
Selenium
Pytest
Pytest html
Allure Pytest

Logging
xdist - Run parallel execution
openpyxl - read csv and excel

Faker lib for fake data generation

pip install selenium pytest pytest-html allure-pytest

# How to run your Testcase Parallelly 
```pip install pytest-xdist```
```pytest -n auto file.py -s -v```

# pytest.ini
[pytest]
log_cli = 1
log_cli_level = INFO
log_cli_format = %(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)
log_cli_date_format = %Y-%m-%d  %H:%M:%S
###########################

terminal - pytest filepath -s -v

chrome options available at - https://chromedriver.chromium.org/capabilities

Relative X path
//tagname[@attribute='value']
Contains -  
//tagname[contains(@attribute, 'value')]
Contain for partial text
//tagname[contains(text(), 'value')]
Full Text
//tagname[text()='Text of the element')]
Starts-with
//tagname[starts-with(@attribute, 'part of attribute value')]
//img[starts-with(@title, "Flip)]

Use seletorHub to get RelXpath