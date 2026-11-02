def pipe(value, *functions):
    for fn in functions:
        value = fn(value)
    return value


def partition_by_validity(raw_orders):
    """Stage: split the raw batch into valid orders and rejects."""
    valid = [order for order in raw_orders if order.get("items")]
    invalid = [order for order in raw_orders if not order.get("items")]
    return valid, invalid


def _calculate_order_total(order):
    subtotal = sum(item["price"] * item["quantity"] for item in order["items"])

    if order.get("coupon") == "DISCOUNT10":
        subtotal = round(subtotal * 0.9, 2)
    if subtotal > 500:
        subtotal = round(subtotal * 0.9, 2)

    return subtotal


def calculate_totals(orders):
    """Stage: map each order to a new dict carrying a computed 'total'."""
    return [dict(order, total=_calculate_order_total(order)) for order in orders]


def build_report(orders):
    """Stage: reduce the whole batch down to one aggregate report."""
    return {
        "order_count": len(orders),
        "total_revenue": round(sum(order["total"] for order in orders), 2),
    }


def run_pipeline(raw_orders):
    valid, rejected = partition_by_validity(raw_orders)

    report = pipe(
        valid,
        calculate_totals,
        build_report,
    )
    report["rejected_count"] = len(rejected)
    return report
