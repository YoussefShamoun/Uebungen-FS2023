import math

class Figur:
    def __init__(self):
        self.name = "Figur"
    
    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name

class Dreieck(Figur):
    def __init__(self, name, p1, p2, p3):
        super().__init__()
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def Umfang(self):
        a = math.dist(self.p1, self.p2)
        b = math.dist(self.p2, self.p3)
        c = math.dist(self.p3, self.p1)
        return a + b + c
    
    def __str__(self):
        return f"{self.name} ({self.p1}, {self.p2}, {self.p3})"
        
class Rechteck(Figur):
    def __init__(self, name, p1, p2, p3, p4):
        super().__init__()
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    
    def Umfang(self):
        a = math.dist(self.p1, self.p2)
        b = math.dist(self.p2, self.p3)
        c = math.dist(self.p3, self.p4)
        d = math.dist(self.p4, self.p1)
        return a + b + c + d
    
    def __str__(self):
        return f"{self.name} ({self.p1}, {self.p2}, {self.p3}, {self.p4})"
        
class Kreis(Figur):
    def __init__(self, name, center, radius):
        super().__init__()
        self.name = name
        self.center = center
        self.radius = radius
    
    def Umfang(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"{self.name} M={self.center} r={self.radius}"
        
import math

class Polygon(Figur):
    def __init__(self, name, points):
        super().__init__()
        self.name = name
        self.points = points
    
    def Umfang(self):
        perimeter = 0
        num_points = len(self.points)

        for i in range(num_points):
            a = math.dist(self.points[i], self.points[(i+1) % num_points])
            perimeter += a

        return perimeter
    
    def __str__(self):
        return f"{self.name} {self.points}"
        
# Example usage
d = Dreieck("Triangle",(0,0), (0,4), (3,0))
print(d)
print("Perimeter:", d.Umfang())

r = Rechteck("Square", (2,2), (2,6), (6,6), (6,2))
print(r)
print("Perimeter:", r.Umfang())

k = Kreis("Circle", (4,4), 2)
print(k)
print("Perimeter:", k.Umfang())

p = Polygon("Polygon", [(2,2), (2,6), (3,7), (6,6), (6,2), (4,1)])
print(p)
print("Perimeter:", p.Umfang())
