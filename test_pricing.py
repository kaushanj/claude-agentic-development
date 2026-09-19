import unittest

from pricing import calculate_total


class PricingTests(unittest.TestCase):
    def test_normal_discount(self):
        self.assertEqual(
            calculate_total(10, 2, 10),
            18.00,
        )

    def test_zero_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 0, 10)

    def test_fractional_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 1.5, 10)

    def test_negative_unit_price_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(-1, 2, 10)

    def test_negative_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, -1)

    def test_discount_above_100_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, 101)

    def test_zero_discount(self):
        self.assertEqual(calculate_total(10, 2, 0), 20.00)

    def test_full_discount(self):
        self.assertEqual(calculate_total(10, 2, 100), 0.00)


if __name__ == "__main__":
    unittest.main()