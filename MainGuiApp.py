from Threads.ThreadMain import ThreadMain
from contextlib import nullcontext
from PyQt5 import QtWidgets
from ui.ui_mainWindow import Ui_MainWindow

from file.FileWork import FileWork
import subprocess
import io
import win32api
import win32gui

from PyQt5 import QtCore, QtGui, QtWidgets
from UITreadWidget import UITreadWidget


class MainGuiApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainGuiApp, self).__init__(parent)
        self.setupUi(self)



        itemN = QtWidgets.QListWidgetItem()
        widget = UITreadWidget()

        # itemN.setSizeHint(QtCore.QSize(212, 40))
        
        itemN.setSizeHint(widget.size())
        self.listWidget.addItem(itemN)
        self.listWidget.setItemWidget(itemN, widget)

        itemN = QtWidgets.QListWidgetItem()
        widget = UITreadWidget()
        # itemN.setSizeHint(QtCore.QSize(212, 40))
        itemN.setSizeHint(widget.size())
        self.listWidget.addItem(itemN)
        self.listWidget.setItemWidget(itemN, widget)

        self.pushButton_1.clicked.connect(self.say_hello)
        self.pushButton_2.clicked.connect(self.runScript)
        self.pushButton_TestTread.clicked.connect(self.runThread)

    def say_hello(self):   
        paths = ["C:\plot","E:\plot1","F:\plot2","F:\plotall","G:\plot","E:\plotall"]
        fileWork: FileWork = FileWork(paths)
        fileWork.fillPrintDublicates()


    def runScript(self):
        # scrname = "C:\\prog\\pyth\\python_shablon_Qt5\\scripts\\Tread1.ps1"
        # p = subprocess.Popen(['powershell.exe', scrname], stdout=subprocess.PIPE)

        # f = open("tread1.txt", "a")
        
        # for line in io.TextIOWrapper(p.stdout, encoding="utf-8"):  # or another encoding
        #     f.write(line)
        #     print(line)
        # f.close()
        
        whnd = win32gui.FindWindowEx(None, None, None, 'Tread1')
        if not (whnd == 0):
            # rect = win32gui.GetWindowRect(whnd)
            # rect.left = 0
            # rect.top = 0
            # rect.right = 100
            # rect.bottom = 100
            print(win32gui.GetWindowRect(whnd))
        

            print('FOUND!')
        print("Ennnnnd")
    
    def runThread(self):
        print("RunThread")
        self.thread1 = ThreadMain()
        self.thread1.start()
        #self.thread1.join()