# Created by Sanches at 10/04/21

Feature: # Amazon bestsellers links functionality

  Scenario: # User can see 5 links
    Given Open amazon page first
    When  Open "Best Sellers" tab
    Then  Verify 5 links exist





