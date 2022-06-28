number=int(input("give me the number: "))
list =[]
num=0
while num <=number :
    num=num+1
    if number%num==0:
        nam = number / num
        list.append(nam)
print(list)
print(len(list))
