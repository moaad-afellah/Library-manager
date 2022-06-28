prs1=int(input("person1:how much money do you have ?:"))
prs2=int(input("person2:how much money do you have ?:"))
while prs1>0 and prs2>0 :
    number=int(input("money consumed :"))
    prs1 = prs1 - number
    prs2 = prs2 - number
    if prs2<0 and prs1<0:
        print("the rest is: person1: " + str(0) + "        person2: " + str(0))
    elif prs2<0 and prs1>0:

        print("the rest is: person1: " + str(prs1) + "        person2: " + str(0))
    elif prs1<0 and prs2>0:

        print("the rest is: person1: " + str(0) + "        person2: " + str(prs2))
    else:

        print("the rest is: person1: "+str(prs1) + "        person2: "+str(prs2))
if prs1<0 and prs2>0:
    print("person1: his money's complete")
    print("person2:the rest is "+str(prs2))
elif prs2<0 and prs1>0 :
    print("person2: his money's complete")
    print("person1:the rest is "+str(prs1))
elif prs2<=0 and prs1<=0 :
    print("person1: his money's complete")
    print("person2: his money's complete")
print("god bay")
