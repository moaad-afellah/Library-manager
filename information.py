import GLOABL_STATE
from Books import listBoos
from Books import listPerson
from Books import takebook
from CommonLibrary.Input.ControllerInput import input_Int
from Books import printEtatOfOnebook

def donneeOFbook():
    booksTmp = []
    number = input_Int("Please give me nuber kind the books : ")
    max = 0
    while max < number:
        max = max + 1
        print(" give me information of  book", max, ":")
        name = input("name : ")
        stock = input_Int("stock : ")
        goldInput = input_Int("it is gold[1/0]: ")
        if goldInput == 1:
            gold = True
        elif goldInput == 0:
            gold = False

        book = {"name": name, "stock": stock, "gold": gold, "initialStock": stock, "person": []}
        booksTmp.append(book)
    return booksTmp


def donneeOfPerson():
    personsTmp = []
    personNumber = input_Int("Please give me number of person: ")
    max = 0
    while max < personNumber:
        max = max + 1
        print("Give me the information of the person N°", max, ": ")
        name = input("Name: ")
        number = input_Int("Number phone : ")
        person = {"name": name, "numberPhone": number}
        personsTmp.append(person)
    return personsTmp


def updateBook(book):
    print(book["name"])
    name = input("name : ")
    stock = input_Int("stock : ")
    goldInput = input_Int("it is gold[1/0]: ")
    if goldInput == 1:
        gold = True
    elif goldInput == 0:
        gold = False
    persons = []
    book = {"name": name, "stock": stock, "gold": gold, "initialStock": stock, persons: None}

    return book


def updatePerson(person):
    print(person["name"])
    name = input("Name: ")
    number = input_Int("Number phone : ")
    person = {"name": name, "numberPhone": number}
    return person


def DetakeBook():
    finBook = listBoos(GLOABL_STATE.books)
    finPerson = listPerson(GLOABL_STATE.persons)
    idPerson = finStockperson(finPerson)
    idBook = finStockbook(finBook)
    takebook(GLOABL_STATE.books[idBook - 1], GLOABL_STATE.persons[idPerson - 1])
    return


def finStockperson(finPerson):
    sp = False
    while sp != True :
        idPerson = input_Int("enter number of person :")
        if finPerson >= idPerson :
            print("ok")
            sp = True
        elif finPerson < idPerson :
            print("sorry , !!")
            sp = False
    return idPerson

def finStockbook(finBook):
    sk = False
    while sk != True :
        idBook = input_Int("enter number of Book :")
        if finBook >= idBook :
            print("ok")
            sk = True
        elif finBook < idBook :
            print("sorry , !!")
            sk = False
    return idBook