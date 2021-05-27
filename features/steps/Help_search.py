from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.keys import Keys


@given('Open Amazon Help Search page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input Cancel order in search help library field')
def Input_Cancel_order(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order')

@when('Emulate hitting keyboard Enter button')
def Click_Enter(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)

@then('Verify Cancel Items or Orders text worked')
def verify_cancel_ordrer_worked(context):
    actual_result = context.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div/h1').text
    expected_result = 'Cancel Items or Orders'
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
