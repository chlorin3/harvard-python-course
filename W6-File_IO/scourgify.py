import sys
import csv

# Expect the user to provide two command-line arguments
if len(sys.argv) != 3:
    sys.exit("Exactly two command-line arguments should be provided")

# The first one should be the name of an existing CSV file to read as input
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Input file must be a CSV file.")

# The last one should be the name of a new CSV to write as output,
elif not sys.argv[2].endswith(".csv"):
    sys.exit("Output file must be a CSV file.")

else:
    # Open input csv file
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input file does not exist")

    # Read csv file as a dictionary
    reader = csv.DictReader(file)

    # Empty array to store students' info
    students = []

    # Append each student info to students array, but split name into a first name and last name
    for row in reader:
        students.append(
            {
                "first": row["name"].split(",")[1].lstrip(),
                "last": row["name"].split(",")[0],
                "house": row["house"],
            }
        )
    # Close input file
    file.close()

    # Open output file in write mode
    with open(sys.argv[2], "w") as file:

        # Prepare column names for a csv file
        fieldnames = ["first", "last", "house"]

        # Create dictionary writer
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write column names into csv file as first row
        writer.writeheader()

        # Append one row of information for each student
        for student in students:
            writer.writerow(
                {
                    "first": student["first"],
                    "last": student["last"],
                    "house": student["house"],
                }
            )
