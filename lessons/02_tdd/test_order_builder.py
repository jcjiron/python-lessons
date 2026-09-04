import unittest

from order_builder import OrderBuilder
from product import Product


class TestOrderBuilder(unittest.TestCase):
    def test_build_returns_order_with_added_items(self):
        t_shirt = Product("t_shirt", price=250)
        cap = Product("cap", price=150)

        order = (
            OrderBuilder()
            .add_item(t_shirt, quantity=2)
            .add_item(cap, quantity=1)
            .build()
        )

        self.assertEqual(order.items, [(t_shirt, 2), (cap, 1)])


if __name__ == "__main__":
    unittest.main()
