import random

random.seed()

while True:
    # Prompt the user for a level n
    n = input("Level: ").strip()

    # Convert input to integer
    try:
        n = int(n)
    except ValueError:
        continue

    # If the user does not input a positive integer, the program should prompt again
    if n < 1:
        continue
    else:
        break

# Generate random an integer between 1 and n, inclusive, using the random module
number = random.randint(1, n)

while True:
    # Prompt the user to guess that integer
    guess = input("Guess: ")

    # Convert input to integer
    try:
        guess = int(guess)
    except ValueError:
        continue

    # If the guess is not a positive integer, the program should prompt the user again
    if guess < 1:
        continue
    # Check if user guessed the number
    elif guess < number:
        print("Too small!")
        continue
    elif guess > number:
        print("Too large!")
        continue
    else:
        print("Just right!")
        break
