from selenium.webdriver.common.by import By
from behave import given, when


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price')
PRODUCT_NAME = (By.ID, 'productTitle')
CART_COUNT = (By.ID, 'nav-cart-count')

@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input {search_word} into Amazon search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_FIELD)
    search.clear()
    search.send_keys(search_word)

@when ('Click on search icon')
def search_icon(context):
   icon = context.driver.find_element(*SEARCH_ICON)
   icon.click()

@when ('Click on the first product')
def first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()

@when ('Store product name')
def store_product_name(context):
    context.current_product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.current_product_name}')


@when ('Click on Add to the Cart button')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()





    





































