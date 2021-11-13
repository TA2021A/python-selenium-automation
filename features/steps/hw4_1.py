from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep


PRODUCT_LINKS = (By.CSS_SELECTOR, "div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li'")
BEST_SELLER_TAB = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")


@given('Open amazon page first')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Open "Best Sellers" tab')
def best_seller_tab(context):
    context.driver.find_element(*BEST_SELLER_TAB).click()


@then('Verify {links_number} links exist')
def verify_lin_count(context, links_number):
    links = context.driver.find_elements(*PRODUCT_LINKS)
    print('\nFOUND ELEMENTS  ID:\n')
    print(links)
    print('\nFOUND ELEMENTS TEXT:\n')
    for l in links:
        print(l.text)
    assert len(links) == int(links_number), f'Expected {links_number} but got {len(links)}'
