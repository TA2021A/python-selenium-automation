from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/Sanches/Documents/GitHub/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

PRODUCT_LINKS = (By.CSS_SELECTOR, "div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li'")
BEST_SELLER_TAB = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")

driver.get('https://www.amazon.com/')


driver.find_element(*BEST_SELLER_TAB).click()


links = driver.find_elements(*PRODUCT_LINKS)
print(links)
assert len(links) == 5, f'Expected 5 links, but got {len(links)}'

for l in links:
    print(l.text)

driver.quit()


















