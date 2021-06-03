from typing import Mapping
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import ui_mainWindow
import os

class recFileInfo(object): 
    def __init__(self, path, name, size): 
        self.path = path
        self.name = name 
        self.size = size

def fillFiles(paths):
    result = []
    for path in paths:
        file_list = os.listdir(path)
        for file_name in file_list:
            result.append(recFileInfo(path, file_name, os.stat(path+"\\"+file_name).st_size))

    return result



class ExampleApp(QtWidgets.QMainWindow, ui_mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.say_hello)

    def say_hello(self):   
        paths = ["C:\plot","E:\plot1","F:\plot2","F:\plotall","G:\plot","E:\plotall"]

        file_list_all = fillFiles(paths)
        file_list = []
        file_list_find_dublicate= []
        for frecord in file_list_all:
            if frecord.name in file_list_find_dublicate:
                continue
            if frecord.name in file_list:
                file_list_find_dublicate.append(frecord.name)
            else:
                file_list.append(frecord.name)
        
        num = 1
        for duplicate_name in file_list_find_dublicate:
            first = True
            for frecord in file_list_all:
                if frecord.name != duplicate_name:
                    continue

                if first:
                    first = False
                    print(str(num) + "  " + duplicate_name)

                print(frecord.path + "  :" + str(frecord.size))
            num=num+1


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()