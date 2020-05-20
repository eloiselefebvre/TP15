from PySide2.QtWidgets import *
from PySide2.QtGui import *

class LabeledTextField(QWidget):
    def __init__(self,text):
        QWidget.__init__(self)

        self.setMaximumSize(400,500)

        self.layout = QHBoxLayout()
        self.label = QLabel()
        self.TextEdit = QTextEdit()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.TextEdit)

        self.config = ConfigurationDialog()
        self.layout.addWidget(self.config)

class ConfigurationDialog(QDialog) :
    def __init__(self):

        self.layout = QVBoxLayout()
        self.obj1 = LabeledTextField('IP adress')
        self.obj2 = LabeledTextField('User')
        self.obj3 = LabeledTextField ('Password')

        self.layout.addWidget(self.obj1)
        self.layout.addWidget(self.obj2)
        self.layout.addWidget(self.obj3)


if __name__ == '__main__':
    app = QApplication ([])
    LTF = LabeledTextField('Configuration')
    LTF.show()
    app.exec_()



