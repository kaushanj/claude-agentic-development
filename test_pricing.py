import unittest

from pricing import calculate_total


class PricingTests(unittest.TestCase):
    def test_normal_discount(self):
        self.assertEqual(
            calculate_total(10, 2, 10),
            18.00,
        )

    def test_negative_unit_price_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(-1, 2, 10)


if __name__ == "__main__":
    unittest.main()