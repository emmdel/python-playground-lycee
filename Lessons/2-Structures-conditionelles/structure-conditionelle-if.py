# get a random number between 1 and 10
import random
number = random.randint(1, 10)
# ask the user to guess the number
guess = int(input("Guess the number: "))
# check if the user guessed the number
if guess == number:
    print("You guessed the number!")
else:
    print("Sorry, the number was", number)