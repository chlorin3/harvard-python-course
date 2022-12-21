import sys
import inflect

p = inflect.engine()

# Empty list for names
names = []

while True:

    # Prompt user for name
    try:
        name = input("Name: ")

    # until they input control+d
    except EOFError:
        break

    # Add name to the "names" list
    names.append(name)

# Exit program when user didn't provide names
if len(names) == 0:
    sys.exit("\nNo names provided!")

print(f"Adieu, adieu, to {p.join(names)}")
