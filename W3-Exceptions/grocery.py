# Empty dictionary
groceries = {}

while True:
    # Prompt user for item (case insensitive) until they hit control+d
    try:
        item = input().upper()
    # If user hit control+d break out of the loop
    except EOFError:
        break

    # If item is in dictionary, increase amount
    if item in groceries:
        groceries[item] += 1

    # Otherwise add item to dictionary and set it's value to 1
    else:
        groceries[item] = 1

# For each item in sorted dictionary by key
for item in sorted(groceries.keys()):

    # Print key's value and key
    print(groceries[item], item)