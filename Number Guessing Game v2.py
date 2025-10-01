import random

def generateNumber():
    return random.randint(1, 100)

def play_game():
    target = generateNumber()
    guess = None
    while guess != target:
        try:
            guess = int(input("Guess a number between 1 and 100: "))

            if guess == target:
                print("You got it!")
            elif guess > target:
                print("Too High!")
            else:
                print("Too low!")
        except ValueError:
            print("Please enter a valid integer.")
            continue

    
play_game()
