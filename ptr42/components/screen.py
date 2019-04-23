from PySide2 import QtWidgets, QtCore


class CalculatorScreen(QtWidgets.QLineEdit):
    """
    Trieda reprezentujuca displej kalkulacky
    """

    def __init__(self):
        """
        Vytvori displej kalkulacky
        """
        super().__init__()
        self.selectionChanged.connect(self._onSelect)
        self._lastSelection = (-1, -1)
        self._blockOnSelect = False
        self.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.setLayout(QtWidgets.QHBoxLayout())

    def _onSelect(self):
        if self._blockOnSelect:
            self._blockOnSelect = False
            return

        if self.hasFocus():
            self._lastSelection = (self.selectionStart(), self.selectionLength())
        else:
            self.setSelection(*self._lastSelection)

    def setSelection(self, start: int, count: int):
        """
        Oznaci text v zadanom rozmadzi

        :param start: pociatocny index
        :param count: pocet znakov na oznacenie
        """
        if start == -1:
            self.deselect()
        else:
            self._blockOnSelect = True
            super(CalculatorScreen, self).setSelection(start, count)

    def deselect(self):
        """
        Odznaci text
        """
        self._blockOnSelect = True
        super(CalculatorScreen, self).deselect()

    def getCursorPositions(self):
        """
        Vrati poziciu kurzoru v tvare (start, end)

        :return: tuple so strukturou (start, end), co reprezentuje poziciu kurzoru
        """
        if self.hasSelectedText():
            return self.selectionStart(), self.selectionEnd()
        else:
            return self.cursorPosition(), self.cursorPosition()

    def insertText(self, text: str):
        """
        Vlozi text na poziciu aktualneho kurzoru, alebo ak je oznaceny text, tak
        ho nahradi

        :param text: text na vlozenie
        :return: poziciu zaciatku textu na displeji
        """
        originalText = self.text()
        start, end = self.getCursorPositions()
        self.setText(originalText[:start] + text + originalText[end:])
        self.deselect()
        self.setCursorPosition(start + len(text))
        return start

    def markError(self):
        """
        Oznaci chybny stav kalkulacky
        """
        self.setProperty("hasError", "True")
        self.style().unpolish(self)
        self.style().polish(self)

    def unmarkError(self):
        """
        Zrusi chybny stav kalkulacky
        """
        self.setProperty("hasError", "False")
        self.style().unpolish(self)
        self.style().polish(self)
