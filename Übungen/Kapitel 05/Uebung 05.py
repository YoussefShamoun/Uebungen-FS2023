from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("MainWindow")                               # Fenster-Titel setzen
#------------------------------------------------------------------------------
        layout = QFormLayout()                                          # Layout erstellen
#------------------------------------------------------------------------------
   
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")                              # File-Menu erstellen
        viewmenu = menubar.addMenu("View")                              # View-Menu erstellen

#------------------------------------------------------------------------------
      
        save = QAction("Save", self)                                    # Action definieren
        save_as = QAction("Save as", self)
        load = QAction("Load", self)
        quit = QAction("Quit", self)
        zoom_in = QAction ("Zoom in", self)
        zoom_out = QAction ("Zoom out", self)
        anzeigen = QAction ("Show on map", self)

        filemenu.addAction(save)                                        # Action zum File-Menu hinzufügen
        filemenu.addAction(save_as)
        filemenu.addAction(quit)
        filemenu.addAction(load)
        viewmenu.addAction(zoom_in)                                     # Action zum View-Menu hinzufügen
        viewmenu.addAction(zoom_out)
        viewmenu.addAction(anzeigen)

#------------------------------------------------------------------------------           

        self.vorname = QLineEdit()                                      # Widget-Instanzen erstellen
        self.name = QLineEdit()
        self.geburtsdatum = QDateEdit()
        self.strasse = QLineEdit()
        self.nummer = QLineEdit()
        self.postleitzahl = QLineEdit()
        self.ort = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button1 = QPushButton("Auf Karte zeigen")
        self.button2 = QPushButton("Laden")
        self.button3 = QPushButton("Save")                               # Save button erstellen
        

        layout.addRow("Vorname:", self.vorname)                         # Instanzen zum Layout hinzufuegen
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtsdatum:", self.geburtsdatum)
        layout.addRow("Strasse:", self.strasse)
        layout.addRow("Hausnummer:", self.nummer)
        layout.addRow("PostLeitzahl:", self.postleitzahl)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.countries)
        layout.addRow(self.button1)
        layout.addRow(self.button2)
        layout.addRow(self.button3)

        save.triggered.connect(self.save)                          # Connect save action to save_data method
        save_as.triggered.connect(self.save)
        quit.triggered.connect(self.close)
        anzeigen.triggered.connect(self.url)
        load.triggered.connect(self.load)                              # Connect quit action to close method of the window
        self.button3.clicked.connect(self.save)                     # Connect button click to save_data method
        self.button1.clicked.connect(self.url)
        self.button2.clicked.connect(self.load)

#------------------------------------------------------------------------------

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

#------------------------------------------------------------------------------

    def save(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Datei Speichern","", "Text Datei (*txt)")
        if filename:
                with open(filename, 'w', encoding='utf-8') as file:
                        v = self.vorname.text()
                        n = self.name.text()
                        g = self.geburtsdatum.text()                                    
                        a = self.strasse.text()
                        m = self.nummer.text()
                        p = self.postleitzahl.text()
                        o = self.ort.text()
                        l = self.countries.currentText()
                        data = f"{v},{n},{g},{a},{m},{p},{o},{l}"
                        file.write(data) 

    def url(self):
        v = self.vorname.text()
        n = self.name.text()
        g = self.geburtsdatum.text()                                    
        a = self.strasse.text()
        m = self.nummer.text()
        p = self.postleitzahl.text()
        o = self.ort.text()
        l = self.countries.currentText()
    
        url_string = f"https://www.google.ch/maps/place/{a}+{m}+{p}+{o}+{l}"
        url = QUrl(url_string)
        QDesktopServices.openUrl(url)

    def load(self):
        filename, filter = QFileDialog.getOpenFileName(self, "Datei Öffnen", "", "Text Datei (*txt)")
        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                data = file.read().split(',')
                self.vorname.setText(data[0])
                self.name.setText(data[1])
                self.geburtsdatum.setDate(QDate.fromString(data[2], "dd.MM.yyyy"))
                self.strasse.setText(data[3])
                self.nummer.setText(data[4])
                self.postleitzahl.setText(data[5])
                self.ort.setText(data[6])
                index = self.countries.findText(data[7])
                self.countries.setCurrentIndex(index)
                                             
        
#------------------------------------------------------------------------------

app = QApplication([])
win = Fenster()
app.exec()