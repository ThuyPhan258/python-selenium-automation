# Created by thuy at 6/01/21
Feature: Your Shopping Cart is empty
  # Enter feature description here

  Scenario: User can see Your Shopping Cart is empty
    Given User opens Amazon page
    When Click on the cart icon
    Then Verify that Your Shopping Cart is empty text worked
