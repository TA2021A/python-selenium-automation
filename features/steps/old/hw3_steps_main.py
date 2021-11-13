from selenium.webdriver.common.by import By
from behave import given, when


@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, "nav-cart").click()
