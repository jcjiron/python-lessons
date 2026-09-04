"""Order system, ad-hoc style: everything loose, no tests, no classes."""

STOCK = {
    "t_shirt": 10,
    "cap": 2,
    "hoodie": 0,
}

PRICES = {
    "t_shirt": 250,
    "cap": 150,
    "hoodie": 600,
}


def calculate_total(items, coupon=None):
    total = 0
    for product, quantity in items.items():
        total += PRICES[product] * quantity

    # business rule mixed in right here, nothing separated
    if coupon == "DISCOUNT10":
        total *= 0.9
    if total > 500:
        total *= 0.9  # another 10% off if the order is big

    return round(total, 2)


def validate_stock(items):
    missing = []
    for product, quantity in items.items():
        if STOCK.get(product, 0) < quantity:
            missing.append(product)
    return missing


def process_order(items, coupon=None):
    missing = validate_stock(items)
    if missing:
        print(f"Cannot process order: out of stock for {missing}")
        return None

    total = calculate_total(items, coupon)
    print("--- Receipt ---")
    for product, quantity in items.items():
        print(f"{product} x{quantity} = ${PRICES[product] * quantity}")
    print(f"TOTAL: ${total}")
    return total


if __name__ == "__main__":
    process_order({"t_shirt": 2, "cap": 1}, coupon="DISCOUNT10")
    print()
    process_order({"hoodie": 1})
