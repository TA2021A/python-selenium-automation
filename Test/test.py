from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep

# init driver
driver = webdriver.WebDriver(executable_path='/Users/Sanches/Documents/GitHub/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()


ADD_TO_CART = (By.ID, 'add-to-cart-button')

# open the url
driver.get('https://www.amazon.com/Organic-Valley-Whole-Stable-Resealable/dp/B08ZZSW8MF/ref=sr_1_1_sspa?crid=1KSU3E5ANIKSR&dchild=1&keywords=milk&qid=1635899891&sprefix=milk%2Caps%2C99&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFJOFVEMk1VSVVJQjgmZW5jcnlwdGVkSWQ9QTA3MTM0NTYyRFhDSVNRM0NSR1ZGJmVuY3J5cHRlZEFkSWQ9QTA0Mzc2NTFUWTlMSjVZVVFCSTkmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl')

# click
driver.find_element(*ADD_TO_CART).click()






