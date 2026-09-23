import unittest

from shipping import calculate_shipping

ERROR_MESSAGE = "weight must be between 1 and 50"


class ShippingTests(unittest.TestCase):

    def test_shipping_cost(self):
        self.assertEqual(calculate_shipping(1), 5.00)

    def test_weight_maximum_is_valid(self):
        self.assertEqual(calculate_shipping(50), 5.00)

    def test_weight_zero_is_invalid(self):
        with self.assertRaises(ValueError) as cm:
            calculate_shipping(0)
        self.assertEqual(str(cm.exception), ERROR_MESSAGE)

    def test_weight_fifty_one_is_invalid(self):
        with self.assertRaises(ValueError) as cm:
            calculate_shipping(51)
        self.assertEqual(str(cm.exception), ERROR_MESSAGE)

    def test_negative_weight_is_invalid(self):
        with self.assertRaises(ValueError) as cm:
            calculate_shipping(-1)
        self.assertEqual(str(cm.exception), ERROR_MESSAGE)

    def test_float_weight_is_invalid(self):
        for value in (1.5, 1.0, 50.0):
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as cm:
                    calculate_shipping(value)
                self.assertEqual(str(cm.exception), ERROR_MESSAGE)

    def test_bool_weight_is_invalid(self):
        for value in (True, False):
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as cm:
                    calculate_shipping(value)
                self.assertEqual(str(cm.exception), ERROR_MESSAGE)

    def test_string_weight_is_invalid(self):
        with self.assertRaises(ValueError) as cm:
            calculate_shipping("1")
        self.assertEqual(str(cm.exception), ERROR_MESSAGE)

    def test_none_weight_is_invalid(self):
        with self.assertRaises(ValueError) as cm:
            calculate_shipping(None)
        self.assertEqual(str(cm.exception), ERROR_MESSAGE)


if __name__ == "__main__":
    unittest.main()
