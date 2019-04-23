import sys
import cProfile
from random import randint

from ptr42.math_language.parser.parser import MathParser
from ptr42.math_language.lexer.default_lexer import get_default_lexer

def calculator(expresion: str) -> float:
    lexer = get_default_lexer(expresion)
    tokens = list(lexer.generate_tokens())
    parser = MathParser(tokens, lexer.get_operators())
    return parser.parse().evaluate()

if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

    counter = 0
    intSum = 0
    intSumPow2 = 0

    for input in sys.stdin:
        counter = calculator(str(counter) + "+" + "1")
        intSum = calculator(str(intSum) + "+" + str(float(input)))
        inputPow2 = calculator(str(float(input)) + "*" + str(float(input)))
        intSumPow2 = calculator(str(intSumPow2) + "+" + str(inputPow2))

    average = calculator(str(intSum) + "/" + str(counter))
    calculator("sqrt("+"1/("+str(counter)+"-1)*("+str(intSumPow2)+"-"+str(counter)+"*"+str(average)+"*"+str(average)+"))")
    
    pr.disable()
    pr.print_stats(sort='time')