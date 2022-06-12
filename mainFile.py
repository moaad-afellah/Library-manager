from Books import takebook
from Books import returnbook
from Books import printReport
from Books import printEtatDuLieu

books = []
book1 = {"name": "pablo", "stock": 8, "gold": True, "initialStock": 8, "person": None}
book2 = {"name": "basketBall", "stock": 4, "gold": False, "initialStock": 4, "person": None}
book3 = {"name": "football", "stock": 8, "gold": True, "initialStock": 8, "person": None}
book4 = {"name": "ninja", "stock": 6, "gold": False, "initialStock": 6, "person": None}
book5 = {"name": "freeFire", "stock": 7, "gold": False, "initialStock": 7, "person": None}
# books=[book1,book2,book3,book4,book5]
books.append(book1)
books.append(book2)
books.append(book3)
books.append(book4)
books.append(book5)

persons = []
person1 = {"name": "ahmed", "number": 66}
person2 = {"name": "saad", "number": 67}
person3 = {"name": "hasan", "number": 68}
person4 = {"name": "mohammed", "number": 69}
persons.append(person1)
persons.append(person2)
persons.append(person3)
persons.append(person4)

printReport(books)
printEtatDuLieu(books)

print(person1["name"], "want to take the  book1")
takebook(books[1], person1)

print(person2["name"], " want to take the book2")
takebook(books[2], person2)

print(person3["name"], " want to take the  book3")
takebook(books[3], person3)

printReport(books)
printEtatDuLieu(books)

print(person4["name"], " want to take the book4")
takebook(books[4], person4)

printReport(books)
printEtatDuLieu(books)

print(person4["name"], " return the book4")
returnbook(books[4], person4)

printReport(books)
printEtatDuLieu(books)

returnbook(books[2], person4)

printReport(books)
printEtatDuLieu(books)
