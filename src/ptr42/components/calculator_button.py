from enum import Enum

from PySide2 import QtWidgets, QtGui
from PySide2.QtGui import QPalette

from ptr42.math_language.parser.expression import Function, Operator, Constant

style = """
    padding: 10px;
"""


class Action(Enum):
    NONE = 0
    EVALUATE = 1
    DECIMAL = 2
    CLEAR = 3
    TABULATOR = 4
    TABULATOR_REVERSED = 5


class CalculatorButton(QtWidgets.QPushButton):
    def __init__(self, name: str, key_stroke: str):
        super().__init__(name)
        self.name = name
        self.clicked.connect(self.on_click)

        QtWidgets.QShortcut(QtGui.QKeySequence(
            key_stroke), self, self.on_click)

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setStyleSheet(style)

        font = self.font()
        font.setPixelSize(24)
        self.setFont(font)

    def on_click(self):
        raise NotImplementedError


class CalculatorFunctionButton(CalculatorButton):
    def __init__(self, name: str, handler, function: Function, key_stroke: str = None):
        super().__init__(name, key_stroke)
        self.function = function
        self.handler = handler

    def on_click(self):
        self.handler(self.name, self.function)


class CalculatorConstantButton(CalculatorButton):
    def __init__(self, name: str, handler, constant: Constant):
        super().__init__(name, name)
        self.handler = handler
        self.constant = constant
        self.setBackgroundRole(QPalette.ButtonText)
        self.setProperty("primary", "True")

    def on_click(self):
        self.handler(self.name, self.constant)


class CalculatorOperatorButton(CalculatorButton):
    def __init__(self, name: str, handler, operator: Operator):
        super().__init__(name, name)
        self.handler = handler
        self.operator = operator

    def on_click(self):
        self.handler(self.name, self.operator)


class CalculatorActionButton(CalculatorButton):
    def __init__(self, name, handler, action: Action, key_stroke=None):
        super().__init__(name, key_stroke)
        self.handler = handler
        self.action = action

    def on_click(self):
        self.handler(self.name, self.action)
