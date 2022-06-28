class Domino:
    def __init__(self, facesA=0, facesB=0):
        self.facesA = facesA
        self.facesB = facesB

    def affiche_points(self):
        print("faces A : ", self.facesA, " faces B : ", self.facesB)

    def valeur(self):
        somme = self.facesA + self.facesB
        return somme


d1 = Domino(2, 6)
d2 = Domino(4, 3)
d1.affiche_points()
d2.affiche_points()
print("total des points :", d1.valeur() + d2.valeur())

liste_dominos = []

for i in range(7):
    liste_dominos.append(Domino(6, i))
nt(liste_dominos[3])
