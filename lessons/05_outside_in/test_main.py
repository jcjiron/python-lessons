import unittest

from main import run


class TestCliWithFakeCalculator(unittest.TestCase):
    """Stage 1 of Outside-In: prove the outer layer (CLI) works correctly
    before trusting the real domain underneath it."""

    def test_receipt_shows_items_and_the_fake_total(self):
        # Arrange: a fake calculator, standing in for the real domain
        def fake_calculate_total(order, coupon=None):
            return 999

        # Act
        receipt = run(
            ["t_shirt:2", "cap:1"], coupon=None, calculate_total_fn=fake_calculate_total
        )

        # Assert: the CLI layer itself works, regardless of real business rules
        self.assertIn("t_shirt x2", receipt)
        self.assertIn("cap x1", receipt)
        self.assertIn("TOTAL: $999", receipt)


class TestCliWithRealCalculator(unittest.TestCase):
    """Stage 2 of Outside-In: swap the fake for the real domain (lesson 2/4)."""

    def test_receipt_uses_real_discount_rules(self):
        # Act
        receipt = run(["t_shirt:2", "cap:1"], coupon="DISCOUNT10")

        # Assert
        self.assertIn("TOTAL: $526.5", receipt)


if __name__ == "__main__":
    unittest.main()
