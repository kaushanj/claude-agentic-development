import unittest

from pricing import calculate_total


class PricingTests(unittest.TestCase):
    def test_normal_discount(self):
        self.assertEqual(
            calculate_total(10, 2, 10),
            18.00,
        )

    def test_minimum_quantity_one(self):
        self.assertEqual(calculate_total(10, 1, 10), 9.00)

    def test_quantity_ten(self):
        self.assertEqual(calculate_total(10, 10, 10), 90.00)

    def test_zero_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 0, 10)

    def test_negative_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, -1, 10)

    def test_fractional_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 1.5, 10)

    def test_boolean_true_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, True, 10)

    def test_boolean_false_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, False, 10)

    def test_integer_valued_float_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 1.0, 10)

    def test_string_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, "1", 10)

    def test_none_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, None, 10)

    def test_negative_unit_price_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(-1, 2, 10)

    def test_negative_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, -1)

    def test_discount_above_100_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, 101)

    def test_boolean_true_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, True)

    def test_boolean_false_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, False)

    def test_string_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, "10")

    def test_none_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, None)

    def test_nan_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, float("nan"))

    def test_positive_infinity_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, float("inf"))

    def test_negative_infinity_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, float("-inf"))

    def test_fractional_discount(self):
        self.assertEqual(calculate_total(10, 2, 10.5), 17.90)

    def test_zero_discount(self):
        self.assertEqual(calculate_total(10, 2, 0), 20.00)

    def test_full_discount(self):
        self.assertEqual(calculate_total(10, 2, 100), 0.00)


if __name__ == "__main__":
    unittest.main()