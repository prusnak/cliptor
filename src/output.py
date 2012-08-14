try:
    from PyQt4 import QtGui
except:
    from PySide import QtGui
from output_ui import Ui_WindowOutput

class WindowOutput(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_WindowOutput()
        self.ui.setupUi(self)
