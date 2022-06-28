def donnée():
    num1 = int(input("give me number 1: "))
    num2 = int(input("give me number 2: "))
    num3 = int(input("give me number 3: "))
    num4 = int(input("give me number 4: "))
    return num1, num4, num3, num2


def somme(num1, num2, num3, num4):
    som = num1 + num4 + num3 + num2
    return som


def mines(num1, num2, num3, num4):
    min = num1 - num2 - num3 - num4
    return min


def moltiplicaton(num1, num2, num3, num4):
    mol = num1 * num2 * num3 * num4
    return mol


def affichage(res, type):
    print("<=======>")
    print("You have select: " + type)
    print(res)
    print("<=======>")


res = "error"
print("hello")
num1, num4, num3, num2 = donnée()
type = input("Type: + or - or * : ")
if type == '+':
    res = somme(num1, num2, num3, num4)
elif type == '-':
    res = mines(num1, num2, num3, num4)
elif type == '*':
    res = moltiplicaton(num1, num2, num3, num4)
else:
    print("error")

if res != "error":
    affichage(res, type)
