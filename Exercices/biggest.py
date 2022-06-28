number=-2
list=[]
i=0

while number!=-1 :
    number = int(input("give me the numbers: "))
    list.append(number)

print(list)
max=list[0]
while i<len(list):
    if list[i]>max:
        max=list[i]
    i=i+1

print("biggest number is: ",max)







