rate=int(input("give me the rate :"))
print("\n")
number=-2
name=-2
list=[]
num=0
nam=0
listd=[]
while number != -1  :
    name = (input("give me the name: "))
    number=int(input("give me the mark: "))
    print("\n")
    if number!=-1 :
        list.append(number)
        listd.append(name)


while num<len(list) :
    if list[num]>=rate:
        print("marks thats are more than  rate:" + str(listd[nam]+"."+str(list[num])))
    num = num + 1
    nam=nam+1

nam=0
num=0
listwinners=[]
listwinner =[]
while num<len(list) :
    if list[num]>=rate:
       listwinner.append(list[num])
       listwinners.append(listd[nam])
    num = num + 1
    nam=nam+1
print("Hello the winners are: "+str(listwinners))
