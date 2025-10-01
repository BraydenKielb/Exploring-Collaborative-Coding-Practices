import random
import test_case

def generateNumber():
    return random.randint(1, 100)

def play_game(number, guess):
    """Run the guessing game using given number and initial guess."""
    target = number
    while guess != target:
        try:
            if guess < 1 or guess > 100:
                print("Invalid input! Enter a number between 1 and 100.")
            elif guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            
            # Ask for a new guess
            guess = int(input("Guess again: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

    print("You got it!")

number = generateNumber()
guess = int(input("Guess a number between 1 and 100: "))
play_game(number, guess)