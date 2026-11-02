from models import Line


def pipe(value, *functions):
    for fn in functions:
        value = fn(value)
    return value


def empty_order():
    return ()


def add_item(order, product, quantity):
    """Returns a NEW order. Never touches the one passed in."""
    return order + (Line(product, quantity),)


def line_subtotal(line):
    return line.product.price * line.quantity


def order_subtotal(order):
    return sum(line_subtotal(line) for line in order)


def apply_coupon(total, coupon):
    if coupon == "DISCOUNT10":
        return round(total * 0.9, 2)
    return total


def apply_large_order_rule(total):
    if total > 500:
        return round(total * 0.9, 2)
    return total


def calculate_total(order, coupon=None):
    if not order:
        raise ValueError("Cannot process an order with no items")

    return pipe(
        order,
        order_subtotal,
        lambda total: apply_coupon(total, coupon),
        apply_large_order_rule,
    )
