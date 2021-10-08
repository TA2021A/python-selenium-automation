from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/chromedriver')

driver.get('https://www.amazon.com/gp/help/customer/display.html')

element = driver.find_element_by_id("helpsearch")
element.send_keys("Cancel order")
element.submit()

actual_result = driver.find_element(By.XPATH, "//a[@class='a-link-normal']").text
expected_result = 'Cancel Items or Orders'

assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'





