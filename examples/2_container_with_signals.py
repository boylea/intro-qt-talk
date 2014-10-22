from PyQt4 import QtGui, QtCore

class MyWidget(QtGui.QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()

        layout = QtGui.QVBoxLayout()

        self.field = QtGui.QLineEdit()
        self.prompt = QtGui.QLabel("Amy says:")
        self.label = QtGui.QLabel("")

        layout.addWidget(self.field)
        layout.addWidget(self.prompt)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.field.textChanged.connect(self.amySays)

    def amySays(self, text):
        self.label.setText(text + ' !!!')


if __name__ == '__main__':
    
    app = QtGui.QApplication([])

    my_widget = MyWidget()
    my_widget.show()

    app.exec_()