import unittest

from shipping import calculate_shipping


class ShippingTests(unittest.TestCase):

    def test_shipping_cost(self):
        self.assertEqual(calculate_shipping(1), 5.00)


if __name__ == "__main__":
    unittest.main()
