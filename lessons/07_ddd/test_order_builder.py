import unittest

from order_builder import OrderBuilder
from product import Product


class TestOrderBuilder(unittest.TestCase):
    def test_build_returns_order_with_id_and_lines(self):
        t_shirt = Product("t_shirt", price=250)
        cap = Product("cap", price=150)

        order = (
            OrderBuilder("order-1")
            .add_item(t_shirt, quantity=2)
            .add_item(cap, quantity=1)
            .build()
        )

        self.assertEqual(order.order_id, "order-1")
        self.assertEqual(len(order.lines), 2)
        self.assertEqual(order.lines[0].product, t_shirt)
        self.assertEqual(order.lines[0].quantity, 2)


if __name__ == "__main__":
    unittest.main()
