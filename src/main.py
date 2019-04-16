import sys

from PySide2 import QtWidgets, QtGui

from ptr42.components.calculator import Calculator
from ptr42.components.keyboards.default import get_default_keyboard

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    container = QtWidgets.QWidget()
    container.setSizePolicy(QtWidgets.QSizePolicy.Maximum,
                            QtWidgets.QSizePolicy.Maximum)

    container.setWindowIcon(QtGui.QIcon("baseline_whatshot_black_48dp.png"))
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
