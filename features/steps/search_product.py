from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open Amazon product B081YS2F7N page')
def open_amazon_product(context):
    context.driver.get('https://www.amazon.com/dp/B081YS2F7N/')

@then('Verify user can click through colors')
def verify_can_loop_thru_colors(context):
    expected_color = ['Black', 'Blue', 'Burgundy', 'Caramel','Gray', 'Green', 'Khaki', 'Pink', 'Yellow']
    color_options = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

    for i in range(len(color_options)):
        color_options[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text
        assert actual_text == expected_color[i], f'Error, color is {actual_text}, but expected {expected_color[i]}'