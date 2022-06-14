from information import donneeOFbook
from Books import printReport
from Books import printEtatOfOnebook
from information import donneeOfPersonAndTakenBook
from Books import takebook
import os
import GLOABL_STATE
import pyautogui


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
    inputNumber = int(input("""
    Enter 1 : in order to enter books.
    Enter 2 : in order to enter persons.
    Enter 3 : in order to  show Report of status of boos.
    Enter 4 : in order to show the owners of books.
    Enter 5 : in order to exit.
    
        You choice: 
    """))
    clearConsole()
    if inputNumber == 1:
        bk = donneeOFbook()
        GLOABL_STATE.books = GLOABL_STATE.books + bk
    elif inputNumber == 2:
        pr = donneeOfPersonAndTakenBook()
        GLOABL_STATE.persons = GLOABL_STATE.persons + pr
        for person in pr:
            takebook(GLOABL_STATE.books[person["takenBookIndex"] - 1], person)
    elif inputNumber == 3:
        printReport(GLOABL_STATE.books)
        input()
    elif inputNumber == 4:
        printEtatOfOnebook(GLOABL_STATE.books)
        input()
    elif inputNumber == 5:
        print("Good bye")
        exit()lùk
    clearConsole
    Welcome()
