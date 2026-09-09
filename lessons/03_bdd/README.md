# 3️⃣ BDD — Behavior-Driven Development

## The idea

Program behavior using business language. Instead of a technical test
(`assertEqual(...)`), you describe the expected behavior as a scenario in
**Given / When / Then**:

- **Given** — the starting context/state
- **When** — the action that happens
- **Then** — the expected result

That scenario is written in near-plain English (Gherkin), readable by
non-programmers — product, QA, business. It's then wired to real Python
code ("step definitions") that executes against your actual system.

**The stop it adds on top of TDD:** in TDD the stop is "write the test
before the code." In BDD the stop is "put the behavior into business
language before you even think about the technical test." If you can't
explain it in Given/When/Then, you probably don't understand the business
rule well enough yet.

**Good for:** teams with constant business↔dev communication, complex
business rules where "what should happen" is easy to get wrong.
**Risk:** verbose specs, or "TDD in disguise" — writing Gherkin just to
check a box, without it actually changing how you think about the problem.

## Two levels of BDD (important distinction)

- **Service-level BDD (what this lesson does):** the steps call the
  domain code directly (`calculate_total(...)`) — same level as TDD, just
  described differently. No `main.py`, no running app — it's still an
  automated test, just written in business language.
- **End-to-end BDD:** the steps drive a real running application (a CLI
  command, an API call, a browser). That needs an actual entry point.
  That's closer to Outside-In Development (lesson 5) and ATDD (lesson 4).

## The example

Reuses `Product`, `OrderBuilder`, and `calculate_total` from lesson 2 —
same domain, no logic duplicated.

- `features/orders.feature` — the behavior, in Given/When/Then
- `features/steps/order_steps.py` — connects that text to the real domain
  code

## Setup

This lesson needs the `behave` package (not in the standard library):

```bash
pip install behave
```

## Running it

```bash
cd lessons/03_bdd
behave
```

You should see both scenarios pass:

```
1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped
```

## What to notice

- `behave` matches each `Given/When/Then` line to a decorated function in
  `order_steps.py` by text pattern, and shows you exactly which file/line
  handled it.
- The `{expected}` parser is picky about number formats (`:f` requires a
  decimal point) — that kind of friction only shows up when you actually
  run the tool, not just reading about it.
- The domain code itself didn't change one bit from lesson 2 — only the
  layer describing *what it should do* changed.
