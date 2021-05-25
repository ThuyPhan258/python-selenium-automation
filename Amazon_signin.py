from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

amazon_logo = driver.find_element(By.CLASS_NAME, 'a-icon.a-icon-logo')
continue_button = driver.find_element(By.ID, 'continue').click()
need_help_link = driver.find_element(By.CLASS_NAME, 'a-expander-prompt').click()
forgot_password_link = driver.find_element(By.ID, 'auth-fpp-link-bottom')
other_issue_link = driver.find_element(By.ID, 'ap-other-signin-issues-link').click()
create_your_amazon_account = driver.find_element(By.ID, 'createAccountSubmit')

driver.quit()
