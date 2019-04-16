from PySide2 import QtCore

import ptr42.math42 as math42
from ptr42.components.calculator import Calculator
from ptr42.components.calculator_button import Action
from ptr42.math_language.parser.expression import Constant, Function, BinaryOperator

default_keyboard_rows = 5
default_keyboard_cols = 5


def get_default_keyboard(calculator: Calculator):
    keyboard = calculator.new_keyboard_template()
    for i in range(1, 4):
        for j in range(1, 4):
            key_value = str(3 * (i - 1) + j)
            keyboard.register_constant(key_value, Constant(key_value), default_keyboard_rows - i, j)

    keyboard.register_function("abs", Function(math42.absolute_number, 1), default_keyboard_rows,
                               default_keyboard_cols / 2 - 1)
    keyboard.register_constant("0", Constant("0"), default_keyboard_rows, default_keyboard_cols / 2)
    keyboard.register_action(QtCore.QLocale().decimalPoint(), Action.DECIMAL, default_keyboard_rows,
                             default_keyboard_cols / 2 + 1)

    keyboard.register_function("exp", Function(math42.natural_exponent, 1), default_keyboard_rows,
                               default_keyboard_cols / 2 - 2)

    keyboard.register_function("ln", Function(math42.ln, 1), default_keyboard_rows - 1,
                               default_keyboard_cols / 2 - 2)

    keyboard.register_function("sqrt", Function(math42.sqrt, 1), default_keyboard_rows - 2,
                               default_keyboard_cols / 2 - 2)

    keyboard.register_function("root", Function(math42.root, 2), default_keyboard_rows - 3,
                               default_keyboard_cols / 2 - 2)

    keyboard.register_function("fact", Function(math42.factorial, 1), default_keyboard_rows - 4,
                               default_keyboard_cols / 2 - 2)

    keyboard.register_action("=", Action.EVALUATE, default_keyboard_rows,
                             default_keyboard_cols / 2 + 2)

    keyboard.register_operator("+", BinaryOperator(math42.addition, 6), default_keyboard_rows - 1,
                               default_keyboard_cols / 2 + 2)

    keyboard.register_operator("-", BinaryOperator(math42.subtract, 6), default_keyboard_rows - 2,
                               default_keyboard_cols / 2 + 2)

    keyboard.register_operator("*", BinaryOperator(math42.multiplication, 5), default_keyboard_rows - 3,
                               default_keyboard_cols / 2 + 2)

    keyboard.register_operator("/", BinaryOperator(math42.multiplication, 5), default_keyboard_rows - 4,
                               default_keyboard_cols / 2 + 2)

    keyboard.register_action("CE", Action.CLEAR, default_keyboard_rows - 4,
                             default_keyboard_cols / 2 - 1)

    keyboard.register_hidden_action_with_inverse(QtCore.Qt.Key_Tab, Action.TABULATOR, Action.TABULATOR_REVERSED)

    return keyboard
