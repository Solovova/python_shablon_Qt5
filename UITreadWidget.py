from ui.ui_thread import Ui_Thread
from PyQt5 import QtCore, QtGui, QtWidgets

class UITreadWidget(QtWidgets.QWidget, Ui_Thread):
    def __init__(self, parent=None):
        super(UITreadWidget, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click)

    def click(self):
        print("click")
        self.lineEdit.setText("LLLLL")