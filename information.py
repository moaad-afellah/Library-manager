from Books import takebook
import GLOABL_STATE


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


def donneeOfPersonAndTakenBook():
    personsTmp = []
    personNumber = int(input("Please give me number of person: "))
    max = 0
    while max < personNumber:
        max = max + 1
        print("Give me the information of the person N°", max, ": ")
        name = input("Name: ")
        number = int(input("Number phone : "))
        takenBookIndex = int(input("Please enter number of book: "))
        person = {"name": name, "numberPhone": number, "takenBookIndex": takenBookIndex, "personId": max + len(GLOABL_STATE.persons)}
        personsTmp.append(person)
    return personsTmp
