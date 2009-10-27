# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from ui_main import Ui_MainWindow
from utils import Utils

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listSearch.setVisible(False)
        self.connect(self.ui.actionAbout  , QtCore.SIGNAL('triggered()')                      , self.actionAbout_triggered    )
        self.connect(self.ui.actionQuit   , QtCore.SIGNAL('triggered()')                      , QtCore.SLOT('close()')        )
        self.connect(self.ui.editSearch   , QtCore.SIGNAL('textChanged(QString)')             , self.editSearch_textChanged   )
        self.connect(self.ui.buttonSearch , QtCore.SIGNAL('clicked()')                        , self.buttonSearch_clicked     )
        self.connect(self.ui.editSearch   , QtCore.SIGNAL('returnPressed()')                  , self.buttonSearch_clicked     )
        self.connect(self.ui.listSearch   , QtCore.SIGNAL('itemActivated(QListWidgetItem *)') , self.listSearch_itemActivated )

    def actionAbout_triggered(self):
        box = QtGui.QMessageBox()
        box.setStandardButtons(QtGui.QMessageBox.Ok)
        box.setIconPixmap( QtGui.QPixmap( ":/icons/cliptor.png" ) )
        box.setText( u"Cliptor\n\nCopyright (c) 2009\n\nPavol Rusnák" )
        box.setWindowTitle("About Cliptor")
        box.exec_()

    def listSearch_itemActivated(self, i):
        self.ui.editSearch.setText(i.text())
        self.buttonSearch_clicked()

    def editSearch_textChanged(self, s):
        self.ui.listSearch.setVisible( s != "" )
        self.ui.listSearch.clear()
        for i in Utils.getSuggestions(s):
            self.ui.listSearch.addItem(i)

    def buttonSearch_clicked(self):
        s = self.ui.editSearch.text()
        if s == "":
            return
        self.ui.listSearch.setVisible(False)
        self.ui.listSearch.clear()
        print 'searching for ... %s' %  s
