import unittest

from order import Order
from order_line import OrderLine
from product import Product


class TestOrder(unittest.TestCase):
    """Order is an Entity: identity comes from order_id, not from its
    lines."""

    def test_same_id_means_same_order_even_with_different_lines(self):
        t_shirt = Product("t_shirt", price=250)
        cap = Product("cap", price=150)

        order_a = Order("order-1", [OrderLine(t_shirt, 2)])
        order_b = Order("order-1", [OrderLine(cap, 1)])

        self.assertEqual(order_a, order_b)

    def test_different_id_means_different_order_even_with_same_lines(self):
        t_shirt = Product("t_shirt", price=250)

        order_a = Order("order-1", [OrderLine(t_shirt, 2)])
        order_b = Order("order-2", [OrderLine(t_shirt, 2)])

        self.assertNotEqual(order_a, order_b)


if __name__ == "__main__":
    unittest.main()
