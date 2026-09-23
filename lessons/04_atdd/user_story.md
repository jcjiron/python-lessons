# User Story: Apply a coupon to an order

**As a** customer
**I want** to apply a discount coupon to my order
**So that** I pay a fair, correctly discounted total before checking out

## Acceptance Criteria

- **AC1:** An order with a total greater than $500 receives an additional 10% discount.
- **AC2:** The coupon `DISCOUNT10` applies a 10% discount, evaluated before the large-order rule (AC1).
- **AC3:** An order with no items cannot be processed — it must be explicitly rejected.

Development does not start until these criteria are agreed on.
