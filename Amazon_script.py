from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/Sanches/Documents/GitHub/Automation/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

driver.find_element_by_id('twotabsearchtextbox'). send_keys('coffee maker')

driver.find_element_by_id ('nav-search-submit-button').click()

actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_result = '"coffee maker"'

assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'

driver.quit()