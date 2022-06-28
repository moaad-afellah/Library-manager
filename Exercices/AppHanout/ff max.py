import random
number_of_guesses = random.randint(1, 20)
number=0
tries=int(input("tries: "))
while number < tries:
    number=number+1
    guess = input('Guess a number between 1 and 20:')
    guess = int(guess)

    if guess < number_of_guesses :
        print("this number is < number between 1 and 20" )
        print("False")
    elif guess >number_of_guesses :
        print("this number is > number between 1 and 20")
        print("False")
    elif guess == number_of_guesses :
        print("True")

        break
print("it is "+ str(number_of_guesses))
print("thanks")


