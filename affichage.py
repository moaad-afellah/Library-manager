def afficherStock(book):
    if book["stock"] > 0:
        print("Yes , there is one in the stock")
    if book["stock"] <= 0:
        print("Sorry!! this  book is not in the stock")
