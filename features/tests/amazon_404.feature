# Created by huy at 6/22/21
Feature: Test for 404 page

  Scenario: 404 page tales to Amazon Blog
    Given Open Amazon product INVALID_B081YS2F7N page
    When Store original window
    When Click on the dog image
    When Switch to new window
    Then Verify Amazon Blog url
    Then Close new window
    When Return to original window
    Then Verify Amazon url
