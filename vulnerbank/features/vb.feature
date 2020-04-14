Feature: Data tampering

  Scenario: Access unauthorised account

    Given an attacker
    When I try to access to an unauthorised account
    Then I should have no access to that account

