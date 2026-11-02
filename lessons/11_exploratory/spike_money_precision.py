# SPIKE -- throwaway exploration, not production code.
# Nothing else in this repo imports this file. Run it, read the output,
# write the conclusion in findings.md, then forget about it.

from decimal import Decimal


def float_money_pipeline(amounts):
    total = 0.0
    for amount in amounts:
        total = round(total + amount, 2)
    return total


def decimal_money_pipeline(amounts):
    total = Decimal("0.00")
    for amount in amounts:
        total = (total + Decimal(str(amount))).quantize(Decimal("0.01"))
    return total


if __name__ == "__main__":
    cases = [
        [0.1, 0.2, 0.3],
        [10.005, 10.005, 10.005],
        [19.99] * 37,  # realistic: lots of small repeated purchases
        [250.0, 150.0, 99.99, 0.01],
        [526.5, 0.1, 0.1, 0.1, 0.1, 0.1],
    ]

    for amounts in cases:
        float_result = float_money_pipeline(amounts)
        decimal_result = float(decimal_money_pipeline(amounts))
        verdict = "MATCH" if float_result == decimal_result else "DIVERGED"
        print(f"{amounts} -> float={float_result} decimal={decimal_result} [{verdict}]")
