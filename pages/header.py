from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART = (By.ID, 'nav-cart-count')
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def hover_flag_icon(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def verify_spanish_language_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def select_department(self, alias):
        select = Select(self.find_element(*self.DEPARTMENT_SELECT))
        select.select_by_value(f'search-alias={alias}')
