from selenium.webdriver.common.by import By
from behave import then


@then('Verify cart is empty')
def verify_cart_empty(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@id='sc-empty-cart-message']/h2").text
    expected_result = 'Your Amazon Cart is empty'
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'
