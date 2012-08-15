#!/usr/bin/python

import sys
from PySide import QtGui
from main import MainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
