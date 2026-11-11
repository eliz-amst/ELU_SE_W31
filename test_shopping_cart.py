
import unittest
from shopping_cart import CalculateTotal


class TestShoppingCart(unittest.TestCase):

    def test_single_item(self):
        cart = [
            {'name': 'Item A', 'price': 10.99}
        ]
        self.assertEqual(CalculateTotal(cart), 10.99)

    def test_multiple_items(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99}
        ]
        self.assertAlmostEqual(CalculateTotal(cart), 16.98)

    def test_empty_cart(self):
        cart = []
        self.assertEqual(CalculateTotal(cart), 0)


if __name__ == '__main__':
    unittest.main()
