from money import Money


def calculate_total(order, coupon=None):
    if not order.lines:
        raise ValueError("Cannot process an order with no items")

    total = Money(0)
    for line in order.lines:
        total = total + line.subtotal

    if coupon == "DISCOUNT10":
        total = total.apply_discount(0.10)
    if total.amount > 500:
        total = total.apply_discount(0.10)

    return total
