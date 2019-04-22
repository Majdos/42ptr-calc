from enum import Enum

from PySide2 import QtWidgets, QtGui
from PySide2.QtGui import QPalette

from ptr42.math_language.parser.expression import Function, Operator, Constant

style = """
    padding: 10px;
"""


class Action(Enum):
    """
    Akciove tlacitka, ktore podporuje kalkulacka
    """
    NONE = 0
    EVALUATE = 1
    DECIMAL = 2
    CLEAR = 3
    TABULATOR = 4
    TABULATOR_REVERSED = 5


class CalculatorButton(QtWidgets.QPushButton):
    """
    Qt tlacitko reprezentujuce tlacitko v kalkulacke
    """

    def __init__(self, name: str, key_stroke: str):
        """
        Vytvori nove tlacitko s textom 'name' a nabinduje ho na 'key_stroke'

        :param name: text tlacitka
        :param key_stroke: klavesova skratka pre tlacitko
        """
        super().__init__(name)
        self.name = name
        self.clicked.connect(self.on_click)

        QtWidgets.QShortcut(QtGui.QKeySequence(
            key_stroke), self, self.on_click)

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                           QtWidgets.QSizePolicy.Expanding)
        self.setStyleSheet(style)

        font = self.font()
        font.setPixelSize(24)
        self.setFont(font)

    def on_click(self) -> None:
        """
        Abstraktna metoda, ktora sa vola pri kliknuti a stlaceni klavesy

        :raises NotImplementedError: abstraktna metoda, musi byt prepisana
        """
        raise NotImplementedError


class CalculatorFunctionButton(CalculatorButton):
    """
    Tlacitko reprezentujuce funkcie v kalkulacke
    """

    def __init__(self, name: str, handler, function: Function, key_stroke: str = None):
        """
        Vytvori tlacitko reprezentujuce funkciu.

        :param name: text tlacitka
        :param handler: funkcia, ktoru objekt zavola pri kliku s menom a funkciou
        :param function: funkcia reprezentujuca tlacitko
        :param key_stroke: klavesova skratka
        """
        super().__init__(name, key_stroke)
        self.function = function
        self.handler = handler

    def on_click(self):
        self.handler(self.name, self.function)


class CalculatorConstantButton(CalculatorButton):
    """
    Tlacitko reprezentujuce konstantu v kalkulacke
    """

    def __init__(self, name: str, handler, constant: Constant):
        """
        Vytvori tlacitko reprezentujuce konstantu.

        :param name: text tlacitka
        :param handler: funkcia, ktoru objekt zavola pri kliku s menom a konstantou
        :param constant: konstanta reprezentujuca tlacitko
        """
        super().__init__(name, name)
        self.handler = handler
        self.constant = constant
        self.setBackgroundRole(QPalette.ButtonText)
        self.setProperty("primary", "True")

    def on_click(self):
        self.handler(self.name, self.constant)


class CalculatorOperatorButton(CalculatorButton):
    """
    Tlacitko reprezentujuce operator v kalkulacke
    """

    def __init__(self, name: str, handler, operator: Operator):
        """
        Vytvori tlacitko reprezentujuce operator.

        :param name: text tlacitka
        :param handler: funkcia, ktoru objekt zavola pri kliku s menom a operatorom
        :param operator: operator reprezentujuci tlacitko
        """
        super().__init__(name, name)
        self.handler = handler
        self.operator = operator

    def on_click(self):
        self.handler(self.name, self.operator)


class CalculatorActionButton(CalculatorButton):
    """
    Tlacitko reprezentujuce akciu v kalkulacke
    """

    def __init__(self, name, handler, action: Action, key_stroke=None):
        """
        Vytvori tlacitko reprezentujuce akciu.

        :param name: text tlacitka
        :param handler: funkcia, ktoru objekt zavola pri kliku s menom a akciou
        :param action: akcia reprezentujuca tlacitko
        :param key_stroke: klavesova skratka
        """
        super().__init__(name, key_stroke)
        self.handler = handler
        self.action = action

    def on_click(self):
        self.handler(self.name, self.action)
