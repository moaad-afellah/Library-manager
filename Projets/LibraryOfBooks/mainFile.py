from affichage import Welcome
import GLOABL_STATE


def initMyapp():
    personsTemp = [{"name": "moaad", "numberPhone": 6546547, "book": None},
                   {"name": "brahim", "numberPhone": 66646855, "book": None},
                   {"name": "saad-addine", "numberPhone": 6846965, "book": None}
                   ]

    GLOABL_STATE.persons = GLOABL_STATE.persons + personsTemp
    booksTemp = [{"name": "pablo", "stock": 54, "gold": True, "initialStock": 54,
                  "person": [GLOABL_STATE.persons[0], GLOABL_STATE.persons[1]]},
                 {"name": "3ali baba", "stock": 15, "gold": False, "initialStock": 15,
                  "person": [GLOABL_STATE.persons[2]]},
                 {"name": "football", "stock": 28, "gold": False, "initialStock": 28, "person": []},
                 {"name": "salad", "stock": 27, "gold": False, "initialStock": 27, "person": []}]
    GLOABL_STATE.books = GLOABL_STATE.books + booksTemp
    personsTemp[0]["book"] = GLOABL_STATE.books[0]
    personsTemp[1]["book"] = GLOABL_STATE.books[0]
    GLOABL_STATE.books[0]["stock"] = GLOABL_STATE.books[0]["stock"] - 2
    GLOABL_STATE.books[1]["stock"] = GLOABL_STATE.books[1]["stock"] - 1


initMyapp()
Welcome()
