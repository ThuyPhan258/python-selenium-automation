# from selenium.webdriver.common.by import By
# from behave import given, when, then
#
# # @when("Click on first product")
# # def click_first_product(context):
# #     context.app.search_results_page.click_first_product()
#
# @then('Verify search worked for {expected_text}')
# def verify_search_worked(context, expected_text):
#     # actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
#     # expected_result = '"Table"'
#     # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
#     context.app.search_results_page.verify_search_worked(expected_text)