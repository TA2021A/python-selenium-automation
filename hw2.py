from selenium.webdriver.common.by import By

"""Amazon logo"""

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

"""Continue button"""

driver.find_element(By.ID, 'continue')

"""Need help link"""

driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

"""Forgot your password link"""

driver.find_element(By.ID, 'auth-fpp-link-bottom')

"""Other issues with Sign-In link"""

driver.find_element(By.ID, 'ap-other-signin-issues-link')

"""Create your Amazon account button"""

driver.find_element(By.ID, 'createAccountSubmit')

"""Conditions of use link"""

driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']")

"""Privacy Notice link"""

driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&nodeId=468496']")


"""Test case for Help search using python & selenium script"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users/Sanches/Documents/GitHub/Automation/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/gp/help/customer/display.html')

element = driver.find_element_by_id("helpsearch")
element.send_keys("Cancel order")
element.submit()

actual_result = driver.find_element(By.XPATH, "//a[@class='a-link-normal']").text
expected_result = 'Cancel Items or Orders'

assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'

driver.quit()






