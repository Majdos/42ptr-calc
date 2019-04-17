import unittest

from ptr42.math_language.lexer.lexer import MathLexer
from ptr42.math_language.parser.parser import MathParser
from ptr42.math_language.lexer.default_lexer import get_default_lexer

def calculator(expresion: str) -> str:
    lexer = get_default_lexer()
    tokens = list(lexer.generate_tokens())
    parser = MathParser(tokens, lexer.get_operators())
    ast = parser.parse()
    return str(ast.evaluate())

class PriorityOperations(unittest.TestCase):

    def test_basic_operations(self):     
        self.assertEqual(calculator("5+6-9"), "2")
        self.assertEqual(calculator("10-6*5+4"), "-16")
        self.assertEqual(calculator("4+16/4*2"), "12")
        self.assertEqual(calculator("5*5+3*2"), "31")

    def test_basic_and_advance(self):
        self.assertEqual(calculator("fact(1+2)*2"), "12")
        self.assertEqual(calculator("root(8,3)/2+4"), "5")
        self.assertEqual(calculator("9+sqrt(16)"), "13")
        self.assertEqual(calculator("ln(1)*42"), "0")
        self.assertEqual(calculator("41+exp(0)"), "42")
        self.assertEqual(calculator("abs(4*3-20)+2"), "10")

        self.assertEqual(calculator("root(2,2)+sqrt(9)"), "7")

    def test_advance_and_advance(self):
        self.assertEqual(calculator("fact(abs(-3))"), "6")
        self.assertEqual(calculator("ln(exp(42))"), "42")
        self.assertEqual(calculator("root(sqrt(4),abs(-3))"), "8")
