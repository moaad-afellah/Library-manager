from time import sleep
import os

def printSlowly(phrase , vitesse = 0.05):
    for c in phrase:
        print(c, end='')
        sleep(vitesse)


def afficher(phrase):
    os.system("cls")
    print("<******************>")
    printSlowly(phrase)
    print("")
    print("<=***********=>")








