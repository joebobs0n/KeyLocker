#!/usr/bin/python3

from PyQt5 import QtWidgets
from src.LocalApp import LocalApp
import sys, os

if __name__ == '__main__':
    os.chdir(sys.path[0])

    app = QtWidgets.QApplication([])
    win = LocalApp()
    win.show()
    sys.exit(app.exec_())
