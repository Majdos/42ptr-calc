from typing import List, Iterable

from ptr42.math_language.lexer.token import Token, TokenTypes
from ptr42.math_language.parser.expression import Function


class FunctionToken(Token):
    """
        Trieda reprezentujuca funkcnionalny token
    """

    def __init__(self, function: Function, args_tokens: List[Token]):
        """
        Inicializuje funkcny token

        :param function: funkcia, ktoru token zastupuje
        :param args_tokens: argumenty funkcie rozparsovane na tokeny
        """
        super(FunctionToken, self).__init__(TokenTypes.FUNCTION_TOKEN, function, precedence=0)
        self.args_tokens = args_tokens

    def arguments(self) -> Iterable[Token]:
        """
        Zoskupi tokeny argumentov podla ich poradia v funkcii Ak ma funkcia napriklad fn(x, y) 2 argumenty,
        tak vrati list tokenov o 2 prvkoch. Funkcia taktiez nezahrnie tokeny oddelovaca argumentov, takze vysledok
        funkcie je pripraveny na parsovanie parserom

        :return: list tokenov, ktore reprezentuju urcite argumenty
        """
        collected_tokens = []
        for token in self.args_tokens:
            if token.type != TokenTypes.COMMA_TOKEN:
                collected_tokens.append(token)
            elif collected_tokens and token.type == TokenTypes.COMMA_TOKEN:
                yield collected_tokens
                collected_tokens.clear()
            else:
                raise ValueError("Nespravna ciarka v argumentoch")

        if collected_tokens:
            yield collected_tokens

    def __repr__(self):
        return f"{self.type}:{self.value.func.__name__}({self.args_tokens})"
