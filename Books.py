from affichage import afficherStock


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


def printReport(book1, book2, book3, book4, book5):
    print("pablo :          in:", book1["stock"], "/   out", book1["initialStock"] - book1["stock"])
    print("basketball : ", "in:", book2["stock"], "/   out:", book2["initialStock"] - book2["stock"])
    print("football :         in:", book3["stock"], "/    out", book3["initialStock"] - book3["stock"])
    print("ninija :            in", book4["stock"], "/     out", book4["initialStock"] - book4["stock"])
    print("freeFire :             in", book5["stock"], "/      out:", book5["initialStock"] - book5["stock"])



def printEtatOfbook(book):
    if book["person"] != None:
        print(book["name"], "    ", book["person"]["name"] , book["person"]["number"])


def printEtatDuLieu(book1, book2, book3, book4, book5):
    print("******Etat du lieu ***************")
    print("Name of the book      name of person         Phone number")
    printEtatOfbook(book1)
    printEtatOfbook(book2)
    printEtatOfbook(book3)
    printEtatOfbook(book4)
    printEtatOfbook(book5)
    print("******Fin etat du lieu ***************")

