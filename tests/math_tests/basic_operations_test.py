import unittest
import ptr42.math42 as math


class BasicOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math.addition(30, 12), 42)
        self.assertEqual(math.addition(-30, -12), -42)

    def test_subtract(self):
        self.assertEqual(math.subtract(30, 20), 10)
        self.assertEqual(math.subtract(30, -20), 50)
        self.assertEqual(math.subtract(5, 20), -15)

    def test_negate(self):
        self.assertAlmostEqual(math.negate(5.003), -5.003)
        self.assertAlmostEqual(math.negate(-10.003), 10.003)
        self.assertAlmostEqual(math.negate(0), 0)

    def test_multiplication(self):
        self.assertEqual(math.multiplication(4, 5), 20)
        self.assertEqual(math.multiplication(42, 0), 0)

    def test_division(self):
        self.assertEqual(math.division(36, 6), 6)
        self.assertAlmostEqual(math.division(9, 4), 2.25)
        self.assertRaises(ValueError, math.division, 42, 0)


class AdvancedOperations(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(math.factorial(9), 362880)

    def test_abs(self):
        self.assertEqual(math.absolute_number(-9), 9)
        self.assertEqual(math.absolute_number(0), 0)
        self.assertEqual(math.absolute_number(9), 9)

    def test_natural_exponent(self):
        self.assertEqual(math.natural_exponent(0), 1)
        self.assertAlmostEqual(math.natural_exponent(6), 403.428793493)

    def test_ln(self):
        self.assertEqual(math.ln(1), 0)
        self.assertAlmostEqual(math.ln(403.428793493), 6)
        self.assertRaises(ValueError, math.ln, 0)
        self.assertRaises(ValueError, math.ln, -5)

    def test_sqrt(self):
        self.assertEqual(math.sqrt(1), 1)
        self.assertEqual(math.sqrt(0), 0)
        self.assertEqual(math.sqrt(4), 2)
        self.assertRaises(ValueError, math.sqrt, -2)

    def test_universal_root(self):
        self.assertEqual(math.root(8, 3), 2)
        self.assertEqual(math.root(16, 4), 2)
        self.assertRaises(ValueError, math.root, 0, 0)
        self.assertRaises(ValueError, math.root, -1, 1)
        self.assertRaises(ValueError, math.root, 5, -1)


class OptionalOperations(unittest.TestCase):

    def test_bin_to_dec(self):
        self.assertEqual(math.bin_to_dec("100"), 4)
        self.assertEqual(math.bin_to_dec("000"), 0)
        self.assertEqual(math.bin_to_dec("1010"), 10)
        self.assertRaises(ValueError, math.bin_to_dec, "120")
        self.assertRaises(ValueError, math.bin_to_dec, "100b")
        self.assertRaises(ValueError, math.bin_to_dec, "-100")

    def test_hex_to_dec(self):
        self.assertEqual(math.hex_to_dec("a"), 10)
        self.assertEqual(math.hex_to_dec("A"), 10)
        self.assertEqual(math.hex_to_dec("42"), 66)
        self.assertRaises(ValueError, math.hex_to_dec, "ahoj")
        self.assertRaises(ValueError, math.hex_to_dec, "-5")

    def test_oct_to_dec(self):
        self.assertEqual(math.oct_to_dec("7"), 7)
        self.assertEqual(math.oct_to_dec("000"), 0)
        self.assertEqual(math.oct_to_dec("21"), 17)
        self.assertRaises(ValueError, math.oct_to_dec, "820")
        self.assertRaises(ValueError, math.oct_to_dec, "10d")
        self.assertRaises(ValueError, math.oct_to_dec, "-214")


if __name__ == '__main__':
    unittest.main()
