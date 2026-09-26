import unittest

from money import Money


class TestMoney(unittest.TestCase):
    """Money is a Value Object: identical amounts are equal, regardless of
    which instance they are."""

    def test_same_amount_are_equal(self):
        self.assertEqual(Money(250), Money(250))

    def test_different_amounts_are_not_equal(self):
        self.assertNotEqual(Money(250), Money(150))

    def test_add_combines_amounts(self):
        self.assertEqual(Money(250) + Money(150), Money(400))

    def test_apply_discount_reduces_amount(self):
        self.assertEqual(Money(500).apply_discount(0.10), Money(450))

    def test_rounds_to_two_decimals(self):
        self.assertEqual(Money(10.005), Money(10.01))


if __name__ == "__main__":
    unittest.main()
