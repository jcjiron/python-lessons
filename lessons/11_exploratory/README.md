# 1️⃣1️⃣ Exploratory / Spike-Driven Development

## The idea

Learn by coding experiments. The code is disposable — the point isn't to
ship it, it's to answer a question you can't answer by just thinking
about it. You write it fast, run it, read what happened, write down the
conclusion, and the code itself is forgettable.

## The stop it adds

This one is the opposite kind of stop from every other lesson: instead
of "write a test first" or "agree on criteria first," the stop is
**"don't let this leak into real code."** You explicitly mark the
exploration as throwaway *before* writing it, so nobody — including you,
next week — mistakes it for production code.

**Good for:** new technologies, uncertain questions you could debate
forever but can resolve in five minutes by actually running something.
**Risk:** experimental code leaking into production — the spike script
quietly becomes a dependency, or its shortcuts (no tests, no error
handling) ship as-is because "it already works."

## Running it

No extra install:

```bash
cd lessons/11_exploratory
python3 spike_money_precision.py
```

## The example

The real question: lesson 7's `Money` uses `float` + `round(x, 2)`.
`test_rounds_to_two_decimals` already hinted at float weirdness
(`Money(10.005)`) — is that a real problem, or does it not matter at this
system's scale?

- `spike_notes.md` — the question, written down **before** the code, plus
  the explicit "this is throwaway" ground rules.
- `spike_money_precision.py` — runs the same amounts through a
  `float`-based pipeline and a `Decimal`-based one, side by side. No
  tests, no docstring beyond the throwaway warning — that's deliberate.
- `findings.md` — what actually happened when it ran, and the decision
  that came out of it: keep `float` in `Money`, the divergence only shows
  up on contrived half-cent inputs real prices don't hit.

## What to notice

- This is the only lesson with no `test_*.py` file. That's not an
  oversight — a spike isn't held to the same bar as real code, because
  it's never meant to outlive the question it answers.
- The actual value of this lesson isn't the script — it's
  `findings.md`. The code gets thrown away; the decision and its
  reasoning are what should survive.
- Compare this to lesson 1 (Ad-hoc): both skip tests, but Ad-hoc intends
  the code to become the real system, while a Spike never does. Same
  lack of rigor, completely different intent — that distinction is the
  whole lesson.
