from contextlib import nullcontext
from PyQt5 import QtWidgets
import ui_mainWindow

from file.FileWork import FileWork
import subprocess
import io


class MainGuiApp(QtWidgets.QMainWindow, ui_mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainGuiApp, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.say_hello)
        self.pushButton_2.clicked.connect(self.runScript)

    def say_hello(self):   
        paths = ["C:\plot","E:\plot1","F:\plot2","F:\plotall","G:\plot","E:\plotall"]
        fileWork: FileWork = FileWork(paths)
        fileWork.printAllFiles()


    def runScript(self):
        scrname = "C:\\prog\\pyth\\python_shablon_Qt5\\scripts\\Tread1.ps1"
        p = subprocess.Popen(['powershell.exe', scrname], stdout=subprocess.PIPE)

        f = open("tread1.txt", "a")
        
        for line in io.TextIOWrapper(p.stdout, encoding="utf-8"):  # or another encoding
            f.write(line)
            print(line)
        f.close()
        print("Ennnnnd")