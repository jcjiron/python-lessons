import unittest

from event_bus import EventBus
from handlers import (
    make_calculate_total_handler,
    make_send_confirmation_handler,
    make_update_stock_handler,
)


def make_payload():
    return {
        "order_id": "order-1",
        "items": [
            {"product": "t_shirt", "price": 250, "quantity": 2},
            {"product": "cap", "price": 150, "quantity": 1},
        ],
        "coupon": "DISCOUNT10",
    }


class TestOrderPlacedEvent(unittest.TestCase):
    def setUp(self):
        self.bus = EventBus()
        self.receipts = {}
        self.stock_log = []
        self.notifications = []

        self.bus.subscribe("OrderPlaced", make_calculate_total_handler(self.receipts))
        self.bus.subscribe("OrderPlaced", make_update_stock_handler(self.stock_log))
        self.bus.subscribe(
            "OrderPlaced", make_send_confirmation_handler(self.notifications)
        )

    def test_publishing_triggers_all_three_independent_handlers(self):
        self.bus.publish("OrderPlaced", make_payload())

        self.assertEqual(self.receipts["order-1"], 526.5)
        self.assertIn(("t_shirt", 2), self.stock_log)
        self.assertIn(("cap", 1), self.stock_log)
        self.assertIn("Order order-1 confirmed", self.notifications)

    def test_an_unrelated_event_triggers_nothing(self):
        self.bus.publish("OrderCancelled", make_payload())

        self.assertEqual(self.receipts, {})
        self.assertEqual(self.stock_log, [])
        self.assertEqual(self.notifications, [])

    def test_a_new_handler_can_be_added_without_changing_how_orders_are_published(self):
        extra_log = []
        self.bus.subscribe("OrderPlaced", lambda payload: extra_log.append(payload["order_id"]))

        self.bus.publish("OrderPlaced", make_payload())

        self.assertEqual(extra_log, ["order-1"])


if __name__ == "__main__":
    unittest.main()
