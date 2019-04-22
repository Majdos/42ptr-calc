import cProfile
from random import randint

from ptr42.math_language.parser.parser import MathParser
from ptr42.math_language.lexer.default_lexer import get_default_lexer

def calculator(expresion: str):
    lexer = get_default_lexer(expresion)
    tokens = list(lexer.generate_tokens())
    parser = MathParser(tokens, lexer.get_operators())
    ast = parser.parse()

if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

    for i in range(1, 100):
        string = "fact("+str(randint(1, i))+")+root(4,"+str(randint(1, i))+")/sqrt(ln("+str(randint(1, i))+"))*exp("+str(randint(1, i))+")-abs(-"+str(randint(1, i))+")"
        calculator(string)
    
    pr.disable()
    pr.print_stats(sort='time')