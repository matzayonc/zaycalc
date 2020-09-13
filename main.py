import PySide2.QtWidgets as qtw

import sys


def showAlert(text):
    alert = qtw.QMessageBox()
    alert.setText(str(text))
    alert.exec_()


def getJebac(widget):
    layout = qtw.QVBoxLayout(widget)
    top = qtw.QPushButton('Pioter')
    bottom = qtw.QPushButton('Trąba')
    layout.addWidget(top)
    layout.addWidget(bottom)

    top.clicked.connect(lambda: showAlert('Jebac Piotera'))
    bottom.clicked.connect(lambda: showAlert('Jebać Trąbe'))


class Calculator:
    def __init__(self, widget):
        self.num = 0
        self.memory = None
        self.action = ''
        self.grid = qtw.QGridLayout(widget)
        self.grid.setSpacing(10)

        self.addAllNumbers()
        self.addActions()
        self.addEqualsAction()

    def addActions(self):
        def plusAction():
            self.memory = self.num
            self.num = 0
            self.action = '+'
            print('plus')

        def minusAction():
            self.memory = self.num
            self.num = 0
            self.action = '-'
            print('minus')

        plus = qtw.QPushButton("+")
        self.grid.addWidget(plus, 3, 3)
        plus.clicked.connect(plusAction)

        minus = qtw.QPushButton("-")
        self.grid.addWidget(minus, 2, 3)
        minus.clicked.connect(minusAction)

    def addEqualsAction(self):
        def equals():
            if self.action == '':
                print(self.num)
            elif self.action == '+':
                print(self.memory + self.num)
            elif(self.action == '-'):
                print(self.memory - self.num)

            self.action = ''
            self.memory = None
            self.num = 0

        button = qtw.QPushButton("=")
        self.grid.addWidget(button, 4, 3)
        button.clicked.connect(equals)

    def numberClick(self, number):
        self.num = self.num * 10 + number
        print(self.num)

    def addAllNumbers(self):
        for i in range(1, 10):
            self.addNumber(i)
        self.addNumber(0, 4, 0)

    def addNumber(self, number, forceX=None, forceY=None):
        x = forceX if forceX != None else 3-int((number-1)/3)
        y = forceY if forceY != None else (number-1) % 3

        button = qtw.QPushButton(str((number) % 10))
        button.clicked.connect(
            lambda state=None, j=number: self.numberClick((j) % 10))

        self.grid.addWidget(button, x, y)


if __name__ == '__main__':
    app = qtw.QApplication()
    window = qtw.QMainWindow()

    w = qtw.QWidget()

    w.show()

    calculator = Calculator(w)

    exit_code = app.exec_()
    sys.exit(exit_code)
