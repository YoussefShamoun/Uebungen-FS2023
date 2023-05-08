from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QFormLayout()

        self.setWindowTitle("Polynom Plotter")

        figure = plt.figure(figsize = (16,9))
        self.canvas = FigureCanvas(figure)

        self.min = QLineEdit("-1")  
        self.max = QLineEdit ("3")
        self.f = QLineEdit("1,-2,-1,0")

        self.colors = QComboBox()
        self.colors.addItems(["red", "blue", "black"])
        self.color_dic = {"red": "ro-", "blue": "bo-", "black": "ko-"}

        self.points = QSlider(Qt.Orientation.Horizontal, self)
        self.points.setRange(0, 20)
        self.points.setValue(10)
        self.points.setSingleStep(2)
        self.points.setPageStep(2)
        self.points.setTickPosition(QSlider.TicksAbove)
                  
        button = QPushButton("Plot")

        layout.addRow("Graph:", self.canvas)
        layout.addRow("Min Range:", self.min)
        layout.addRow("Max Range:", self.max)
        layout.addRow("Coefficients:", self.f)
        layout.addRow("Color:", self.colors)
        layout.addRow(button)
        layout.addRow("Nr. of Points:", self.points)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        button.clicked.connect(self.plot)
        self.points.valueChanged.connect(self.updateslider)

    def updateslider(self, value):
        points = int(self.points.value())

    def updateslider(self, value):
        plt.clf()  #clear_figure

        grade = self.f.text()
        xmin = float(self.min.text())
        xmax = float(self.max.text())
        points = int(self.points.value())
        color = self.colors.currentText()
        c = self.color_dic[color]

        try:
            coeff = [float(x) for x in grade.split(',')]
            f = np.poly1d(coeff)
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid coefficient input!")
            return
        x = np.linspace(xmin, xmax, points)
        y = f(x)

        plt.plot(x,y,c)
        plt.axis("equal")

        n = len(f)
        title = f"Polynomial Function: {n}-ten Grades"
        plt.title(title)
        self.canvas.draw()

    def plot(self):
        plt.clf()  #clear_figure

        grade = self.f.text()
        xmin = float(self.min.text())
        xmax = float(self.max.text())
        points = int(self.points.value())
        color = self.colors.currentText()
        c = self.color_dic[color]

        try:
            coeff = [float(x) for x in grade.split(',')]
            f = np.poly1d(coeff)
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid coefficient input!")
            return
        x = np.linspace(xmin, xmax, points)
        y = f(x)

        plt.plot(x,y,c)
        plt.axis("equal")

        n = len(f)
        title = f"Polynomial Function {n}-ten Grades"
        plt.title(title)
        self.canvas.draw()

app = QApplication([])
window = Window()
app.exec_()
