import gettext
import sys

from PySide2 import QtWidgets, QtGui, QtCore

from ptr42.components.calculator import Calculator
from ptr42.components.keyboards.default import get_default_keyboard


def main():

    app = QtWidgets.QApplication(sys.argv)
    try:
        country_code = QtCore.QLocale().name()
        lang = gettext.translation("messages", "resources/translations", [country_code])
        lang.install()
    except FileNotFoundError:
        lang = gettext.translation("messages", "resources/translations", ["en_US"])
        lang.install()

    file = QtCore.QFile("resources/themes/native-theme.css")
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
    container_layout = QtWidgets.QVBoxLayout()
    container_layout.setMargin(20)

    calculator = Calculator()
    calculator.set_keyboard(get_default_keyboard(calculator))
    container_layout.addWidget(calculator)

    container.setLayout(container_layout)
    container.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
