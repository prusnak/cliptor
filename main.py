# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from ui_main import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.actionAbout, QtCore.SIGNAL('triggered()'), self.doAbout)
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

    def doAbout(self):
        box = QtGui.QMessageBox()
        box.setStandardButtons(QtGui.QMessageBox.Ok)
        box.setIconPixmap( QtGui.QPixmap( ":/icons/cliptor.png" ) )
        box.setText( u"Cliptor\n\nCopyright (c) 2009\n\nPavol Rusnák" )
        box.setWindowTitle("About Cliptor")
        box.exec_()
