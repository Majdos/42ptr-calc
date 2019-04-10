import unittest
import src.math42 as math


class BasicOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math.addition(30, 12), 42)
        self.assertEqual(math.addition(-30, -12), -42)

    def test_subtract(self):
        self.assertEqual(math.subtract(30, 20), 10)
        self.assertEqual(math.subtract(30, -20), 50)
        self.assertEqual(math.subtract(5, 20), -15)

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
        self.assertEqual(math.absoluteNumber(-9), 9)
        self.assertEqual(math.absoluteNumber(0), 0)
        self.assertEqual(math.absoluteNumber(9), 9)

    def test_naturalExponent(self):
        self.assertEqual(math.naturalExponent(0), 1)
        self.assertAlmostEqual(math.naturalExponent(6), 403.428793493)

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
        self.assertEqual(math.binToDec("100"), 4)
        self.assertEqual(math.binToDec("000"), 0)
        self.assertEqual(math.binToDec("1010"), 10)
        self.assertRaises(ValueError, math.binToDec, "120")
        self.assertRaises(ValueError, math.binToDec, "100b")
        self.assertRaises(ValueError, math.binToDec, "-100")

    def test_hex_to_dec(self):
        self.assertEqual(math.hextoDec("a"), 10)
        self.assertEqual(math.hextoDec("A"), 10)
        self.assertEqual(math.hextoDec("42"), 66)
        self.assertRaises(ValueError, math.hextoDec, "ahoj")
        self.assertRaises(ValueError, math.hextoDec, "-5")

    def test_oct_to_dec(self):
        self.assertEqual(math.octToDec("7"), 7)
        self.assertEqual(math.octToDec("000"), 0)
        self.assertEqual(math.octToDec("21"), 17)
        self.assertRaises(ValueError, math.octToDec, "820")
        self.assertRaises(ValueError, math.octToDec, "10d")
        self.assertRaises(ValueError, math.octToDec, "-214")


if __name__ == '__main__':
    unittest.main()
