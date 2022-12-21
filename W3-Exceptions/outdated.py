months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    # Prompt user for date
    date = input("Date: ").strip()

    """Split date into month, day, year depending on date format"""

    # If there's comma
    if "," in date:
        # Replace it with a space and split with space delimiter into M(onth), D(ay), Y(ear)
        try:
            M, D, Y = date.replace(", ", " ").split(" ")
        except ValueError:
            continue

    # If there's no comma, split with "/" delimiter into M(onth), D(ay), Y(ear)
    else:
        try:
            M, D, Y = date.split("/")
        except ValueError:
            continue

        # Using this date format make sure M is a number
        if not M.isdecimal():
            continue

    # Check if month is month name (so it is not a number/not decimal)
    if not M.isdecimal():

        # If so, get month's index from 'months' table and add 1
        try:
            M = months.index(M) + 1
        except ValueError:
            continue

    # Otherwise month is a number, so convert it into integer
    else:
        M = int(M)

    # Convert D into integer
    try:
        D = int(D)
    except ValueError:
        continue

    # Make sure D is a proper day, M is a proper month and year is a number
    if not (1 <= D <= 31 and 1 <= M <= 12 and Y.isdecimal()):
        continue

    # Date is correct so break out of the loop
    break

# Print date in expected format
print(f"{Y}-{M:02}-{D:02}")
