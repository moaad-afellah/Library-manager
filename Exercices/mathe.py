number=int(input("give me the number higher than 1:"))

nombreDeFois = 0

while number !=1:
    nombreDeFois = nombreDeFois+1
    if number % 2 ==0 :
        number=number/2
    else:
        number=3*number+1

print('Nombre de fois : ', nombreDeFois );










