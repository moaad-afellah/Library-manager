import math
import random

class Points:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY
        self.coordinate = (coordX, coordY)

    def distance(self, pointB):
        distance = math.sqrt((self.coordX-pointB.coordX)**2 + (self.coordY-pointB.coordY)**2)
        return distance


distance = 1
found = False
distances = []
while found == False and len(distances) <10000:
    a = Points(random.uniform(0, 10.0), random.uniform(0, 5.0))
    b = Points(random.uniform(0, 10.0), random.uniform(0, 5.0))

    distance = a.distance(b)
    distances.append(distance)
    #print(distance)
    if  distance <= 0.9 and distance != 0:
        found = True
        print(a.coordinate, b.coordinate)

distances.sort()
print(distances)
