from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Input {search_word} in search field')
def search_amazon(context, search_word):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Table')
    context.app.header.input_search('Table')
    context.app.header.input_search('coffee mug')


@when('Click on amazon search icon')
def click_search(context):
    #context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.header.click_search()

@then('Verify search worked')
def verify_search_worked(context):
    # actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    # expected_result = '"Table"'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    context.app.search_results_page.verify_search_worked()