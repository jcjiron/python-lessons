# Spike notes

**Question:** `Money` (lesson 7) uses `float` + `round(x, 2)`. Is that
good enough for this system's scale, or should it use `Decimal` instead
to avoid floating-point rounding errors?

**Why this matters now:** `test_rounds_to_two_decimals` in lesson 7
already hinted at float weirdness (`Money(10.005)`). Before deciding to
rewrite `Money` around `Decimal` everywhere, spike it: run both
approaches side by side on a handful of realistic cases and see if they
actually diverge in a way that matters.

**Ground rules for this spike:**
- `spike_money_precision.py` is throwaway. It has no tests, no
  docstrings beyond a warning, and nothing else in this repo imports it.
- The goal is learning, not shipping. Run it, read the output, write the
  conclusion in `findings.md`, and consider the code disposable the
  moment that's done.
