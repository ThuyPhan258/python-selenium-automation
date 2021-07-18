from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    SIZE_TOOLTIP = (By.ID, "a-popover-content-1")
    SIZE_SELECTION_BN = (By.ID, "dropdown_selected_size_name")
    SIZE_OPTION_0 = (By.ID, "native_size_name_0")
    PRICE_BUY_BOX = (By.ID, "priceInsideBuyBox_feature_div")
    COLOR_OPTIONS = (By.CSS_SELECTOR,"variation_color_name li")
    SELECTED_COLOR =(By.CSS_SELECTOR, "variation_color_name .selection")

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def select_size(self):
        self.click(*self.SIZE_SELECTION_BN)
        self.click(*self.SIZE_OPTION_0)
        self.wait_for_element_appear(*self.PRICE_BUY_BOX)

    def verify_can_select_dress_colors(self):
        expected_colors = ['Dark Navy', 'Dusty Rose', 'Black']
        colors = self.find_element(*self.COLOR_OPTIONS)

        for i in range(len(colors)):
            colors[i].click()
            self.verify_text(expected_colors[i], self.SELECTED_COLOR)

    def verify_size_selection_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_TOOLTIP)