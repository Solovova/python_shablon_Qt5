from PyQt5 import QtWidgets
import ui_mainWindow

from file.FileWork import FileWork

class MainGuiApp(QtWidgets.QMainWindow, ui_mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainGuiApp, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.say_hello)

    def say_hello(self):   
        paths = ["C:\plot","E:\plot1","F:\plot2","F:\plotall","G:\plot","E:\plotall"]
        fileWork: FileWork = FileWork(paths)
        fileWork.printAllFiles()