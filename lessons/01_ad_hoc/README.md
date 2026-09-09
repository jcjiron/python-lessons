# 1️⃣ Ad-hoc / Code-First

## The idea

You write code directly, with no upfront design and no tests. You adjust as
you go, testing manually (running the script and seeing what comes out).
It's the most natural way almost everyone starts programming.

- Zero (or almost zero) automated tests
- Manual debugging: `print()`, run and look
- Fast decisions, guided by intuition
- Everything usually lives in a single file/function

**Good for:** one-off scripts, prototypes, quickly exploring an idea.
**Risk:** as the file grows, you become afraid to touch it — there's no
safety net (tests) to warn you if you broke something.

## The example

`orders.py` solves the whole order system: it calculates an order's total,
applies a discount coupon, checks there's enough stock, and builds the
receipt. All in one file, loose functions, no classes, no tests. Notice how
the business rules (the 10% over $500, the fixed coupon) are mixed directly
into the receipt logic — typical of the ad-hoc style.

Run the example:

```bash
python3 lessons/01_ad_hoc/orders.py
```

## What to notice

- There isn't a single test: to know if it works, you run it and read the
  `print()` output.
- If tomorrow I wanted to add a new coupon or change the 10% threshold, I'd
  edit `calculate_total` directly and cross my fingers.
- It's fast to write — for a one-afternoon script, it's perfect.
