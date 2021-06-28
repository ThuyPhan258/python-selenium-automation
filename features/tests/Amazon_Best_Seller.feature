# Created by thuy at 6/27/21
Feature: Verify 5 links in Amazon BestSellers page
  # Enter feature description here

  Scenario: Open Amazon BestSellers page and verify there are 5 links
    Given Open Amazon BestSellers page
    Then Verify there are 5 links

    Scenario: BestSellers links can be opened
      Given Open Amazon BestSellers page
      Then User can click through top links and verify correct page opened