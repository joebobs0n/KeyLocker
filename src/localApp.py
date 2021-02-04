#!/usr/bin/python3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class LocalApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('src/local_gui.ui', self)
        self.showFullScreen()

        self.password_button.clicked.connect(self.close)
