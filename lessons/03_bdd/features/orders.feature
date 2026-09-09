Feature: Calculate order total with coupon

  Scenario: Apply discount coupon to a large order
    Given an order with 2 t-shirts at $250 and 1 cap at $150
    When I apply the coupon "DISCOUNT10"
    Then the total should be $526.5

  Scenario: No discount on a small order
    Given an order with 1 cap at $150
    When I don't apply any coupon
    Then the total should be $150
