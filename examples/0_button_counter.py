from PyQt4 import QtGui

class MyButton(QtGui.QPushButton):
    nclicks = 0
    def mousePressEvent(self, event):
        super(MyButton, self).mousePressEvent(event)
        self.nclicks += 1
        self.setText("pressed {}".format(self.nclicks))

if __name__ == '__main__':
    
    app = QtGui.QApplication([])

    hello_widget = MyButton("click me")
    hello_widget.show()

    app.exec_()