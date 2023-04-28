
# Aufgabe 1 

import numpy as np
import matplotlib.pyplot as plt

# Generiere 1000 zufällige Punkte
n_points = 1000
x = np.random.uniform(-100, 100, n_points)
y = np.random.uniform(-100, 100, n_points)

# Erzeuge eine zufällige Farbe für jeden Punkt
colors = np.random.rand(n_points)

# Plotte die Punkte
plt.scatter(x, y, c=colors)
plt.show()

# -------------------------------------------------------------------------------------------------

# Aufgabe 2

import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.exp(-x**2) * np.sin(y)

# Array mit x- und y-Koordinaten erzeugen
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# 2D-Gitter erstellen
X, Y = np.meshgrid(x, y)

# f(X,Y) auswerten
Z = f(X, Y)

# Zweidimensionales Gitter grafisch darstellen
plt.pcolormesh(X, Y, Z)
plt.show()



