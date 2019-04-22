import gettext
import sys

from PySide2 import QtWidgets, QtGui, QtCore

from ptr42.components.calculator import Calculator
from ptr42.components.keyboards.default import get_default_keyboard

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    try:
        country_code = QtCore.QLocale().name()
        lang = gettext.translation("messages", "./translations", [country_code])
        lang.install()
    except FileNotFoundError:
        lang = gettext.translation("messages", "./translations", ["en_US"])
        lang.install()

    file = QtCore.QFile("themes/native-theme.css")
    file.open(QtCore.QFile.ReadOnly)
    style = QtCore.QTextStream(file).readAll()
    app.setStyleSheet(style)

    container = QtWidgets.QWidget()
    container.setObjectName("container")
    container.setSizePolicy(QtWidgets.QSizePolicy.Maximum,
                            QtWidgets.QSizePolicy.Maximum)

    container.setWindowIcon(QtGui.QIcon("logo.svg"))
    container.setWindowTitle("42ptr calc")
    container.resize(650, 650)
    containerLayout = QtWidgets.QVBoxLayout()
    containerLayout.setMargin(20)

    calculator = Calculator()
    calculator.set_keyboard(get_default_keyboard(calculator))
    containerLayout.addWidget(calculator)

    container.setLayout(containerLayout)
    container.show()

    sys.exit(app.exec_())
