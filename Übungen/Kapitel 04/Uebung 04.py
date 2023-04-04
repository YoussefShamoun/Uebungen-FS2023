from PyQt5.QtWidgets import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("GUI-Programmierung")                                     # Fenster-Titel setzen
#------------------------------------------------------------------------------
        layout = QFormLayout()                                          # Layout erstellen
#------------------------------------------------------------------------------
   
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")                              # File-Menu erstellen
        viewmenu = menubar.addMenu("View")                              # View-Menu erstellen

#------------------------------------------------------------------------------
      
        save = QAction("Save", self)                                    # Action definieren
        save_as = QAction("Save as", self)
        quit = QAction("Quit", self)
        zoom_in = QAction ("Zoom in", self)
        zoom_out = QAction ("Zoom out", self)

        filemenu.addAction(save)                                        # Action zum File-Menu hinzufügen
        filemenu.addAction(save_as)
        filemenu.addAction(quit)
        viewmenu.addAction(zoom_in)                                     # Action zum View-Menu hinzufügen
        viewmenu.addAction(zoom_out)

#------------------------------------------------------------------------------           

        self.vorname = QLineEdit()                                      # Widget-Instanzen erstellen
        self.name = QLineEdit()
        self.geburtsdatum = QDateEdit()
        self.adresse = QLineEdit()
        self.postleitzahl = QLineEdit()
        self.ort = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button = QPushButton("Save")                               # Save button erstellen

        layout.addRow("Vorname:", self.vorname)                         # Instanzen zum Layout hinzufuegen
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtsdatum:", self.geburtsdatum)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("PostLeitzahl:", self.postleitzahl)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.countries)
        layout.addRow(self.button)

        save.triggered.connect(self.save_data)                          # Connect save action to save_data method
        quit.triggered.connect(self.close)                              # Connect quit action to close method of the window
        self.button.clicked.connect(self.save_data)                     # Connect button click to save_data method

#------------------------------------------------------------------------------

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

#------------------------------------------------------------------------------

    def save_data(self):                                                # save_data Methode definieren (Text + Datei erstellen + Daten Einfuegen)
        data = f"{self.vorname.text()},{self.name.text()},{self.geburtsdatum.text()},{self.adresse.text()},{self.postleitzahl.text()},{self.ort.text()},{self.countries.currentText()}"
        file = open("output.txt", "w",encoding="utf-8") 
        file.write(data)

#------------------------------------------------------------------------------

app = QApplication([])
win = Fenster()
app.exec()