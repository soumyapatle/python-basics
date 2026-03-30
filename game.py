import random

number = random.randint(1, 100)
guess = None
attempts = 0

print("Welcome to the Number Guessing Game 😄")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct! 🎉 Attempts:", attempts)
