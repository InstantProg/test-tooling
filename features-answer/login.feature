Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open orange HRM Homepage
    And Enter username "farr_odinaev" and password "farr_121220"
    And Click on login button
    Then User must successfully login to the Dashboard page












  Scenario Outline: Login to OrangeHRM with Multiple parameters
    Given I launch chrome browser
    When I open orange HRM Homepage
    And Enter username "<username>" and password "<password>" and email "<email>"
    And Click on login button
    Then User must successfully login to the Dashboard page


    Examples:
            |username | password | email |
            |admin123 | password1 | admin@gmail.com |
            |farrukh | passwordfar | farrukh.odinaev@kimep.kz |
            |sino | passwordsino | sino@gmail.com
