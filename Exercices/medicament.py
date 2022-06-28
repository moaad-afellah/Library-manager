import random
import string


class Medicament:
    def __init__(self, type, price, name):
        self.type = type
        self.price = price
        self.name = name


def averagePriceAndPrint(list, type):
    listPrice = []
    for p in list:
        if p.type == type:
            listPrice.append(p.price)
    somme = 0
    for i in listPrice:
        somme = somme + i

    if len(listPrice) != 0:
        print("Average wish of ", type, "is: ", somme / len(listPrice))


types = ["Categorie A", "Categorie B", "Categorie C", "Categorie D", "Categorie E", "Categorie F"]


def makeMedicaments(size):
    letters = string.ascii_lowercase
    medicaments = []
    for i in range(0, size):
        p = Medicament(types[random.randint(0, 5)], random.randint(200, 800),
                       "".join(random.choice(letters) for i in range(5)))
        medicaments.append(p)
    return medicaments


def printAllAvergeType(medicaments):
    for type in types:
        averagePriceAndPrint(medicaments, type)

def printListOfMedcaments(medicaments):
    pass

medicaments = makeMedicaments(20)
printAllAvergeType(medicaments)