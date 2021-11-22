from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price')
PRODUCT_NAME = (By.ID, 'productTitle')
CART_COUNT = (By.ID, 'nav-cart-count')


# init driver
driver = webdriver.Chrome(executable_path='/Users/Sanches/Documents/GitHub/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get('https://www.amazon.com')


element = driver.find_element(*SEARCH_FIELD)
element.send_keys("dumbell")
element.submit()


driver.find_element(*SEARCH_ICON).click()


driver.find_element(*PRODUCT_PRICE).click()


driver.find_element(*ADD_TO_CART).click()


driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


dumbell = driver.find_element(By.XPATH, "//span[@class='a-truncate-cut']").text
print(dumbell)






















