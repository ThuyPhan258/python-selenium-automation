from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open Amazon T&C page')
def open_Amazon_TermAndCondition(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.driver.current_window_handle

@when('Click on Amazon Privacy Notice link')
def click_Privacy_Notice(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(new_window)

@then('Verify Amazon Privacy Notice page is opened')
def verify_Privacy_Notice_page(context):
    assert 'https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ' in context.driver.current_url, \
        f'URL https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ not in {context.driver.current_url}'

@then('User can close new window')
def close_new_window(context):
    context.driver.close()

@then('Switch back to original url')
def switch_original_url(context):
    context.driver.switch_to_window(context.original_window)
    assert 'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088' in context.driver.current_url, \
        f'URL https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 not in {context.driver.current_url}'
