# Created by thuy at 5/25/21
Feature: Test Amazon Log in
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Logged out user opens Amazon page
    When Signed out of page
    And Click on Orders
    Then Verify Sign in page opened
