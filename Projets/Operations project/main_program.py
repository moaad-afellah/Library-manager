import DataOfUser
import operates as op
from affichages import affichage

res = "error"
print("hello")
num1, num4, num3, num2 = DataOfUser.donneeMock()
type = input("Type: + or - or * : ")
if type == '+':
    res = op.somme(num1, num2, num3, num4)
elif type == '-':
    res = op.mines(num1, num2, num3, num4)
elif type == '*':
    res = op.moltiplicaton(num1, num2, num3, num4)
else:
    print("error")

if res != "error":
    affichage(res, type)
