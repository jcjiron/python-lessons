# 4️⃣ ATDD — Acceptance Test-Driven Development

## The idea

Acceptance criteria drive development. Before writing a single line of
code, you sit down with whoever owns the requirement (product, business,
customer) and agree, in writing, on exactly what "done" means.

**The stop it adds:** development doesn't start until the acceptance
criteria exist and are agreed on. If the criteria are unclear, the ticket
isn't ready to be coded — it goes back, it doesn't get guessed at.

**Good for:** close collaboration with a PO/UX, features where "what does
done mean" is easy to get wrong if it isn't written down.
**Risk:** if getting that agreement turns bureaucratic or slow, it becomes
the bottleneck instead of the safety net.

## Running it

No extra install — standard library `unittest`:

```bash
cd lessons/04_atdd
python3 -m unittest test_acceptance -v
```

You should see all 3 acceptance criteria pass.

## The example

- `user_story.md` — the agreement: user story + 3 acceptance criteria
  (AC1, AC2, AC3), written **before** any code existed.
- `product.py`, `order.py`, `order_builder.py` — same domain as lesson 2.
- `calculator.py` — `calculate_total`, extended with AC3's rejection rule
  (raises `ValueError` on an empty order — new, since lesson 2 never
  covered that case).
- `test_acceptance.py` — one test per AC, named `test_ac1_...`,
  `test_ac2_...`, `test_ac3_...`. Each test traces directly back to a line
  in `user_story.md` — that traceability is the point of ATDD, not the
  Given/When/Then phrasing (that's BDD's job, lesson 3).

## What to notice

- Compared to lesson 2/3, nothing here is exploratory — every test exists
  because a specific, pre-agreed criterion demanded it. There's no test
  for a case nobody asked about.
- AC3 forced a real code change (the empty-order check) that didn't exist
  before — it wasn't invented while coding, it came from the acceptance
  agreement itself.
- If a new acceptance criterion shows up later, the flow is: update
  `user_story.md` first, then add the matching `test_ac4_...`, then code.
  Never the other way around.
