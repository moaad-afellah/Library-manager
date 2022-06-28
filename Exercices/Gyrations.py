number=-2
list=[]
i=0
while number!=-1 :
    number = int(input("give me the numbers: "))
    list.append(number)
print(list)
numberB=int(input("wanted number: "))
found = False
while len(list)>i :
    if list[i] == numberB :
        print("number found: ",list[i])
        found = True
    i = i + 1
if found == False:
    print("number not found")
print("good bye")

