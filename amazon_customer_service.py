from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.amazon.com/gp/help/customer/display.html')
large_container = driver.find_elements(By.CSS_SELECTOR, '.ss-landing-container-wide .ss-rich-card-column')
help_search = driver.find_element(By.ID, "helpsearch")
Browser_Help_Topics = driver.find_element(By.CSS_SELECTOR, ".help-content .csg-header h1")
Recommended_Topics = driver.find_elements(By.CSS_SELECTOR, "category-section")


driver.quit()
