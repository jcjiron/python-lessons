# Ubiquitous Language Glossary

Written and agreed before any code — the DDD stop.

| Term | Classification | Definition |
|------|----------------|------------|
| **Order** | Entity | Has an `order_id`. Two orders are the *same order* if their id matches, even if their lines later change. Not the same order just because the lines happen to match. |
| **OrderLine** | Value Object | A product + a quantity, on one order. No identity of its own — defined entirely by its values. |
| **Money** | Value Object | An amount. Two `Money` instances with the same amount are interchangeable — equal, not "the same instance". |
| **Product** | *(kept simple here)* | Has a name and a price. In a fuller model this would be its own Entity (a catalog item with an id, price history, etc.) — out of scope for this lesson. |

This glossary is what gets negotiated with the business before writing
`order.py` or `money.py` — not after.
