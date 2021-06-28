from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.keys import Keys
TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')
HEADER =(By.CSS_SELECTOR, '#zg_banner_text_wrapper')

@given('Open Amazon BestSellers page')
def open_Amazon_BestSellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify there are 5 links')
def verify_5_links(context):
    link_count = context.driver.find_elements(By.CSS_SELECTOR, *TOP_LINKS)
    print('Links count:', len(link_count))
    assert len(link_count) == 5, f'Expected 5 links, but got {len(link_count)}'

@then('User can click through top links and verify correct page opened')
def click_thru_top_link(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'