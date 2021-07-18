from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_RESULTS = (By.XPATH, "//a[@class='a-link-normal a-text-normal']")
    BOOKS_SUBNAV =(By.CSS_SELECTOR,"#nav-subnav[data-category='books']")

    def verify_search_worked(self):
       self.verify_text('Table', *self.SEARCH_RESULT)

    def click_first_product(self):
        e = self.find_elements(*self.PRODUCT_RESULTS)
        e[0].click()

    def verify_books_department(self):
        self.wait_for_element_appear(*self.BOOKS_SUBNAV)