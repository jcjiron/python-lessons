import unittest

from money import Money
from order_line import OrderLine
from product import Product


class TestOrderLine(unittest.TestCase):
    def test_subtotal_multiplies_price_by_quantity(self):
        t_shirt = Product("t_shirt", price=250)
        line = OrderLine(t_shirt, quantity=2)

        self.assertEqual(line.subtotal, Money(500))


if __name__ == "__main__":
    unittest.main()
