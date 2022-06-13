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
