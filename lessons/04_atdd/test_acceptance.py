import unittest

from calculator import calculate_total
from order_builder import OrderBuilder
from product import Product


class TestAcceptanceCriteria(unittest.TestCase):
    def test_ac1_large_order_gets_additional_10_percent_discount(self):
        # Arrange
        t_shirt = Product("t_shirt", price=250)
        order = OrderBuilder().add_item(t_shirt, quantity=3).build()  # $750

        # Act
        total = calculate_total(order)

        # Assert
        self.assertEqual(total, 675)

    def test_ac2_discount10_coupon_applies_before_large_order_rule(self):
        # Arrange
        t_shirt = Product("t_shirt", price=250)
        cap = Product("cap", price=150)
        order = (
            OrderBuilder()
            .add_item(t_shirt, quantity=2)
            .add_item(cap, quantity=1)
            .build()
        )

        # Act
        total = calculate_total(order, coupon="DISCOUNT10")

        # Assert
        self.assertEqual(total, 526.5)

    def test_ac3_empty_order_is_rejected(self):
        # Arrange
        order = OrderBuilder().build()

        # Act / Assert
        with self.assertRaises(ValueError):
            calculate_total(order)


if __name__ == "__main__":
    unittest.main()
