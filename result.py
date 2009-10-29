# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from ui_result import Ui_widgetResult

class WidgetResult(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_widgetResult()
        self.ui.setupUi(self)
        self.vid = None

    def setData(self, data):
        self.vid = data['vid']
        self.ui.labelAuthor.setText( data['author'] )
        self.ui.labelPublished.setText( data['published'] )
        self.ui.labelTitle.setText( data['title'] )
        self.ui.labelDesc.setText( data['desc'] )
        self.ui.labelLength.setText( "%d:%d" % (data['length'] / 60, data['length'] % 60) )
        self.ui.labelViews.setText( str(data['views']) + ' views' )
        ratingwidth = int( data['rating'] * 16)
        rate0 = QtGui.QPixmap(':icons/rating0.png')
        rate1 = QtGui.QPixmap(':icons/rating1.png')
        rating = QtGui.QPixmap(5*16,16)
        rating.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter()
        painter.begin(rating)
#        painter.drawPixmap(0,0,rate1,0,0,ratingwidth-1,16)
        painter.drawPixmap(ratingwidth,0,rate0,80-ratingwidth,0,80-ratingwidth,16)
        painter.end()
        self.ui.imageRating.setPixmap(rating)
        #       'thumbs': [ ('http://i.ytimg.com/vi/%s/' % vid) + str(i) + '.jpg' for i in range(1,4) ]
