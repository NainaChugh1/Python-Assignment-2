# Q43 - Simple Coin Toss Game

import random

print("Welcome to the Coin Toss Game")

while True:

    guess = input("Guess (heads/tails): ").lower()

    while guess != "heads" and guess != "tails":
        print("Invalid Input")
        guess = input("Guess (heads/tails): ").lower()

    toss = random.choice(["heads", "tails"])

    print("Coin shows:", toss)

    if guess == toss:
        print("You guessed it right!")
    else:
        print("Wrong guess!")

    play = input("Do you want to play again? (yes/no): ").lower()

    if play == "no":
        print("Thanks for playing!")
        break
