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

    def test_quantity_fifty(self):
        self.assertEqual(calculate_total(10, 50, 10), 450.00)

    def test_quantity_forty_nine(self):
        self.assertEqual(calculate_total(10, 49, 10), 441.00)

    def test_quantity_fifty_one(self):
        self.assertEqual(calculate_total(10, 51, 10), 459.00)

    def test_quantity_fifty_two(self):
        self.assertEqual(calculate_total(10, 52, 10), 468.00)

    def test_quantity_seventy_four(self):
        self.assertEqual(calculate_total(10, 74, 10), 666.00)

    def test_quantity_seventy_five(self):
        self.assertEqual(calculate_total(10, 75, 10), 675.00)

    def test_quantity_seventy_six_raises(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(10, 76, 10)
        self.assertEqual(str(ctx.exception), "quantity must not exceed 75")

    def test_quantity_fifty_zero_discount(self):
        self.assertEqual(calculate_total(10, 50, 0), 500.00)

    def test_quantity_fifty_full_discount(self):
        self.assertEqual(calculate_total(10, 50, 100), 0.00)

    def test_quantity_nine_hundred_ninety_nine(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(10, 999, 10)
        self.assertEqual(str(ctx.exception), "quantity must not exceed 75")

    def test_quantity_one_thousand(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(10, 1000, 10)
        self.assertEqual(str(ctx.exception), "quantity must not exceed 75")

    def test_quantity_one_thousand_zero_discount(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(10, 1000, 0)
        self.assertEqual(str(ctx.exception), "quantity must not exceed 75")

    def test_quantity_one_thousand_full_discount(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(10, 1000, 100)
        self.assertEqual(str(ctx.exception), "quantity must not exceed 75")

    def test_quantity_above_one_thousand_raises(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(10, 1001, 10)
        self.assertEqual(str(ctx.exception), "quantity must not exceed 75")

    def test_quantity_far_above_one_thousand_raises(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(10, 10000, 10)
        self.assertEqual(str(ctx.exception), "quantity must not exceed 75")

    def test_zero_quantity_raises(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(10, 0, 10)
        self.assertEqual(str(ctx.exception), "quantity must be positive")

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
        with self.assertRaises(ValueError) as ctx:
            calculate_total(-1, 2, 10)
        self.assertEqual(str(ctx.exception), "unit_price must be non-negative")

    def test_boolean_true_unit_price_raises(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(True, 2, 10)
        self.assertEqual(str(ctx.exception), "unit_price must be non-negative")

    def test_boolean_false_unit_price_raises(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(False, 2, 10)
        self.assertEqual(str(ctx.exception), "unit_price must be non-negative")

    def test_zero_unit_price(self):
        self.assertEqual(calculate_total(0, 2, 10), 0.00)

    def test_integer_one_unit_price(self):
        self.assertEqual(calculate_total(1, 2, 10), 1.80)

    def test_zero_float_unit_price(self):
        self.assertEqual(calculate_total(0.0, 2, 10), 0.00)

    def test_positive_float_unit_price(self):
        self.assertEqual(calculate_total(10.5, 2, 10), 18.90)

    def test_string_unit_price_raises(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total("10", 2, 10)
        self.assertEqual(str(ctx.exception), "unit_price must be non-negative")

    def test_none_unit_price_raises(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total(None, 2, 10)
        self.assertEqual(str(ctx.exception), "unit_price must be non-negative")

    def test_list_unit_price_raises(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_total([10], 2, 10)
        self.assertEqual(str(ctx.exception), "unit_price must be non-negative")

    def test_nan_unit_price_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(float("nan"), 2, 10)

    def test_positive_infinity_unit_price_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(float("inf"), 2, 10)

    def test_negative_infinity_unit_price_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(float("-inf"), 2, 10)

    def test_large_finite_float_unit_price(self):
        self.assertEqual(calculate_total(1e12, 1, 0), 1000000000000.00)

    def test_large_integer_unit_price(self):
        self.assertEqual(calculate_total(1_000_000, 2, 10), 1_800_000.00)

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
        with self.assertRaises(ValueError):
            calculate_total(10, 2, 10.5)

    def test_integer_valued_float_discount_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(10, 2, 10.0)

    def test_zero_discount(self):
        self.assertEqual(calculate_total(10, 2, 0), 20.00)

    def test_integer_one_discount(self):
        self.assertEqual(calculate_total(10, 2, 1), 19.80)

    def test_full_discount(self):
        self.assertEqual(calculate_total(10, 2, 100), 0.00)

    def test_round_half_up_midpoint(self):
        self.assertEqual(calculate_total(2.675, 1, 0), 2.68)

    def test_round_half_up_below_midpoint(self):
        self.assertEqual(calculate_total(2.674, 1, 0), 2.67)

    def test_round_half_up_even_hundredths_midpoint(self):
        self.assertEqual(calculate_total(1.225, 1, 0), 1.23)


if __name__ == "__main__":
    unittest.main()
