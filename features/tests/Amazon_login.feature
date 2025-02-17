# Created by thuy at 5/25/21
Feature: Test Amazon Log in
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Logged out user opens Amazon page
    When Click on Orders
    Then Verify Sign in page opened

  Scenario: Sign in page can be opened from Sign In popup
    Given Logged out user opens Amazon page
    When Click Sign In from popup
    Then Verify Sign in page opened

  Scenario: Sign in tooltip appears and disappears
    Given Logged out user opens Amazon page
    Then Verify Sign in popup is clickable
    When Wait for 8 sec
    Then Verify Sign in popup disappears