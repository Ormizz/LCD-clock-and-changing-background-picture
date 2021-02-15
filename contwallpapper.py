"""
------------------------------------------------------------------------
author  : Soro Katchi
version : 1.0
date    : 02.15.2021
------------------------------------------------------------------------
"""

import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import sys
import time
import random
import threading

class wallpapper(QDialog):
    def __init__(self):
        super(wallpapper, self).__init__()
        loadUi("wallpapper.ui", self)
        photoNumb = random.randint(1,7)
        pixmap = QtGui.QPixmap(f"img_storage/{photoNumb}.png")
        self.label.setStyleSheet(f"border-image: url(img_storage/{photoNumb}.png);")
        #call threading to execute multiple tasks
        threading.Thread(target=lambda: self.updatedate()).start() #start time thread
        threading.Thread(target=lambda : self.changeBackground()).start() #start background changing thread

    def updatedate(self):
        launch = True
        while launch:
            currentTime = QtCore.QTime.currentTime()
            strCurrentTime = currentTime.toString("hh:mm")
            self.lcdNumber.display(strCurrentTime)
            time.sleep(1)#change time after 1s

    def changeBackground(self):
        while True:
            photoNumb = random.randint(1,7)
            pixmap = QtGui.QPixmap(f"img_storage/{photoNumb}.png")
            self.label.setStyleSheet(f"border-image: url(img_storage/{photoNumb}.png);")
            time.sleep(15) #change background after 15s

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = wallpapper()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(300)
    widget.setFixedWidth(400)
    widget.show()
app.exec_()
