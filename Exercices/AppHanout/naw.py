import sys
sys.path.append('/Practice/Exercices/AppHanout/printFacture1.py')
"""
import printFacture1
printFacture1.printFactute1(productsList)

"""
from printFacture1 import printFactute1

print(" welcome")
n = 1
productsList = []
while n < 4:
    name = (input("Give me name of article" + str(n) + ": "))
    quantity = (int(input("enter quantity of article" + str(n) + ": ")))
    price = (int(input("enter price of one article" + str(n) + ": ")))
    sum = quantity * price
    infoProductDict = {"id": n, 'product': name, 'quantity': quantity, 'price': price, 'totality': sum}
    print(infoProductDict)
    n = n + 1
    productsList.append(infoProductDict)

printFactute1(productsList)
