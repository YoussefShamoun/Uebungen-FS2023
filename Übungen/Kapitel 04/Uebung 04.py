from PyQt5.QtWidgets import *
import os


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI-Programmierung")  # Fenster-Titel setzen

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        save.triggered.connect(self.save_data)  # Connect save action to save_data method
        quit = QAction("Quit", self)
        quit.triggered.connect(self.close)  # Connect quit action to close method of the window
        self.button = QPushButton("Save")
        self.button.clicked.connect(self.save_data)  # Connect button click to save_data method

        quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" zuweisen, nur für MacOS relevant

        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(quit)

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:

        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtsdatum = QDateEdit()
        self.adresseLineEdit = QLineEdit()
        self.postleitzahlLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtsdatum:", self.geburtsdatum)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("PostLeitzahl:", self.postleitzahlLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.countries)
        layout.addRow(self.button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

    def save_data(self):
        data = f"{self.vornameLineEdit.text()},{self.nameLineEdit.text()},{self.geburtsdatum.text()},{self.adresseLineEdit.text()},{self.postleitzahlLineEdit.text()},{self.ortLineEdit.text()},{self.countries.currentText()}"
        file = open("output.txt", "w",encoding="utf-8") 
        file.write(str(data))
       


app = QApplication([])
win = Fenster()
app.exec()