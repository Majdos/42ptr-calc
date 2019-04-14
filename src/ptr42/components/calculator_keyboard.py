from PySide2 import QtWidgets, QtGui, QtCore

import ptr42.components.calculator_button as buttons
from ptr42.math_language.parser.expression import Constant, Function, Operator


class CalculatorKeyboard(QtWidgets.QWidget):
    def __init__(self, spacing: int = 5):
        super().__init__()

        self._on_function_input = None
        self._on_operator_input = None
        self._on_constant_input = None
        self._on_action_input = None

        self._layout = QtWidgets.QGridLayout()
        self._layout.setSpacing(spacing)
        self._layout.setMargin(0)
        self.setLayout(self._layout)

    def set_handlers(self, on_function_input, on_operator_input, on_constant_input, on_action_input):
        self._on_function_input = on_function_input
        self._on_operator_input = on_operator_input
        self._on_constant_input = on_constant_input
        self._on_action_input = on_action_input

    def register_function(self, name: str, function: Function, row: int, col: int):
        button = buttons.CalculatorFunctionButton(
            name, self._on_function_input, function)
        self._layout.addWidget(button, row, col)

    def register_operator(self, name: str, operator: Operator, row: int, col: int):
        button = buttons.CalculatorOperatorButton(
            name, self._on_operator_input, operator.operator_func)
        self._layout.addWidget(button, row, col)

    def register_constant(self, name: str, constant: Constant, row: int, col: int):
        button = buttons.CalculatorConstantButton(
            name, self._on_constant_input, constant)
        self._layout.addWidget(button, row, col)

    def register_action(self, name: str, action: buttons.Action, row: int, col: int):
        button = buttons.CalculatorActionButton(
            name, self._on_action_input, action)
        self._layout.addWidget(button, row, col)

    def register_hidden_action(self, key_stroke: QtCore.Qt.Key, action: buttons.Action):
        self.register_hidden_action_with_inverse(key_stroke, action, buttons.Action.NONE)

    def register_hidden_action_with_inverse(self, key_stroke: QtCore.Qt.Key, action: buttons.Action,
                                            reversed_action: buttons.Action):
        QtWidgets.QShortcut(QtGui.QKeySequence(key_stroke), self,
                            self.propagate_hidden_action(action))
        QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Shift | key_stroke), self,
                            self.propagate_hidden_action(action))

    def propagate_hidden_action(self, action: buttons.Action):
        def on_action(): self._on_action_input(None, action)

        return on_action

    def get_layout(self):
        return self._layout
