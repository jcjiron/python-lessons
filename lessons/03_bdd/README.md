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

## Real-world use cases

BDD earns its place once the behavior matters to someone who doesn't read
code:

- **Business rules that change often, dictated by non-engineers.**
  Pricing, tax calculation, discount eligibility, credit approval policy.
  When finance/legal/product ask for a rule change, the `.feature` file is
  the document they can read (and even edit) without touching Python — and
  it's still a real, running test.
- **Checkout / e-commerce flows.** Free-shipping rules, coupons, return
  policies — the classic `behave`/Cucumber use case, since QA (who may not
  code) can write or read the acceptance scenarios directly.
- **Regulatory compliance / audits.** Banking, insurance, healthcare. When
  an auditor asks "how do you know the system does X when Y happens," a
  running Gherkin scenario is living evidence — not a PDF that went stale
  a year ago.
- **Public libraries / SDKs.** The value isn't for you — it's for whoever
  *consumes* your library. Scenarios document the public contract ("this
  is how my calculator behaves from the outside") without exposing the
  implementation. If a change breaks the contract, the scenario fails
  before you publish it. Concrete examples:
  - An internal "business rules" package (e.g. pricing/commission
    calculation) shared across multiple services — web checkout, mobile
    backend, in-store POS — published to a private registry so every
    consumer gets the exact same behavior instead of reimplementing it.
  - A payments SDK (Stripe/PayPal-style): declined cards, retries, 3D
    Secure — the exact behavior promised to whoever integrates it.
  - An authorization/policy engine: "Given a user with role Supervisor,
    when they try to approve an order over $10,000, then access is
    denied" — security behavior that can't be ambiguous.
  - Multi-language SDKs sharing the **same** `.feature` file across
    implementations (Python via `behave`, JS via Cucumber.js, Java via
    Cucumber-JVM) to guarantee identical behavior across every language a
    product ships in.
  - A validation library with legal/fiscal impact (tax ID formats, VAT
    calculation by region) consumed by multiple systems, where behavior
    must be auditable.
- **Bridging manual QA into automation.** When QA already tests by hand
  using "given I do this, then that happens" cases, BDD turns those into
  automated regression almost verbatim — same language, now executable.
- **Rescuing legacy systems with no specs.** Before refactoring undocumented
  code, writing scenarios that capture *current* behavior (however odd)
  means any refactor that breaks it gets caught.

## What to notice

- `behave` matches each `Given/When/Then` line to a decorated function in
  `order_steps.py` by text pattern, and shows you exactly which file/line
  handled it.
- The `{expected}` parser is picky about number formats (`:f` requires a
  decimal point) — that kind of friction only shows up when you actually
  run the tool, not just reading about it.
- The domain code itself didn't change one bit from lesson 2 — only the
  layer describing *what it should do* changed.
