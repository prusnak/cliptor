# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from ui_main import Ui_MainWindow
from result import WidgetResult
from utils import Utils, SEARCHRESULTS

class MainWindow(QtGui.QMainWindow):

    playingA = False
    playingB = False
    resultWidgets = []

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listSearch.setVisible(False)
        self.ui.scrollResult.setVisible(False)
        self.connect(self.ui.actionAbout  , QtCore.SIGNAL('triggered()')                      , self.actionAbout_triggered    )
        self.connect(self.ui.actionQuit   , QtCore.SIGNAL('triggered()')                      , QtCore.SLOT('close()')        )
        self.connect(self.ui.editSearch   , QtCore.SIGNAL('textChanged(QString)')             , self.editSearch_textChanged   )
        self.connect(self.ui.buttonSearch , QtCore.SIGNAL('clicked()')                        , self.buttonSearch_clicked     )
        self.connect(self.ui.editSearch   , QtCore.SIGNAL('returnPressed()')                  , self.buttonSearch_clicked     )
        self.connect(self.ui.listSearch   , QtCore.SIGNAL('itemActivated(QListWidgetItem *)') , self.listSearch_itemActivated )
        self.connect(self.ui.buttonPlayA  , QtCore.SIGNAL('clicked()')                        , self.buttonPlayA_clicked      )
        self.connect(self.ui.buttonPlayB  , QtCore.SIGNAL('clicked()')                        , self.buttonPlayB_clicked      )
        self.connect(self.ui.buttonCueA   , QtCore.SIGNAL('clicked()')                        , self.buttonCueA_clicked       )
        self.connect(self.ui.buttonCueB   , QtCore.SIGNAL('clicked()')                        , self.buttonCueB_clicked       )
        for i in range(0, SEARCHRESULTS):
            self.resultWidgets.append( WidgetResult(self.ui.scrollResultContents) )
            self.resultWidgets[i].setGeometry(QtCore.QRect(0, i * self.resultWidgets[i].height(), self.resultWidgets[i].width(), self.resultWidgets[i].height()));
            self.resultWidgets[i].setObjectName( "result" + str(i) )

    def actionAbout_triggered(self):
        box = QtGui.QMessageBox()
        box.setStandardButtons(QtGui.QMessageBox.Ok)
        box.setIconPixmap( QtGui.QPixmap( ':/icons/cliptor.png' ) )
        box.setText( u'Cliptor\n\nCopyright (c) 2009\n\nPavol Rusnák' )
        box.setWindowTitle('About Cliptor')
        box.exec_()

    def listSearch_itemActivated(self, i):
        self.ui.editSearch.setText(i.text())
        self.buttonSearch_clicked()

    def editSearch_textChanged(self, s):
        self.ui.scrollResult.setVisible(False)
        self.ui.listSearch.setVisible( s != '' )
        self.ui.listSearch.clear()
        for i in Utils.getSuggestions(s):
            self.ui.listSearch.addItem(i)

    def buttonSearch_clicked(self):
        s = self.ui.editSearch.text()
        if s == "":
            return
        self.ui.listSearch.setVisible(False)
        self.ui.listSearch.clear()
        vids = Utils.getVideos(s)
        for i in range(0, SEARCHRESULTS):
            if i < len(vids):
                self.resultWidgets[i].setData(vids[i])
            else:
                self.resultWidgets[i].setData(None)
        self.ui.scrollResultContents.setGeometry(QtCore.QRect(0,0,self.resultWidgets[0].width(),self.resultWidgets[0].height()*len(vids)))
        self.ui.scrollResult.setVisible(True)

    def buttonPlayA_clicked(self):
        self.playingA = not self.playingA
        self.ui.buttonPlayA.setIcon( Utils.getIcon(self.playingA and 'pause' or 'play') )

    def buttonPlayB_clicked(self):
        self.playingB = not self.playingB
        self.ui.buttonPlayB.setIcon( Utils.getIcon(self.playingB and 'pause' or 'play') )

    def buttonCueA_clicked(self):
        self.ui.buttonCueA.setIcon( Utils.getIcon('cue-go') )

    def buttonCueB_clicked(self):
        self.ui.buttonCueB.setIcon( Utils.getIcon('cue-go') )
