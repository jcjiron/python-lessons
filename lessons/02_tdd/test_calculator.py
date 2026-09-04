import unittest

from calculator import calculate_total
from order_builder import OrderBuilder
from product import Product


class TestCalculator(unittest.TestCase):
    def test_sums_items_without_discount(self):
        cap = Product("cap", price=150)
        order = OrderBuilder().add_item(cap, quantity=1).build()

        self.assertEqual(calculate_total(order), 150)

    def test_applies_10_percent_if_over_500(self):
        t_shirt = Product("t_shirt", price=250)
        order = OrderBuilder().add_item(t_shirt, quantity=3).build()

        self.assertEqual(calculate_total(order), 675)

    def test_applies_discount10_coupon_then_big_order_rule(self):
        t_shirt = Product("t_shirt", price=250)
        cap = Product("cap", price=150)
        order = (
            OrderBuilder()
            .add_item(t_shirt, quantity=2)
            .add_item(cap, quantity=1)
            .build()
        )

        self.assertEqual(calculate_total(order, coupon="DISCOUNT10"), 526.5)


if __name__ == "__main__":
    unittest.main()
