# Created by thuy at 5/24/21
Feature: Test Amazon Search

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    Then Verify search worked


  Scenario: User can select blouse colors
    Given Open Amazon product B081YS2F7N page
    Then Verify user can click through colors


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias stripbooks
    And Search for Faust
    Then Verify books department is selected