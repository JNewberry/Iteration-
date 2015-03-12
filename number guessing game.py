#John Newberry
#10/11/2014
#Number guessing game
import random
target = random.randint(1,100)

attempts = 0
guess = False
while guess == False:
    number = int(input("Please enter your guess between 1 and 100: "))
    if number > 100 or number < 1:
        print("Your guess is invalid: ")
    elif number > target:
        print("Your guess is too high")
        attempts = attempts + 1
    elif number < target:
        print("your guess is too low")
        attempts = attempts + 1
    elif number == target:
        attempts = attempts + 1
        print("You guessed correctly")
        print("It took you {0} attempts".format(attempts))
        guess = True
    elif attempts = 10:
        print("You guessed 10 times, the target number was {0}".format(target))
        guess = True
