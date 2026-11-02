import unittest

from models import Product
from order_functions import (
    add_item,
    apply_coupon,
    apply_large_order_rule,
    calculate_total,
    empty_order,
    line_subtotal,
    order_subtotal,
)


class TestOrderFunctions(unittest.TestCase):
    def test_empty_order_is_empty(self):
        self.assertEqual(empty_order(), ())

    def test_add_item_does_not_mutate_the_original_order(self):
        # Arrange
        t_shirt = Product("t_shirt", price=250)
        cap = Product("cap", price=150)
        order_a = add_item(empty_order(), t_shirt, quantity=1)

        # Act: build a second order on top of order_a
        order_b = add_item(order_a, cap, quantity=1)

        # Assert: order_a is exactly as it was before order_b existed
        self.assertEqual(len(order_a), 1)
        self.assertEqual(len(order_b), 2)

    def test_line_subtotal_multiplies_price_by_quantity(self):
        t_shirt = Product("t_shirt", price=250)
        line = add_item(empty_order(), t_shirt, quantity=2)[0]

        self.assertEqual(line_subtotal(line), 500)

    def test_order_subtotal_sums_all_lines(self):
        t_shirt = Product("t_shirt", price=250)
        cap = Product("cap", price=150)
        order = add_item(add_item(empty_order(), t_shirt, 2), cap, 1)

        self.assertEqual(order_subtotal(order), 650)

    def test_apply_coupon_discounts_10_percent(self):
        self.assertEqual(apply_coupon(650, "DISCOUNT10"), 585)

    def test_apply_coupon_does_nothing_without_a_match(self):
        self.assertEqual(apply_coupon(650, None), 650)

    def test_apply_large_order_rule_discounts_over_500(self):
        self.assertEqual(apply_large_order_rule(585), 526.5)

    def test_calculate_total_composes_all_the_rules(self):
        t_shirt = Product("t_shirt", price=250)
        cap = Product("cap", price=150)
        order = add_item(add_item(empty_order(), t_shirt, 2), cap, 1)

        self.assertEqual(calculate_total(order, coupon="DISCOUNT10"), 526.5)

    def test_empty_order_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total(empty_order())


if __name__ == "__main__":
    unittest.main()
