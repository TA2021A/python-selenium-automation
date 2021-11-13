# Created by Sanches at 9/29/21

Feature: Test cases scenario for search functionality

  Scenario: User can search for Cancelling an order on Amazon

    Given Open amazon help page
    When Type Cancel order in search and hit ENTER
    Then Verify Cancel Items or Orders text is present


