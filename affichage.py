from information import donneeOFbook
from Books import printReport
from Books import printEtatOfOnebook
import os
import GLOABL_STATE
import pyautogui



def afficherStock(book):
    if book["stock"] > 0:
        print("Yes , there is one in the stock")
    if book["stock"] <= 0:
        print("Sorry!! this  book is not in the stock")

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
    Enter 1 : in order to Enter Books :
    Enter 2 : in order to  Enter Rapor :
    Enter 3 : In order to show the owners of books :
    enter 4 : in order to show the exit : 
    """))
    if inputNumber == 1:
        GLOABL_STATE.books = donneeOFbook()
    elif inputNumber == 2:
        printReport(GLOABL_STATE.books)
    elif inputNumber == 3:
        printEtatOfOnebook(GLOABL_STATE.books)
    elif inputNumber == 4:
        printOfExit()
    clearConsole()
Welcome()






def printOfExit():
    print("Good bye")
