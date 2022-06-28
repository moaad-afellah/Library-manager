import math
import random

class Points:
    def __init__(self, coordX, coordY):
        self.coordX = int(coordX)
        self.coordY = int(coordY)
        self.coordinate = (coordX,coordY)

    def distance(self, pointB):
        distance = math.sqrt((self.coordX-pointB.coordX)**2 + (self.coordY-pointB.coordY)**2)
        return distance


distance = 1
isFUll = False
while isFUll == False:
    a = Points(random.randint(-5, 64), random.randint(-2, 1))
    b = Points(random.randint(-3, 11), random.randint(-4, 51))
    distance = a.distance(b)
    print(distance)
    if distance > 0 and distance <= 1.41:
        isFUll = True
        print(a.coordinate, b.coordinate)