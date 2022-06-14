def takebook(book, person):
    afficherStock(book)
    if book["gold"] == False:
        if book["stock"] == 0:
            return 0
        book["person"] = person
        book["stock"] = book["stock"] - 1
        return
    if book["gold"] == True:
        if book["stock"] == 0:
            return
        print(book["name"], "is gold")
        password = int(input("please enter password: "))
        if password == 2006:
            book["person"] = person
            book["stock"] = book["stock"] - 1
        else:
            print("Sorry , password is incorrect !!!")
            return


def returnbook(book, person):
    afficherStock(book)
    if book["stock"] >= book["initialStock"]:
        print("No, this is not the book of this libray")
    if book["stock"] < book["initialStock"]:
        print("thank you ", person['name'], "!! for returning the book ")
        book["person"] = None
        book["stock"] = book["stock"] + 1


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
        if book["person"] != None:
            print(book["name"], "    ", book["person"]["name"], book["person"]["numberPhone"])
        elif book["person"] == None:
            print(book["name"], "    ", book["person"])


def printEtatDuLieu(books):
    print("******Etat du lieu ***************")
    print("Name of the book      name of person         Phone number")
    for book in books:
        printEtatOfOnebook(book)
    print("******Fin etat du lieu ***************")
