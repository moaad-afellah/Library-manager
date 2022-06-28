def multiple(number):
    listOfMultiple = []
    num = 1
    m = "*"
    for i in range(1, 21):
        multiple = number * i
        if i % 3 == 0:
            listOfMultiple.append(multiple)
            listOfMultiple.append(m)
        else:
            listOfMultiple.append(multiple)

    return listOfMultiple


def tripl(number):
    listOfTripl = [number]
    tripl = number
    num = 0

    while num < 12 :
        tripl = 3 * tripl
        num = num + 1
        listOfTripl.append(tripl)

    return listOfTripl


def draw(number):
    num = 0
    while num <= number:
        print(num * "*")
        num = num + 1


def triangle(number):
    num = 0
    print("*")
    print("* *")
    while num <= number - 4:
        print("*", num * " ", "*")
        num = num + 1
    print((number +1) * "*" )


triangle(54)


multiple = multiple(7)
for i in multiple:
    print(i, end=" ")

draw(12)

triangle(54)