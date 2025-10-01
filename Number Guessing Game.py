import random

def generate_number():
    number = random.randint(1, 100)
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("You got it!")
    elif guess > number:
        print("Too High!")
    else:
        print("Too low!")
