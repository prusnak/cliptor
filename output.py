from PyQt4 import QtGui
from ui_output import Ui_WindowOutput

class WindowOutput(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_WindowOutput()
        self.ui.setupUi(self)
