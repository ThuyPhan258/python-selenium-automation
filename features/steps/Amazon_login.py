from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

@given('Logged out user opens Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('Click on Orders')
def click_search(context):
    ORDER_LINK = (By.ID, 'nav-orders')

    # orders_link = context.driver.find_element(By.ID, 'nav-orders')
    # print(orders_link)
    # orders_link.click()
    context.app.main_page.click(*ORDER_LINK)

@when('Click Sign In from popup')
def click_sign_in_btn(context):
    sign_in_btn = context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#nav-signin-tooltip .nav-action-inner')))
    sign_in_btn.click()

@then('Verify Sign in page opened')
def verify_signin_opened(context):
    # actual_result = context.driver.find_element(By.CLASS_NAME,'a-spacing-small').text
    # expected_result = 'Sign-In'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

    Sign_in_Text = (By.CLASS_NAME,'a-spacing-small')
    context.app.main_page.verify_text("Sign-In",*Sign_in_Text)

@then('Verify Sign in popup is clickable')
def verify_sign_in_popup_clickable(context):
     context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#nav-signin-tooltip .nav-action-inner')))

@when('Wait for {sec_count} sec')
def sleep_8sec(context, sec_count):
    sleep(int(sec_count))

@then('Verify Sign in popup disappears')
def verify_signin_popup_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')))