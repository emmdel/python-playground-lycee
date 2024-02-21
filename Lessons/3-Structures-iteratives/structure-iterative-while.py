# get a random number between 1 and 10
import random
number = random.randint(1, 10)
attempts = 0

while True:
    # ask the user to guess the number
    guess = int(input("Guess the number: "))
    # increment the number of attempts
    attempts += 1
    # check if the user guessed the number
    if guess == number:
        print("You guessed the number!")
        break
    # give a tip if the number is too high or too low
    elif guess < number:
        print("The number is higher")
    else:
        print("The number is lower")

print("You needed", attempts, "attempts to guess the number")