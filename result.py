# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from ui_result import Ui_widgetResult

class WidgetResult(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_widgetResult()
        self.ui.setupUi(self)
