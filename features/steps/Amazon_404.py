from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

@given('Open Amazon product INVALID_B081YS2F7N page')
def open_invalid_page(context):
    context.driver.get('https://www.amazon.com/B081YS2F7N')


@when('Store original window')
def store_window(context):
    original_window = context.driver.current_window_handle

@when('Click on the dog image')
def click_dog_image(context):
    context.driver.find_element(By.CSS_SELECTOR, "img#d").click()

@when('Switch to new window')
def switch_windown(context):
    context.driver.wait.until(EC.new_window_is_opened)

    new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(new_window)

@when('Return to original window')
def return_original_window(context):
    context.driver.switch_to_window(context.original_window)

@then('Verify Amazon url')
def verify_Amazon__base_url(context):
    assert 'https://www.amazon.com/' in context.driver.current_url,\
        f'URL https://www.amazon.com/ not in {context.driver.current_url}'

@then('Verify Amazon Blog url')
def verify_Amazon_Blog_url(context):
    assert 'https://www.aboutamazon.com/' in context.driver.current_url,\
        f'URL https://www.aboutamazon.com/ not in {context.driver.current_url}'

@then('Close new window')
def close_window(context):
    context.driver.close()