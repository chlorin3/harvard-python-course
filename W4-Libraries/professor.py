import random

random.seed()


def main():

    # Prompt the user for a level
    level = get_level()

    # Number of math problems to solve
    problems = 10

    # User's score
    score = 0

    # Randomly generate ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with level digits
    while problems > 0:
        X = generate_integer(level)
        Y = generate_integer(level)

        # allow the user up to three tries per math problem
        tries = 3
        while tries > 0:

            # Prompt the user for solution
            answer = input(f"{X} + {Y} = ")

            # Convert input to int
            try:
                answer = int(answer)
            except ValueError:
                print("EEE")
                tries -= 1
                continue

            # Check if answer is correct
            if answer != (X + Y):
                print("EEE")
                tries -= 1
                continue
            else:
                score += 1
                break

        # after three tries output the correct answer
        if tries == 0:
            print(f"{X} + {Y} = {X + Y}")

        # Decrement number of problems
        problems -= 1

    # output the user's score, a number out of 10
    print(f"Score: {score}")


# Prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3
def get_level():

    while True:
        n = input("Level: ")

        try:
            n = int(n)
        except ValueError:
            continue

        if n in range(1, 4):
            return n


# Returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level in [2, 3]:
        return random.randint(10 ** (level - 1), 10 ** (level) - 1)
    else:
        raise ValueError


if __name__ == "__main__":
    main()