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

        self.field.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, event):
        QtGui.QLineEdit.keyPressEvent(self.field, event)
        if event.key() == QtCore.Qt.Key_Backspace:
            self.label.setText(self.label.text()[:-1])
        else:
            self.label.setText(self.label.text() + event.text())


if __name__ == '__main__':
    
    app = QtGui.QApplication([])

    my_widget = MyWidget()
    my_widget.show()

    app.exec_()