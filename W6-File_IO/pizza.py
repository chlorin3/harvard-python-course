import sys
import csv
from tabulate import tabulate

# Expect exactly one command-line argument
if len(sys.argv) != 2:
    sys.exit("There should be one command-line argument")

# It should be the name (or path) of a CSV file in Pinocchio’s format
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

else:
    # Open csv file
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Read csv file
    reader = csv.reader(file)

    # Create empty array
    menu = []

    # Append each line to the menu
    for row in reader:
        menu.append(row)

    # Close file
    file.close()

    # Print menu using ASCII art
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))