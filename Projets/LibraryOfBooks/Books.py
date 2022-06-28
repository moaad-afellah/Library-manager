from CommonLibrary.Input.ControllerInput import input_Int


def takebook(book, person):
    afficherStock(book)
    if book["gold"] == False:
        if book["stock"] == 0:
            return 0
        person["book"] = book["name"]
        book["person"].append(person)
        book["stock"] = book["stock"] - 1
        return
    if book["gold"] == True:
        if book["stock"] == 0:
            return
        print(book["name"], "is gold")
        password = input_Int("please enter password: ")
        if password == 2006:
            print("Good , password is correct !!!")
            person["book"].append(book["name"])
            book["person"].append(person)
            book["stock"] = book["stock"] - 1
            input()
        else:
            print("Sorry , password is incorrect !!!")
            input()
            return book, person


def returnbook(books, Person):
    Person["book"] = None
    for book in books:
        if book["stock"] == book["initialStock"]:
            print("No, this is not the book of this libray")
            continue
        for person in book["person"]:
            if person == Person:
                if book["stock"] < book["initialStock"]:
                    print("thank you ", Person['name'], "!! for returning the book ")
                    Person["book"] = None
                    book["person"].remove(Person)
                    book["stock"] = book["stock"] + 1

        input()


def afficherStock(book):
    if book["stock"] > 0:
        print("Yes , there is one in the stock")
    if book["stock"] <= 0:
        print("Sorry!! this  book is not in the stock")
    return


def printReport(books):
    for book in books:
        print(book["name"], ":          in:", book["stock"], "/   out",
              book["initialStock"] - book["stock"])


def printEtatOfOnebook(books):
    for book in books:
        if len(book["person"]) > 0:
            for person in book["person"]:
                print("",
                      book["name"],
                      "           ", person["name"], person["numberPhone"],
                      "")
        else:
            print(" ", book["name"], "               ", "No one")


def printEtatDuLieu(books):
    print("******Etat du lieu ***************")
    print("Name of the book      name of person         Phone number")
    for book in books:
        printEtatOfOnebook(book)
    print("******Fin etat du lieu ***************")


def listBoos(books):
    print("THE BOOKS: ")
    n = 1
    for book in books:
        print(n, "-", book["name"])
        n = n + 1
    return n - 1


def listPerson(persons):
    print("THE PERSONS: ")
    m = 1
    for person in persons:
        print(m, "-", person["name"])
        m = m + 1
    return m - 1


def searchBook(nameOFbookSearch, Books):
    for book in Books:
        if nameOFbookSearch == book["name"]:
            print(book)
            break
    else:
        print("sorry , not found.")


def searchPerson(nameOFperson, Persons):
    found = False
    for person in Persons:
        if nameOFperson in person["name"] and person["book"] is not None:
            print(person["name"], ": ", person["book"]["name"])
            found = True

    if not found:
        print("sorry , not found ")


def searchPerson2(nameOFperson, Books):
    for book in Books:
        for person in book["person"]:
            if person["name"] == nameOFperson:
                print(person["name"], ": ", book["name"])
                break
            else:
                print("sorry , not find ")
