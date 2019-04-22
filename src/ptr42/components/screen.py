from PySide2 import QtWidgets, QtCore

# style = """
# QLineEdit {{
#     padding-top: {verticalPadding}px;
#     padding-bottom: {verticalPadding}px;
#     padding-left: {horizontalPadding}px;
#     padding-right: {horizontalPadding}px;
#     margin-bottom: {verticalPadding}px;
#     font: normal {fontSize}px;
#     max-height: {maxHeight}px;
# }}
#
# QLineEdit[error=true] {{
#     border: 1px solid red;
# }}
# """

illegalStartStrings = {"0", "+"}


class CalculatorScreen(QtWidgets.QLineEdit):
    def __init__(self):
        super().__init__()
        self.selectionChanged.connect(self._onSelect)
        self.lastSelection = (-1, -1)
        self.blockOnSelect = False
        self.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.setLayout(QtWidgets.QHBoxLayout())

    def _onSelect(self):
        if self.blockOnSelect:
            self.blockOnSelect = False
            return

        if self.hasFocus():
            self.lastSelection = (self.selectionStart(), self.selectionLength())
        else:
            self.setSelection(*self.lastSelection)

    def setSelection(self, start: int, count: int):
        if start == -1:
            self.deselect()
        else:
            self.blockOnSelect = True
            super(CalculatorScreen, self).setSelection(start, count)

    def deselect(self):
        self.blockOnSelect = True
        super(CalculatorScreen, self).deselect()

    def getCursorPositions(self):
        if self.hasSelectedText():
            return self.selectionStart(), self.selectionEnd()
        else:
            return self.cursorPosition(), self.cursorPosition()

    def insertText(self, text: str):
        originalText = self.text()
        start, end = self.getCursorPositions()
        self.setText(originalText[:start] + text + originalText[end:])
        self.deselect()
        self.setCursorPosition(start + len(text))
        return start

    def markError(self):
        self.setProperty("hasError", "True")
        self.style().unpolish(self)
        self.style().polish(self)

    def unmarkError(self):
        self.setProperty("hasError", "False")
        self.style().unpolish(self)
        self.style().polish(self)
