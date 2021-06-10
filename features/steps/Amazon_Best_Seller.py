from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.keys import Keys

@given('Open Amazon BestSellers page')
def open_Amazon_BestSellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify there are 5 links')
def verify_5_links(context):
    link_count = context.driver.find_elements(By.CSS_SELECTOR, '#zg_tabs li')
    print('Links count:', len(link_count))
    assert len(link_count) == 5, f'Expected 5 links, but got {len(link_count)}'
