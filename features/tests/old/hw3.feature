# Created by Sanches at 9/29/21

Feature: Test cases scenario for empty cart functionality

  Scenario: Amazon Cart is empty when user click on cart icon
    Given Open amazon page
    When Click on the cart icon
    Then Verify cart is empty