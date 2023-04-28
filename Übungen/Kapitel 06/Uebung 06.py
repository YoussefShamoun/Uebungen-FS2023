from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *


class UiFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel 06/showmap.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        l = self.lat.text()
        b = self.lon.text()
        url_string = f"https://www.google.ch/maps/place/{l},{b}"
        url = QUrl(url_string)
        QDesktopServices.openUrl(url)

app = QApplication([])
win = UiFenster()
app.exec()