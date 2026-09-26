# 6️⃣ Inside-Out Development

## The idea

You start from the core domain and build outward. Infrastructure and UI
come last. It's the mirror image of lesson 5: there, the CLI came first
(tested against a fake calculator) and the domain was wired in afterward.
Here, a brand-new domain piece gets built and fully tested completely on
its own, with no interface at all — and only at the very end does it touch
the CLI.

**The stop it adds:** you resist the urge to hook up something visible
right away just to feel progress. You make the domain piece solid and
well-tested in isolation first, trusting that once you finally connect it
to an interface, it'll work the first time because it's already solid.

**Good for:** stable, complex domains — where the business rules are the
hard part and the interface is comparatively trivial.
**Risk:** slow feedback — since nothing outside gets connected until the
end, you can go a long time before discovering the domain doesn't actually
fit how it'll really be used (the opposite problem from lesson 5).

## Running it

No extra install — standard library `unittest`:

```bash
cd lessons/06_inside_out
python3 -m unittest discover -s . -p "test_*.py" -v
```

Run the CLI directly:

```bash
python3 main.py --item t_shirt:2 --item cap:1 --coupon DISCOUNT10
```

## The example

New domain piece: **loyalty points** — 1 point per $50 spent.

- `loyalty.py` — `calculate_loyalty_points(total)`. A pure function: takes
  a number, returns a number. No `Order`, no CLI, no dependency on
  anything else in the lesson.
- `test_loyalty.py` — 5 tests covering zero, just-under-the-threshold,
  exactly-at-the-threshold, a partial/rounding case, and a large total.
  All of this passes with **zero** interface in existence.
- `main.py` — only after `loyalty.py` was solid did it get one new line:
  `calculate_loyalty_points(total)` feeding an extra line in the receipt.
- `test_main.py` — one new test (`test_receipt_includes_loyalty_points...`)
  proving the wiring, not the logic — the logic was already proven in
  `test_loyalty.py`.

## What to notice

- Compare the size of the change in `main.py` (two lines) to the size of
  `test_loyalty.py` (5 thorough tests). Almost all the effort went into
  the domain, none into the interface — the opposite ratio from lesson 5,
  where the CLI mechanics were the thing being tested with a fake domain.
- If `loyalty.py` had a bug, `test_loyalty.py` would have caught it before
  `main.py` ever existed. Lesson 5's approach catches CLI/domain mismatches
  early; this approach catches domain bugs early — different blind spots,
  same underlying discipline.
- Same two lessons, same discipline (TDD-style tests), opposite direction
  — proof that Outside-In/Inside-Out is a separate axis from
  Ad-hoc/TDD/BDD/ATDD, not a stricter version of it.
