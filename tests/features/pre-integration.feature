@pre_integration
Feature: Pre-Integration Testing
  Ensure that localstack is running a test input data is present.

  Scenario: Setup Entry Criteria
    Given localstack has started
    When localstack is ready
    Then transfer input data

