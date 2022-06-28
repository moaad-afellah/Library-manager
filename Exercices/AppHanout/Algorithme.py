def données():
    nam1 = (input("give me name1: "))
    num1 = int(input("give me number of name1: "))
    nam2 = (input("give me name2: "))
    num2 = int(input("give me number of name 2: "))
    nam3 = (input("give me name3: "))
    num3 = int(input("give me number of name 3: "))
    nam4 = (input("give me name4: "))
    num4 = int(input("give me number of name4: "))
    list1 = []
    list1.append(nam1)
    list1.append(num1)
    list2 = []
    list2.append(nam2)
    list2.append(num2)
    list3 = []
    list3.append(nam3)
    list3.append(num3)
    list4 = []
    list4.append(nam4)
    list4.append(num4)
    listfinal=[]
    listfinal.append(list1)
    listfinal.append(list2)
    listfinal.append(list3)
    listfinal.append(list4)
    somme=num1+num2+num3+num4
    return somme,listfinal

def  moyenne (note):
    account= note /4
    return account

def  shape (note) :
    print("=========")
    print(note)
    print("=========")

def affichage(list):
    for item in list:
        print(item[0]+": "+str(item[1]))


print("Hello")
somme,listFinal = données()
note= moyenne(somme)
shape(note)

affichage(listFinal)
