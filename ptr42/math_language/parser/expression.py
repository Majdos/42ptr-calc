from typing import Any, Iterable


class Function(object):
    """
    Objekt reprezentujuci funkciu
    """

    def __init__(self, func, arg_count: int = 0):
        """

        :param func: ukazovatel na funkciu
        :param arg_count: pocet argumentov funkcie
        """
        self.func = func
        self.arg_count = arg_count
        self.args = list()

    def set_args(self, *args: Iterable[Any]) -> None:
        """
        Nastavi argumenty, ktore sa doplnia v evaluacii

        :param args: argumenty, ktore sa nastavia dalsi eval
        """

        args = list(args)
        if len(args) != self.arg_count:
            raise ValueError(f"Funkcie vyzaduje {self.arg_count} argumentov! Bolo ich zadanych len {len(args)}")
        self.args = args

    def evaluate(self):
        """
        Spusti funkciu s nastavenymi argumentami, ktore nastavuje set_args

        :return: vysledok funkcie
        """

        return self.func(*self.args)


class Constant(object):
    """
    Trieda ktora reprezentuje konstantu. Konstanta moze mat svoje meno(name).
    """

    def __init__(self, value, name=None):
        self.name = name if name is not None else value
        self.value = float(value)

    def __repr__(self):
        return f"{self.name} = {self.value}"


class Operator(object):
    """
    Trieda reprezentujuca binarny aj unarny operator
    """

    def __init__(self, operator_func, precedence: int, unary_func=None):
        self.operator_func = operator_func
        self.precedence = precedence
        self.unary_func = unary_func

    def __lt__(self, other):
        return self.precedence < other.precedence

    def evaluate(self, *args):
        return self.operator_func(*args)

    def __repr__(self):
        return f"{self.operator_func.__name__}"


class UnaryOperator(Operator):
    def __init__(self, operator_func):
        super().__init__(operator_func, 0, operator_func)


class BinaryOperator(Operator):
    def __init__(self, operator_func, precedence):
        super().__init__(operator_func, precedence)
