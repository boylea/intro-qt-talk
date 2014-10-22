from PyQt4 import QtGui

if __name__ == '__main__':
    
    app = QtGui.QApplication([])

    hello_widget = QtGui.QWidget()
    hello_widget.show()

    app.exec_()