from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.keys import Keys

@given('Logged out user opens Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Signed out of page')
def signout_check(context):
    nav_text = context.driver.find_element(By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]').text
    expected_nav_text = "Hello, Sign in"
    assert expected_nav_text == nav_text, f'Expected {expected_nav_text}, but got {nav_text}'


@when('Click on Orders')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify Sign in page opened')
def verify_signin_worked(context):
    actual_result = context.driver.find_element(By.CLASS_NAME,'a-spacing-small').text
    expected_result = 'Sign-In'
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
