import unittest
import math42
#sys.path.append(0, './math42')

class BasicOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(30, 12), 42)
        self.assertEqual(add(-30, -12), -42)

    def test_subtract(self):
        self.assertEqual(subtract(30, 20), 10)
        self.assertEqual(subtract(30, -20), 40)
        self.assertEqual(subtract(5, 20), -15)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 5), 20)
        self.assertEqual(multiplication(42, 0), 0)

    def test_division(self):
        self.assertEqual(division(36, 6), 6)
        self.assertEqual(division(9, 4), 2.25)
        self.assertRaises(division(42, 0))
    
class AdvanceOperations(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(facorial(9), 362880)

    def test_abs(self):
        self.assertEqual(abs(-9), 9)
        self.assertEqual(abs(0), 0)
        self.assertEqual(abs(9), 9)

    def test_naturalExponent(self):
        self.assertEqual(naturalExponent(0), 1)
        self.assertAlmostEqual(naturalExponent(6), 403.428793493)

    def test_ln(self):
        self.assertEqual(ln(1), 0)
        self.assertAlmostEqual(naturalExponent(403.428793493), 6)
        self.assertRaises(ln(0))
        self.assertRaises(ln(-5))


if __name__ == '__main__':
    unittest.main()