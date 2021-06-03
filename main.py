from PyQt5.QtWidgets import QApplication
import sys
from MainGuiApp import MainGuiApp

def main():
    app = QApplication(sys.argv)
    form = MainGuiApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()