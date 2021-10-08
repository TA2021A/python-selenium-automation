from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/chromedriver')


driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')



driver.find_element(By.XPATH, "//div[@id='sc-empty-cart-message'] /h2").text





"""
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']").click()


driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox').send_keys('Cancel order', Keys.ENTER)

"""








