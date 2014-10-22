import sys
from PySide import QtGui, QtCore, QtWebKit

class Browser(QtGui.QWidget):
    def __init__(self):
        super(Browser, self).__init__()

        self.page = QtWebKit.QWebView()
        self.addressBar = QtGui.QLineEdit("http://www.amyboyle.ninja")

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.addressBar)
        layout.addWidget(self.page)
        self.setLayout(layout)

        self.addressBar.returnPressed.connect(self.loadAddress)

    def loadAddress(self):
        address = self.addressBar.text()
        self.page.load(QtCore.QUrl(address))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())