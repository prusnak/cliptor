# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from result_ui import Ui_widgetResult
from datetime import timedelta, datetime
from utils import Utils, THUMBDIR

class WidgetResult(QtGui.QWidget):

    def __init__(self, parent, listA, listB):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_widgetResult()
        self.ui.setupUi(self)
        self.vid = None
        self.title = None
        self.listA = listA
        self.listB = listB
        self.connect(self.ui.buttonA, QtCore.SIGNAL('clicked()'), self.buttonA_clicked )
        self.connect(self.ui.buttonB, QtCore.SIGNAL('clicked()'), self.buttonB_clicked )

    def buttonA_clicked(self):
        i = QtGui.QListWidgetItem(self.title)
        i.setData(QtCore.Qt.UserRole, self.vid)
        streams = Utils.getStreams(self.vid)
        i.setData(QtCore.Qt.UserRole+1, streams)
        self.listA.addItem(i)

    def buttonB_clicked(self):
        i = QtGui.QListWidgetItem(self.title)
        i.setData(QtCore.Qt.UserRole, self.vid)
        streams = Utils.getStreams(self.vid)
        i.setData(QtCore.Qt.UserRole+1, streams)
        self.listB.addItem(i)

    def setData(self, data):
        if data == None:
            self.setVisible(False)
            return
        else:
            self.setVisible(True)
        self.vid = data['vid']
        self.title = data['title']
        self.ui.labelAuthor.setText( data['author'] )
        delta = datetime.now() - data['published']
        if delta.days >= 365*2:
            delta = str(delta.days / 365) + ' years ago'
        elif delta.days >= 365:
            delta = '1 year ago'
        elif delta.days >= 30*2:
            delta = str(delta.days / 30) + ' months ago'
        elif delta.days >= 30:
            delta = '1 month ago'
        elif delta.days > 1:
            delta = str(delta.days) + ' days ago'
        elif delta.days == 1:
            delta = 'yesterday'
        else:
            delta = 'today'
        self.ui.labelPublished.setText( delta )
        self.ui.labelTitle.setText( data['title'] )
        self.ui.labelDesc.setText( data['desc'] )
        self.ui.labelLength.setText( "%d:%02d" % (data['length'] / 60, data['length'] % 60) )
        views = data['views']
        if views > 1000000000:
            views = "%d.%03d.%03d.%03d" % ( views / 1000000000 , views / 1000000 % 1000, views / 1000 % 1000, views % 1000)
        elif views > 1000000:
            views = "%d.%03d.%03d" % ( views / 1000000 , views / 1000 % 1000, views % 1000)
        elif views > 1000:
            views = "%d.%03d" % ( views / 1000, views % 1000)
        else:
            views = "%d" % views
        self.ui.labelViews.setText( views + ' views' )
        ratingwidth = int( data['rating'] * 16)
        rate0 = QtGui.QPixmap(':icons/rating0.png')
        rate1 = QtGui.QPixmap(':icons/rating1.png')
        rating = QtGui.QPixmap(80,16)
        rating.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter()
        painter.begin(rating)
        painter.drawPixmap(0,0,rate1,0,0,ratingwidth,16)
        painter.drawPixmap(ratingwidth,0,rate0,ratingwidth,0,80-ratingwidth,16)
        painter.end()
        self.ui.imageRating.setPixmap(rating)
        thumb = QtGui.QPixmap(':icons/nothumb.png')
        self.ui.imageThumb.setPixmap(thumb)
        # TODO: put download in separate thread + set callback to set image
        Utils.downloadThumb(self.vid)
        # TODO: the following two line should be set as a callback when download above is finished
        thumb = QtGui.QPixmap( THUMBDIR + self.vid + '.jpg' )
        self.ui.imageThumb.setPixmap(thumb)
