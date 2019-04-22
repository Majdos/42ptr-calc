from ptr42.math_language.lexer.lexer import MathLexer
from ptr42.math_language.parser.expression import Function, BinaryOperator, Operator
import ptr42.math42 as math42


def get_default_lexer(expresion: str) -> MathLexer:
    """
    Vytvori nove lexer pre kalkulacku s preddefinovanymi funkciam ia operatormi

    :param expresion: matematicky vyraz, ktory sa spracuje na tokeny
    :return: novy lexer s nastavenymi funkciami a operatormi
    """

    lexer = MathLexer(expresion)

    lexer.add_operator("+", BinaryOperator(math42.addition, 6))
    lexer.add_operator("-", Operator(math42.subtract, 6, math42.negate))
    lexer.add_operator("*", BinaryOperator(math42.multiplication, 5))
    lexer.add_operator("/", BinaryOperator(math42.division, 5))

    lexer.add_function("fact", Function(math42.factorial, 1))
    lexer.add_function("root", Function(math42.root, 2))
    lexer.add_function("sqrt", Function(math42.sqrt, 1))
    lexer.add_function("ln", Function(math42.ln, 1))
    lexer.add_function("exp", Function(math42.natural_exponent, 1))
    lexer.add_function("abs", Function(math42.absolute_number, 1))

    return lexer
