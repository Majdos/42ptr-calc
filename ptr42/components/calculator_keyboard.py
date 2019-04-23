from PySide2 import QtWidgets, QtGui, QtCore

import ptr42.components.calculator_button as buttons
from ptr42.math_language.parser.expression import Constant, Function, Operator


class CalculatorKeyboard(QtWidgets.QWidget):
    """
    Trieda reprezentujuca klavesnicu kalkulacky
    """

    def __init__(self, spacing: int = 5):
        """
        Vyrvori klavesovu maticu s medzerami o hodnoty 'spacing'

        :param spacing: ciselna hodnota medzier
        """
        super().__init__()

        self._on_function_input = None
        self._on_operator_input = None
        self._on_constant_input = None
        self._on_action_input = None

        self._layout = QtWidgets.QGridLayout()
        self._layout.setSpacing(spacing)
        self._layout.setMargin(0)
        self.setLayout(self._layout)

    def set_handlers(self, on_function_input, on_operator_input, on_constant_input, on_action_input) -> None:
        """
        Nastavi ovladac klavesovych udalosti

        :param on_function_input: funkcia, ktora sa zavola, ked dojde ku kliku na funkciu
        :param on_operator_input: funkcia, ktora sa zavola, ked dojde ku kliku na operator
        :param on_constant_input: funkcia, ktora sa zavola, ked dojde ku kliku na konstantu
        :param on_action_input: funkcia, ktora sa zavola, ked dojde ku kliku na akciu
        """
        self._on_function_input = on_function_input
        self._on_operator_input = on_operator_input
        self._on_constant_input = on_constant_input
        self._on_action_input = on_action_input

    def register_function(self, name: str, function: Function, row: int, col: int):
        """
        Zaregistruje funkciu do kalkulacky a prida tlacitko do kalkulacky

        :param name: text tlacitka
        :param function: funkcia pre tlacitko
        :param row: riadok, kde bude umiestene tlacitko
        :param col: stlpec, kde bude umiestene tlacitko
        """
        button = buttons.CalculatorFunctionButton(
            name, self._on_function_input, function)
        self._layout.addWidget(button, row, col)

    def register_operator(self, name: str, operator: Operator, row: int, col: int):
        """
        Zaregistruje operator do kalkulacky a prida tlacitko do kalkulacky

        :param name: text tlacitka
        :param operator: funkcia pre tlacitko
        :param row: riadok, kde bude umiestene tlacitko
        :param col: stlpec, kde bude umiestene tlacitko
        """
        button = buttons.CalculatorOperatorButton(
            name, self._on_operator_input, operator.operator_func)
        self._layout.addWidget(button, row, col)

    def register_constant(self, name: str, constant: Constant, row: int, col: int):
        """
        Zaregistruje konstantu do kalkulacky a prida tlacitko do kalkulacky

        :param name: text tlacitka
        :param constant: funkcia pre tlacitko
        :param row: riadok, kde bude umiestene tlacitko
        :param col: stlpec, kde bude umiestene tlacitko
        """
        button = buttons.CalculatorConstantButton(
            name, self._on_constant_input, constant)
        self._layout.addWidget(button, row, col)

    def register_action(self, name: str, action: buttons.Action, row: int, col: int):
        """
        Zaregistruje akciu do kalkulacky a prida tlacitko do kalkulacky

        :param name: text tlacitka
        :param action: funkcia pre tlacitko
        :param row: riadok, kde bude umiestene tlacitko
        :param col: stlpec, kde bude umiestene tlacitko
        """
        button = buttons.CalculatorActionButton(
            name, self._on_action_input, action)
        self._layout.addWidget(button, row, col)

    def register_hidden_action(self, key_stroke: QtCore.Qt.Key, action: buttons.Action):
        """
        Zaregistruje skrytu akciu do kalkulacky a neprida tlacitko do kalkulacky

        :param key_stroke: klavesova skratka akcie
        :param action: akcia
        """
        self.register_hidden_action_with_inverse(key_stroke, action, buttons.Action.NONE)

    def register_hidden_action_with_inverse(self, key_stroke: QtCore.Qt.Key, action: buttons.Action,
                                            reversed_action: buttons.Action):
        """
        Zaregistruje skrytu akciu do kalkulacky s inverziou a neprida tlacitko do kalkulacky

        :param key_stroke: klavesova skratka akcie (inverzna akcia sa vykona po drzani shiftu)
        :param action: akcia
        """
        QtWidgets.QShortcut(QtGui.QKeySequence(key_stroke), self,
                            self._propagate_hidden_action(action))
        QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Shift | key_stroke), self,
                            self._propagate_hidden_action(reversed_action))

    def _propagate_hidden_action(self, action: buttons.Action):
        def on_action(): self._on_action_input(None, action)

        return on_action

    def get_layout(self):
        """
        Vrati layout klavesnice

        :return: layout klavesnice
        """
        return self._layout
