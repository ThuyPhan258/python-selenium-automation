from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.keys import Keys

@given('User opens Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count').click()


@then('Verify that Your Shopping Cart is empty text worked')
def verify_your_shopping_cart_empty_worked(context):
    actual_result = context.driver.find_element(By.XPATH, '//*[@id="sc-empty-cart-message"]/h2').text
    expected_result = 'Your Amazon Cart is empty'
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
