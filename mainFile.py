from Books import takebook
from Books import returnbook
from Books import printReport
from Books import printEtatDuLieu

book1 = {"name": "pablo", "stock": 8, "gold": True, "initialStock": 8, "person": None}
book2 = {"name": "basketBall", "stock": 4, "gold": False, "initialStock": 4, "person": None}
book3 = {"name": "football", "stock": 8, "gold": True, "initialStock": 8, "person": None}
book4 = {"name": "ninja", "stock": 6, "gold": False, "initialStock": 6, "person": None}
book5 = {"name": "freeFire", "stock": 7, "gold": False, "initialStock": 7, "person": None}

person1 = {"name": "ahmed", "number": 66}
person2 = {"name": "saad", "number": 67}
person3 = {"name": "hasan", "number": 68}
person4 = {"name": "mohammed", "number": 69}

printReport(book1, book2, book3, book4, book5)
printEtatDuLieu(book1, book2, book3, book4, book5)

print(person1["name"], "want to take the  book1")
takebook(book1, person1)

print(person2["name"], " want to take the book2")
takebook(book2, person2)

print(person3["name"], " want to take the  book3")
takebook(book3, person3)

printReport(book1, book2, book3, book4, book5)
printEtatDuLieu(book1, book2, book3, book4, book5)

print(person4["name"], " want to take the book4")
takebook(book4, person4)

printReport(book1, book2, book3, book4, book5)
printEtatDuLieu(book1, book2, book3, book4, book5)

print(person4["name"], " return the book4")
returnbook(book4, person4)

printReport(book1, book2, book3, book4, book5)
printEtatDuLieu(book1, book2, book3, book4, book5)

returnbook(book2, person4)

printReport(book1, book2, book3, book4, book5)
printEtatDuLieu(book1, book2, book3, book4, book5)
