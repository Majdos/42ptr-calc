import cProfile
import sys

from ptr42 import get_default_lexer
from ptr42 import MathParser


def calculator(expresion: str) -> float:
    lexer = get_default_lexer(expresion)
    tokens = list(lexer.generate_tokens())
    parser = MathParser(tokens, lexer.get_operators())
    return parser.parse().evaluate()


def main():
    pr = cProfile.Profile()
    pr.enable()

    counter = 0
    int_sum = 0
    int_sum_pow2 = 0

    for input_text in sys.stdin:
        counter = calculator(str(counter) + "+" + "1")
        int_sum = calculator(str(int_sum) + "+" + str(float(input_text)))
        input_pow2 = calculator(str(float(input_text)) + "*" + str(float(input_text)))
        int_sum_pow2 = calculator(str(int_sum_pow2) + "+" + str(input_pow2))

    average = calculator(str(int_sum) + "/" + str(counter))
    calculator("sqrt(" + "1/(" + str(counter) + "-1)*(" + str(int_sum_pow2) + "-" + str(counter) + "*" + str(
        average) + "*" + str(average) + "))")

    pr.disable()
    pr.print_stats(sort='time')


if __name__ == '__main__':
    main()
