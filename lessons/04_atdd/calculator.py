def calculate_total(order, coupon=None):
    if not order.items:
        raise ValueError("Cannot process an order with no items")

    total = sum(product.price * quantity for product, quantity in order.items)

    if coupon == "DISCOUNT10":
        total *= 0.9
    if total > 500:
        total *= 0.9

    return round(total, 2)
