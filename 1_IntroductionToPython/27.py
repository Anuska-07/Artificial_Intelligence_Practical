#Create a number guessing game using functions and loops.
import random
def guessing_game():
    secret=random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == secret:
            print("Correct! You guessed the number.")
            break
        elif guess < secret:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
guessing_game()