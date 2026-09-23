# 5️⃣ Outside-In Development

## The idea

You start from the layer the user/consumer touches (UI, API, CLI) and push
inward. It's the opposite of how lessons 2-4 were built — those started
from the domain (`Product`, `calculate_total`) and never had an outer
layer at all. This is where a `main.py` finally shows up.

**The stop it adds:** you don't let yourself jump straight into the
"interesting" business logic. You first define how the real entry point
looks and behaves — even while the inside is still empty — using **test
doubles** (fakes/mocks) to stand in for the domain that doesn't exist yet.
Only once the outer contract is proven do you work inward, replacing the
fake with the real thing.

**Good for:** web apps, APIs — anything where the contract with the
consumer matters more than the internal details.
**Risk:** bloated outer layers — if you linger too long in the CLI/API
without descending into the domain, you end up with a lot of "facade"
code and little real logic behind it.

## Running it

No extra install — standard library `unittest`:

```bash
cd lessons/05_outside_in
python3 -m unittest test_main -v
```

Run the CLI directly:

```bash
python3 main.py --item t_shirt:2 --item cap:1 --coupon DISCOUNT10
```

## The example

- `main.py` — the CLI: parses `--item name:quantity` (repeatable) and
  `--coupon`, builds the receipt text. `run()` takes `calculate_total_fn`
  as a parameter (defaulting to the real one), so the outer layer can be
  tested independently of the domain underneath it.
- `product.py`, `order.py`, `order_builder.py`, `calculator.py` — same
  domain as lessons 2/4, reused as-is.
- `test_main.py` — two stages:
  - `TestCliWithFakeCalculator`: proves the CLI parses arguments and
    formats the receipt correctly, using a **fake** `calculate_total_fn`
    that returns a hardcoded number. This test would pass even if
    `calculator.py` were broken or didn't exist yet.
  - `TestCliWithRealCalculator`: the same CLI, now wired to the real
    domain — proving the full path end to end.

## What to notice

- The CLI test (`TestCliWithFakeCalculator`) never imports `calculator`
  logic — it injects a fake function instead. That's the Outside-In
  move: build and trust the outer contract first, independent of whether
  the inside is real yet.
- Compare this to lessons 2-4: there, the domain came first and nothing
  ever called it from a real entry point. Here the entry point came
  first, and the domain got plugged in afterward.
- Lesson 6 (Inside-Out) does the opposite: domain first, outer layer
  last — closer in spirit to how lessons 2-4 were actually built.
