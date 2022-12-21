# Menu: dictionary of items and their price
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Total cost
total = 0

while True:

    # Prompt user for item until they hit control+d
    try:
        item = input("Item: ").title()
    # If user hit control+d exit program
    except EOFError:
        print()
        exit()

    # If item is not in menu, skip rest of the loop and prompt user for input again
    if not item in menu:
        continue

    # Otherwise, add item's price to total cost
    total += menu[item]

    # Print total cost rounded to two decimal places
    print(f"Total: ${total:.2f}")
