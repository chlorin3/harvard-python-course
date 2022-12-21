"""Program outputs the number of lines of code in provided python file"""

import sys


if len(sys.argv) != 2:
    sys.exit("There should be one command-line argument!")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file!")
else:
    # Open file
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Line counter
    count = 0

    # Count lines of code in that file, excluding comments and blank lines.
    for line in file:
        if not (line.lstrip().startswith("#") or line.isspace()):
            count += 1

    # Close file
    file.close()

    # Print number of lines
    print(count)
