# Created by Sanches at 10/04/21

Feature: Amazon cart functionality

  Scenario Outline: User can add item in cart
    Given Open amazon page
    When Input <search_word> into Amazon search field
    And Click on search icon
    And Click on the first product
    And Store product name
    And Click on Add to the Cart button
    And Open cart page
    Then Verify cart count has 1 item(s)
    And Verify cart has correct product
    Examples:
      |search_word      |result    |
      |Wallpaper        |"Wallpaper" |




