while True:
    # Prompt user for input as fraction (1/4, 1/2 etc.)
    try:
        x, y = input("Fraction: ").strip().split("/")

    # If there is no "/", prompt user again for input
    except ValueError:
        continue

    # Convert x, y to integers
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        continue

    # Make sure y is lower than x
    if x > y:
        continue

    # Convert fraction to precentage, round it to the nearest integer
    try:
        percentage = round(x / y * 100)
        break

    # Catch division by zero
    except ZeroDivisionError:
        pass

# Print percentage
if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{percentage}%")