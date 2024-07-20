#!/usr/bin/env python
# -*- coding: utf-8 -*-


# pip install PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel

from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QModelIndex

import os, sys

from pathlib import Path

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.stk_w = QStackedWidget(self)
        self.init_widget()

    def init_widget(self):
        widget_laytout = QBoxLayout(QBoxLayout.LeftToRight)
        BTN_Print = QPushButton("print")
        BTN_Print.clicked.connect(self.Print_img)
        widget_laytout.addWidget(BTN_Print)
        self.setLayout(widget_laytout)

    def Print_img(self):
        print("print_img")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet(Path('style.qss').read_text())
    form = Form()
    form.show()
    sys.exit(app.exec_())