import unittest

from loyalty import calculate_loyalty_points


class TestLoyaltyPoints(unittest.TestCase):
    """No CLI, no Order, no OrderBuilder involved — the domain piece is
    proven correct entirely on its own before anything gets to use it."""

    def test_zero_total_earns_zero_points(self):
        self.assertEqual(calculate_loyalty_points(0), 0)

    def test_below_50_earns_zero_points(self):
        self.assertEqual(calculate_loyalty_points(49.99), 0)

    def test_exactly_50_earns_one_point(self):
        self.assertEqual(calculate_loyalty_points(50), 1)

    def test_rounds_down_a_partial_amount(self):
        self.assertEqual(calculate_loyalty_points(526.5), 10)

    def test_large_total(self):
        self.assertEqual(calculate_loyalty_points(1000), 20)


if __name__ == "__main__":
    unittest.main()
