def _calculate_order_total(payload):
    subtotal = sum(item["price"] * item["quantity"] for item in payload["items"])

    if payload.get("coupon") == "DISCOUNT10":
        subtotal = round(subtotal * 0.9, 2)
    if subtotal > 500:
        subtotal = round(subtotal * 0.9, 2)

    return subtotal


def make_calculate_total_handler(receipts):
    """Reacts to OrderPlaced by computing and storing the total.
    Has no idea who else is listening for the same event."""

    def handler(payload):
        receipts[payload["order_id"]] = _calculate_order_total(payload)

    return handler


def make_update_stock_handler(stock_log):
    """Reacts to OrderPlaced by logging what should be decremented from
    stock. Completely independent of the total calculation."""

    def handler(payload):
        for item in payload["items"]:
            stock_log.append((item["product"], item["quantity"]))

    return handler


def make_send_confirmation_handler(notifications):
    """Reacts to OrderPlaced by recording a confirmation message."""

    def handler(payload):
        notifications.append(f"Order {payload['order_id']} confirmed")

    return handler
