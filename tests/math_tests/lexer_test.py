import gettext
import unittest

from ptr42.math_language.lexer.expression_error import ExpressionError
from ptr42.math_language.lexer.default_lexer import get_default_lexer
from ptr42.math_language.parser.parser import MathParser

lang = gettext.translation("messages", "resources/translations", ["sk_SK"])
lang.install()


def calculator(expresion: str) -> float:
    lexer = get_default_lexer(expresion)
    tokens = list(lexer.generate_tokens())
    parser = MathParser(tokens, lexer.get_operators())
    ast = parser.parse()
    return ast.evaluate()


class PriorityOperations(unittest.TestCase):

    def test_basic_operations(self):
        self.assertAlmostEqual(calculator("5+6-9"), 2)
        self.assertAlmostEqual(calculator("10-6*5+4"), -16)
        self.assertAlmostEqual(calculator("4+16/4*2"), 12)
        self.assertAlmostEqual(calculator("5*5+3*2"), 31)
        self.assertAlmostEqual(calculator("abs(-20)"), 20)
        self.assertAlmostEqual(calculator("sqrt(25)"), 5)

    def test_basic_and_advance_minimized(self):
        self.assertAlmostEqual(calculator("fact(1+2)*2"), 12)
        self.assertAlmostEqual(calculator("root(8,3)/2+4"), 5)
        self.assertAlmostEqual(calculator("9+sqrt(16)"), 13)
        self.assertAlmostEqual(calculator("ln(1)*42"), 0)
        self.assertAlmostEqual(calculator("41+exp(0)"), 42)
        self.assertAlmostEqual(calculator("abs(4*3-20)+2"), 10)

        self.assertAlmostEqual(calculator("root(2,2)+sqrt(9)"), 4.414213562373095)

    def test_basic_and_advance(self):
        self.assertAlmostEqual(calculator("fact(1+2) * 2"), 12)
        self.assertAlmostEqual(calculator("root(8,3) / 2 + 4"), 5)
        self.assertAlmostEqual(calculator("9 + sqrt(16)"), 13)
        self.assertAlmostEqual(calculator("ln(1) * 42"), 0)
        self.assertAlmostEqual(calculator("41 + exp(0)"), 42)
        self.assertAlmostEqual(calculator("abs(4*3-20) + 2"), 10)

        self.assertAlmostEqual(calculator("root(2,2) + sqrt(9)"), 4.414213562373095)

    def test_advance_and_advance(self):
        self.assertAlmostEqual(calculator("fact(abs(-3))"), 6)
        self.assertAlmostEqual(calculator("ln(exp(42))"), 42)
        self.assertAlmostEqual(calculator("root(sqrt(4),abs(-3))"), 1.2599210498948732)

    def test_incorrect_input(self):
        self.assertRaises(ExpressionError, calculator, "++42")
        self.assertRaises(ExpressionError, calculator, "-42-")
        self.assertRaises(ExpressionError, calculator, "fact(-)")
        self.assertRaises(ExpressionError, calculator, "5+5)*4")
        self.assertRaises(ExpressionError, calculator, "devet")
        self.assertRaises(ExpressionError, calculator, "5.5.6")
        self.assertRaises(ExpressionError, calculator, "foo(5)")
