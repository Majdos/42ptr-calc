from enum import Enum
from string import ascii_letters

from PySide2 import QtWidgets

from ptr42.components.calculator_button import Action
from ptr42.components.calculator_keyboard import CalculatorKeyboard
from ptr42.components.screen import CalculatorScreen
from ptr42.math_language.parser.expression import Constant, Operator, Function


class CalculatorState(Enum):
    IN_FUNCTION = 1
    BUILDING_NUMBER = 2


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._keyboard = None
        self._layout = None
        self._screen = None
        self._layout = QtWidgets.QVBoxLayout()
        self._screen = CalculatorScreen()
        self._layout.setStretchFactor(self._screen, 2)
        self._layout.addWidget(self._screen)

    def new_keyboard_template(self):
        keyboard = CalculatorKeyboard()
        keyboard.set_handlers(self._on_function_input, self._on_operator_input, self._on_constant_input,
                              self._on_action_input)
        return keyboard

    def set_keyboard(self, keyboard: CalculatorKeyboard):
        self._keyboard = keyboard
        self._layout.setStretchFactor(keyboard, 5)
        self._layout.addWidget(keyboard)
        self.setLayout(self._layout)

    def has_selected_text(self):
        return self._screen.hasSelectedText()

    def _on_function_input(self, name: str, function: Function):
        arguments = ", ".join(ascii_letters[:function.arg_count])
        function_notation = f"{name}({arguments})"
        old_pos = self._screen.insertText(function_notation)
        self._screen.setSelection(old_pos + len(name) + 1, 1)

    def _on_operator_input(self, name: str, operator: Operator):
        self._screen.insertText(name)

    def _on_constant_input(self, name: str, constant: Constant):
        self._screen.insertText(constant.name)

    def _on_action_input(self, name: str, action: Action):
        if action == Action.CLEAR:
            self._screen.setText("")
        # elif action == Action.EVALUATE:
        #   todo: pouzije sa Lexer
        # elif action == Action.TABULATOR:
        #   todo: pouzije sa Lexer
        # elif action == Action.TABULATOR_REVERSED:
        #   todo: pouzije sa Lexer
