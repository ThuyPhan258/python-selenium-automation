# Created by thuy at 5/24/21
Feature: Test Help Search
  # Enter feature description here

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon Help Search page
    When Input Cancel order in search help library field
    And Emulate hitting keyboard Enter button
    Then Verify Cancel Items or Orders text worked
