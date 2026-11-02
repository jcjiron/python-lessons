# 8️⃣ Functional-First Programming

## The idea

Prefer pure functions over objects with behavior. Three principles:

- **Immutability** — never change something that already exists; if you
  need a different version, you return a **new** one.
- **Composition** — build complex behavior by chaining small functions,
  not by inheriting or calling methods on an object.
- **Minimal side effects** — a function takes data, returns data, and
  touches nothing else (no printing, no mutating outside variables, no
  hidden state).

## The stop it adds

You resist reaching for a class with internal mutable state — like
lesson 7's `OrderBuilder`, which accumulates `self._lines` with
`.append`. Instead, every "add an item" operation returns a **different**
order, leaving the original untouched.

**Good for:** concurrency (nothing shared gets mutated, so nothing can
get corrupted between threads), complex logic made of many chainable
rules.
**Risk:** mental overhead if you're coming from OOP, and friction if the
rest of the system (a UI, a database layer) genuinely expects
stateful objects.

## Running it

No extra install — standard library `unittest`:

```bash
cd lessons/08_functional
python3 -m unittest test_order_functions -v
```

## The example

- `models.py` — `Product` and `Line` are plain `namedtuple`s. No methods,
  no behavior — just data.
- `order_functions.py`:
  - `add_item(order, product, quantity)` returns a **new** tuple; it never
    mutates the `order` passed in.
  - `line_subtotal`, `order_subtotal`, `apply_coupon`,
    `apply_large_order_rule` — small pure functions, each doing one thing.
  - `pipe(value, *functions)` — explicit composition: runs `value` through
    each function in sequence. `calculate_total` is built by composing
    the smaller functions through `pipe`, not by writing one big method.

## What to notice

- `test_add_item_does_not_mutate_the_original_order` is the whole point:
  after building `order_b` from `order_a`, `order_a` still has exactly the
  lines it started with. Compare this to lesson 7's `OrderBuilder`, where
  `add_item` mutates `self._lines` in place.
- `calculate_total` is four lines, all plumbing — `pipe` passing one pure
  function's output into the next. None of the actual rules live there;
  they live in the small functions being composed.
- Nothing here prints, logs, or touches anything outside its own
  arguments and return value — contrast with lesson 1's `orders.py`,
  where `process_order` both calculates **and** prints in the same
  function.
