from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.keys import Keys

@given('User opens Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('Click on the cart icon')
def click_cart_icon(context):
    # context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count').click()

    CART_ICON = (By.CSS_SELECTOR, '#nav-cart-count')
    context.app.main_page.click(*CART_ICON)

@then('Verify that Your Shopping Cart is empty text worked')
def verify_your_shopping_cart_empty_worked(context):
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, "#sc-active-cart h2").text
    # expected_result = 'Your Amazon Cart is empty'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#sc-active-cart h2")
    context.app.main_page.verify_text("Your Amazon Cart is empty",*EMPTY_CART_TEXT)