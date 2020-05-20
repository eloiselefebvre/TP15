from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Window(QWidget) :

    def __init__(self):
        QWidget.__init__(self)


        self.setWindowTitle('SQL CLient')
        self.setMinimumSize(600,400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.buttonsPanel = ButtonPanel()
        self.layout.addWidget(self.buttonsPanel)

        self.notifPanel = QTextEdit()
        self.layout.addWidget(self.notifPanel)

        self.resultTable = QTableWidget()
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.resultTable)


class ButtonPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout=QHBoxLayout()

        self.button1=QPushButton('Configure')
        self.button2=QPushButton('Connect')
        self.button3=QPushButton('Disconnect')

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

        self.setLayout(self.layout)




if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
