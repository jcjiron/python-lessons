import argparse

from calculator import calculate_total
from loyalty import calculate_loyalty_points
from order_builder import OrderBuilder
from product import Product

PRICES = {
    "t_shirt": 250,
    "cap": 150,
    "hoodie": 600,
}


def parse_items(item_args):
    items = []
    for entry in item_args:
        name, quantity = entry.split(":")
        items.append((name, int(quantity)))
    return items


def build_order(items, prices):
    builder = OrderBuilder()
    for name, quantity in items:
        builder.add_item(Product(name, price=prices[name]), quantity)
    return builder.build()


def build_receipt(items, total, loyalty_points):
    lines = ["--- Receipt ---"]
    for name, quantity in items:
        lines.append(f"{name} x{quantity}")
    lines.append(f"TOTAL: ${total}")
    lines.append(f"Loyalty points earned: {loyalty_points}")
    return "\n".join(lines)


def run(item_args, coupon, calculate_total_fn=calculate_total, prices=PRICES):
    items = parse_items(item_args)
    order = build_order(items, prices)
    total = calculate_total_fn(order, coupon=coupon)
    loyalty_points = calculate_loyalty_points(total)
    return build_receipt(items, total, loyalty_points)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Calculate an order's total from the command line."
    )
    parser.add_argument(
        "--item",
        action="append",
        required=True,
        metavar="name:quantity",
        help="e.g. --item t_shirt:2 (repeatable)",
    )
    parser.add_argument("--coupon", default=None)
    args = parser.parse_args(argv)

    print(run(args.item, args.coupon))


if __name__ == "__main__":
    main()
