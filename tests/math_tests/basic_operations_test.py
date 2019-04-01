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
        self.assertRaises(ValueError,math.division,42,0)


class AdvancedOperations(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(math.factorial(9), 362880)

    def test_abs(self):
        self.assertEqual(abs(-9), 9)
        self.assertEqual(abs(0), 0)
        self.assertEqual(abs(9), 9)

    def test_naturalExponent(self):
        self.assertEqual(math.naturalExponent(0), 1)
        self.assertAlmostEqual(math.naturalExponent(6), 403.428793493)

    def test_ln(self):
        self.assertEqual(math.ln(1), 0)
        self.assertAlmostEqual(math.ln(403.428793493),6)
        self.assertRaises(ValueError, math.ln,0)
        self.assertRaises(ValueError, math.ln,-5)


if __name__ == '__main__':
    unittest.main()
