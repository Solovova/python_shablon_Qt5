from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import ui_mainWindow

class ExampleApp(QtWidgets.QMainWindow, ui_mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.say_hello)

    def say_hello(self):   
        self.label.setText('dd')
        self.textBrowser.setText('sdsafasf')
        print("Button clicked, Hello!")

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()