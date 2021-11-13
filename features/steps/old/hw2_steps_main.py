from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys



@given('Open amazon help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Type Cancel order in search and hit ENTER')
def search_order_enter(context):
   context.driver.find_element_by_id('helpsearch').send_keys('Cancel order', Keys.ENTER)


@then('Verify Cancel Items or Orders text is present')
def verify_order(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_result = 'Cancel Items or Orders'
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'


