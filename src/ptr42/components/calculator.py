from enum import Enum
from string import ascii_letters

from PySide2 import QtWidgets

from ptr42.components.calculator_button import Action
from ptr42.components.calculator_keyboard import CalculatorKeyboard
from ptr42.components.screen import CalculatorScreen
from ptr42.math_language.lexer.default_lexer import get_default_lexer
from ptr42.math_language.lexer.expression_error import ExpressionError
from ptr42.math_language.parser.expression import Constant, Operator, Function
from ptr42.math_language.parser.parser import MathParser
from ptr42.math_language.parser.parser_error import ParserError


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
        self._error_label = QtWidgets.QLabel()
        self._error_label.setObjectName("error-label")

        self._layout.addWidget(self._error_label)

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

    def _mark_error(self, error_msg: str):
        self._screen.markError()
        self._error_label.setText(error_msg)
        self.style().unpolish(self)
        self.style().polish(self)

    def _unmark_error(self):
        self._screen.unmarkError()
        self._error_label.setText("")
        self.style().unpolish(self)
        self.style().polish(self)

    def _on_function_input(self, name: str, function: Function):
        self._unmark_error()
        arguments = ", ".join(ascii_letters[:function.arg_count])
        function_notation = f"{name}({arguments})"
        old_pos = self._screen.insertText(function_notation)
        self._screen.setSelection(old_pos + len(name) + 1, 1)

    def _on_operator_input(self, name: str, operator: Operator):
        self._unmark_error()
        self._screen.insertText(name)

    def _on_constant_input(self, name: str, constant: Constant):
        self._unmark_error()
        self._screen.insertText(constant.name)

    def _on_action_input(self, name: str, action: Action):
        self._unmark_error()
        if action == Action.CLEAR:
            self._screen.setText("")
        elif action == Action.EVALUATE:
            try:
                lexer = get_default_lexer(self._screen.text())
                tokens = list(lexer.generate_tokens())

                if not tokens:
                    self._screen.setText(_("Zadajte vyraz"))
                    return

                parser = MathParser(tokens, lexer.get_operators())
                ast = parser.parse()
                self._screen.setText(str(ast.evaluate()))
            except ExpressionError as e:
                self._mark_error(str(e))
            except ValueError as e:
                self._mark_error(str(e))
            except ParserError:
                self._mark_error(_("Chyba vyrazu"))

        elif action == Action.DECIMAL:
            self._screen.insertText(".")
