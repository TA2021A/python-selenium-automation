from selenium.webdriver.common.by import By
from behave import when, then


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price')
PRODUCT_NAME = (By.ID, 'productTitle')
CART_COUNT = (By.ID, 'nav-cart-count')


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart count has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART_COUNT).text
    assert actual_count == expected_count, f' Expected {expected_count} item(s) does not match with actual count {actual_count}'


@then('Verify cart has correct product')
def verify_product_name(context):
    cart_product_name = context.driver.find_element(By.XPATH, "//span[@class='a-truncate-cut']").text
    print(f'Product name in cart: {cart_product_name}')
    assert cart_product_name == context.current_product_name
