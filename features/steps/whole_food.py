from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BEST_DEAL_ITEMS = (By.CSS_SELECTOR,".s-result-list .s-result-item .s-item-container .a-section.a-padding-extra-large:not(.a-text-center)")
PRODUCT_NAME = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name")

from selenium.webdriver.common.keys import Keys
@given('Open Amazon wholefoods page')
def open_amazon_wholefoods_page(context):
    context.driver.get('https://amazon.com/wholefoodsdeals')

@then('Verify that wholefood products have regular price and names')
def verify_best_deal(context):
    best_deal_items = context.driver.find_elements(*BEST_DEAL_ITEMS)
    #go thru every web element
    for e in best_deal_items:
        #verify regular
        assert 'Regular' in e.text, f'Expected Regular price not found in {e.text}'
        #verify name
        product_name = e.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, f'Product name if missing'

#element = driver.find_element(By.ID, '')
#element.find_element(