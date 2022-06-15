import GLOABL_STATE
from  Books import listBoos
from  Books import  listPerson
from  Books import  takebook

def donneeOFbook():
    booksTmp = []
    number = int(input("Please give me nuber kind the books : "))
    max = 0
    while max < number:
        max = max + 1
        print(" give me information of  book", max, ":")
        name = input("name : ")
        stock = int(input("stock : "))
        goldInput = int(input("it is gold[1/0]: "))
        if goldInput == 1:
            gold = True
        elif goldInput == 0:
            gold = False
        book = {"name": name, "stock": stock, "gold": gold, "initialStock": stock, "person": None}
        booksTmp.append(book)
    return booksTmp


def donneeOfPerson():
    personsTmp = []
    personNumber = int(input("Please give me number of person: "))
    max = 0
    while max < personNumber:
        max = max + 1
        print("Give me the information of the person N°", max, ": ")
        name = input("Name: ")
        number = int(input("Number phone : "))
        person = {"name": name, "numberPhone": number}
        personsTmp.append(person)
    return personsTmp


def updateBooks(book):
    print(book["name"])
    name = input("name : ")
    stock = int(input("stock : "))
    goldInput = int(input("it is gold[1/0]: "))
    if goldInput == 1:
        gold = True
    elif goldInput == 0:
        gold = False
        book = {"name": name, "stock": stock, "gold": gold, "initialStock": stock, "person": None}

    return book

def updatePerson(person):
    print(person["name"])
    name = input("Name: ")
    number = int(input("Number phone : "))
    person = {"name": name, "numberPhone": number}
    return person

def DetakeBook():
    listBoos(GLOABL_STATE.books)
    listPerson(GLOABL_STATE.persons)
    idPerson = int(input("enter number of person :"))
    idBook = int(input("enter number of Book :"))
    takebook(GLOABL_STATE.books[idBook-1],GLOABL_STATE.persons[idPerson-1])