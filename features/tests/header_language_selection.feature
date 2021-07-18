# Created by huy at 7/14/21
Feature: Language selection tests

  Scenario: User can see Spanish language option
    Given Open Amazon page
    When Move mouse over flag icon
    Then Spanish language selection is visible
