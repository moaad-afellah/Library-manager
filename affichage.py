from information import donneeOFbook
from Books import printReport
from Books import printEtatOfOnebook
from information import donneeOfPerson
from information import DetakeBook
from Books import listBoos
from information import updateBook
from Books import searchBook
from information import updatePerson
from Books import searchPerson
from Books import searchPerson2
from Books import returnbook
from Books import listPerson
from information import finStockperson
import os
import GLOABL_STATE
import pyautogui
from CommonLibrary.Input.ControllerInput import input_Int


def clearConsoleCmd():
    os.system("cls")


def clearConsolePycharm():
    pyautogui.hotkey("Ctrl", "X")


def clearConsole():
    if GLOABL_STATE.typeClear == 0:
        clearConsoleCmd()
    else:
        clearConsolePycharm()


def Welcome():
    print('         Hello sir,              ')
    print("""
    Enter 1 : in order to enter books.
    Enter 2 : in order to enter persons.
    Entre 3 : list the Books.
    Enter 4 : list the Person.
    Enter 5 : update the Books. 
    Enter 6 : update the Persons.
    Enter 7 : take Books.
    Enter 8 : return book.
    Enter 9 : in order to  show Report of status of boos.
    Enter 10 : in order to show the owners of books.
    Enter 11 : Search par name of book.
    Enter 12 : Search par person. 
    Enter 13 : in order to exit.
        
    """)
    inputNumber = input_Int("You choice: ")
    clearConsole()
    if inputNumber == 1:
        bk = donneeOFbook()
        GLOABL_STATE.books = GLOABL_STATE.books + bk


    elif inputNumber == 2:
        pr = donneeOfPerson()
        GLOABL_STATE.persons = GLOABL_STATE.persons + pr


    elif inputNumber == 3:
        listBoos(GLOABL_STATE.books)
        input()


    elif inputNumber == 4:
        listPerson(GLOABL_STATE.persons)
        input()


    elif inputNumber == 5:
        listBoos(GLOABL_STATE.books)
        number = input_Int("Please give me number of book :")
        GLOABL_STATE.books[number - 1] = updateBook(GLOABL_STATE.books[number - 1])
        input()


    elif inputNumber == 6:
        listPerson(GLOABL_STATE.persons)
        number = input_Int("please give me number of Person :")
        GLOABL_STATE.persons[number - 1] = updatePerson(GLOABL_STATE.persons[number - 1])
        input()


    elif inputNumber == 7:
        DetakeBook()
        input()

    elif inputNumber == 8:
        finPerson = listPerson(GLOABL_STATE.persons)
        idPerson = finStockperson(finPerson)
        returnbook(GLOABL_STATE.books, GLOABL_STATE.persons[idPerson - 1])

    elif inputNumber == 9:
        printReport(GLOABL_STATE.books)
        input()


    elif inputNumber == 10:
        printEtatOfOnebook(GLOABL_STATE.books)
        input()


    elif inputNumber == 11:
        nameOFbookSearch = input("Give me name of book: ")
        searchBook(nameOFbookSearch, GLOABL_STATE.books)
        input()


    elif inputNumber == 12:
        nameOFpersonsearch = input("Give me name of person: ")
        searchPerson(nameOFpersonsearch, GLOABL_STATE.persons)
        searchPerson2(nameOFpersonsearch, GLOABL_STATE.books)
        input()


    elif inputNumber == 13:
        print("Good bye")
        exit()


    else:
        print('No cption for this number:', inputNumber)
    clearConsole()
    Welcome()
