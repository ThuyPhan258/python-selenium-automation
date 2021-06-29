# Created by thuy at 6/6/21
Feature: Verify number of items in Amazon Cart list

  Scenario: Check the number of items in the cart
    Given User opens Amazon page
    When Click on the amazon search icon
    When Search for pen
    When Click on first product
    When Click on Add to Cart button
    Then Verify cart has 1 item