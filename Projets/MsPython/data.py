import Affichage

def donnee () :
    Affichage.printSlowly("give me your name: ", 1 / 20)
    your_name=input()
    Affichage.printSlowly("give me seurname:", 1 / 20)
    surname=input()
    Affichage.printSlowly("give me your age: ", 1 / 20)
    age = input()
    Affichage.printSlowly("give me your city: ", 1 / 20)
    city= input()
    Affichage.printSlowly("give me your job: ", 1 / 20)
    job=input()
    return your_name,surname,age,city,job

def donneeMock():
    return  ["mouad", "afellah", "15", "agadir", "student"]


