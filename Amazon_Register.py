from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=9SP8DSJFQDJW36NRCBFH&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

amazon_logo = driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
create_account_text = driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small')
your_name = driver.find_element(By.CSS_SELECTOR,'input#ap_customer_name').send_keys('thuyphan')
email = driver.find_element(By.CSS_SELECTOR,'input#ap_email').send_keys('thuyphan222@gmail.com')
password = driver.find_element(By.CSS_SELECTOR,'input#ap_password').send_keys('123456789')
re_password = driver.find_element(By.CSS_SELECTOR,'input#ap_password_check').send_keys('123456789')
create_account_button = driver.find_element(By.CSS_SELECTOR,'input#continue').click()
driver.back()

condition_of_use = driver.find_element_by_css_selector("a[href*='condition_of_use']").click()
driver.back()
privacy_notice = driver.find_element_by_css_selector("a[href*='privacy_notice']").click()
driver.back()
Sign_in_link = driver.find_element_by_css_selector('a.a-link-emphasis').click()

driver.quit()
