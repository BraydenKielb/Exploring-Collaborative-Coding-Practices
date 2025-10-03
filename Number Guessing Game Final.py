import random

def generate_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

def check_guess(target, guess):
    """
    Checks the player's guess against the target number.
    Returns feedback as a string.
    """
    if guess < 1 or guess > 100:
        return "Invalid input! Enter a number between 1 and 100."
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct! You win!"

def play_game():
    """Runs the interactive guessing game."""
    target = generate_number()
    guess = None
    while guess != target:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        feedback = check_guess(target, guess)
        print(feedback)

play_game()
