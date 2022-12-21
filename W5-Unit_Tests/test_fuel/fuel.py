def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):

    try:
        x, y = fraction.strip().split("/")
    except ValueError:
        raise ValueError("There is no '/'")

    # Convert x, y to integers
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError("X or/and Y is not an integer")

    # Make sure y is lower than x
    if x > y:
        raise ValueError("X is greater than Y")

    # Convert fraction to precentage, round it to the nearest integer
    try:
        percentage = round(x / y * 100)

    # Catch division by zero
    except ZeroDivisionError:
        raise ZeroDivisionError("You are dividing by ZERO!")

    return percentage


def gauge(percentage):
    # Make sure input is an int
    # try:
    #     percentage = int(percentage)
    # except ValueError:
    #     raise ValueError("Input is not an integer!")
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()