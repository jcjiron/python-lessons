# Findings

Ran `spike_money_precision.py` on 5 cases. Results:

| Amounts | float | Decimal | |
|---|---|---|---|
| `[0.1, 0.2, 0.3]` | 0.6 | 0.6 | match |
| `[10.005, 10.005, 10.005]` | **30.02** | **30.0** | **diverged** |
| `[19.99] × 37` | 739.63 | 739.63 | match |
| `[250.0, 150.0, 99.99, 0.01]` | 500.0 | 500.0 | match |
| `[526.5, 0.1 × 5]` | 527.0 | 527.0 | match |

## Conclusion

They diverge in exactly one case: repeated amounts that land on the
`x.xx5` boundary (`10.005`), because `round()`-ing after every single
addition compounds the rounding error three times in a row. Most
realistic order totals (prices like `19.99`, `250.0`) never hit that
boundary, so they match.

**Decision:** keep `float` + `round(x, 2)` in `Money` (lesson 7) as-is.
The divergence only shows up with contrived half-cent inputs that don't
happen with real prices — switching the whole `Money` class to `Decimal`
would be solving a problem this system doesn't actually have, for the
cost of a less convenient API everywhere `Money` is used.

**If this ever becomes real:** if the business starts pricing things at
exact half-cents, or `Money` starts accumulating hundreds of operations
per value (neither is true today), revisit this spike before switching.

`spike_money_precision.py` stays in the repo only as a record of this
investigation — it is not imported anywhere and should not become a
dependency of real code.
