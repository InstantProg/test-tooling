Feature: Calculator
  This will be a simple python script
  that will do calculation

  Scenario: Adding two numbers
    Given I have entered 100 and 120 into the calculator
    When I press add
    Then the result should be 120 on screen