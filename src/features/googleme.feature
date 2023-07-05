# Created by AEvans at 05/07/2023
Feature: Google Me
  Open Google and search for me

  Scenario: Google Me
    Given I open a browser
    And I navigate to www.google.com
    When I enter "Andrew Evans" in the search field
    And I click search
    Then I see the results


