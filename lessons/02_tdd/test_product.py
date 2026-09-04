import unittest

from product import Product


class TestProduct(unittest.TestCase):
    def test_stores_name_and_price(self):
        product = Product("t_shirt", price=250)

        self.assertEqual(product.name, "t_shirt")
        self.assertEqual(product.price, 250)


if __name__ == "__main__":
    unittest.main()
