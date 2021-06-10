from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.keys import Keys

@given('Open Amazon webpage')
def open_amazon_webpage(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on the amazon search icon')
def click_search(context):
     context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@when('Search for {product_name}')
def search_for_product(context, product_name):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(product_name, Keys.ENTER)

@when('Click on first product')
def click_first_product(context):
    links = context.driver.find_elements(By.XPATH,"//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']/a")
    links[0].click()

@when('Click on Add to Cart button')
def click_Add_to_Cart(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID,'add-to-cart-button').click()

@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    context.driver.implicitly_wait(15)
    expected_count = 1
    items_count = context.driver.find_element(By.ID, 'nav-cart-count').text
    print('Items in cart count:', items_count)
    assert items_count == str(expected_count), f'Expected {expected_count}, but got {items_count}'
