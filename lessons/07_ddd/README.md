# 7️⃣ DDD — Domain-Driven Design

## The idea

The domain is the center of the system. Before writing code, you build a
**ubiquitous language** (a vocabulary agreed with the business) and
classify each concept:

- **Entity** — has its own identity that persists even as its data
  changes (an `Order` is still "the same order" whether or not its lines
  change — what matters is its id).
- **Value Object** — defined purely by its value, no identity of its own,
  interchangeable (`Money(250)` is equal to any other `Money(250)`).

## The stop it adds

Before touching code, you write the glossary and decide, explicitly,
what's an Entity and what's a Value Object — you don't leave it to
intuition while coding. This is the exact question you already asked
yourself back in lesson 2, without a name for it: "Product vs. Item,
which is which?" DDD just gives that pause a formal name.

**Good for:** large, long-lived systems, where the domain grows and a
loose tuple or float becomes ambiguous.
**Risk:** for a system as small as ours, all this ceremony is more than
it needs — that's exactly why lessons 2-6 worked fine without any of it.

## Running it

No extra install — standard library `unittest`:

```bash
cd lessons/07_ddd
python3 -m unittest discover -s . -p "test_*.py" -v
```

## The example

- `glossary.md` — the ubiquitous language, written **first**: `Order` is
  an Entity, `Money` and `OrderLine` are Value Objects.
- `money.py` — `Money`, a Value Object. Equality by value (`Money(250) ==
  Money(250)` even though they're different instances), plus `+` and
  `apply_discount`.
- `order_line.py` — `OrderLine`, a Value Object. This is exactly the
  `ItemPedido` that got rejected in lesson 2 as YAGNI — no test demanded
  it back then. Here, the ubiquitous language demands it: the business
  talks about "order lines," not tuples.
- `order.py` — `Order`, now an **Entity** with an `order_id`. Two orders
  with the same id are the same order even with different lines; two
  orders with different ids are different even with identical lines.
- `order_builder.py`, `calculator.py` — same shape as lessons 2/4, now
  built from `order_id` + `OrderLine`s and returning `Money` instead of a
  raw float.

## What to notice

- `test_order.py` tests identity, not content — that's the whole point of
  an Entity. `test_money.py` tests value equality — the whole point of a
  Value Object. Different kinds of objects get tested for different
  things.
- `calculate_total` now returns a `Money`, not a `float` — the domain
  concept ("an amount of money") is explicit in the return type instead
  of being just a number that happens to represent currency.
- Compare the amount of ceremony here to lesson 2's `calculate_total`
  returning a plain `float` from a plain tuple list — both are "correct,"
  but DDD's version scales better as more money-related rules
  (currencies, taxes, refunds) get added later.
