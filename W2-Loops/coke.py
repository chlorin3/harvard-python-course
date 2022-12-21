# Amount due
amount = 50

# While amount due is greater than zero
while amount > 0:

    # Inform user of amount due
    print(f"Amount Due: {amount}")

    # Prompt user to insert a coin
    inserted = int(input("Insert Coin: "))

    # Check if coin is in accepted denomination
    if inserted in [25, 10, 5]:

        # If so, subtract coin value from amount due
        amount -= inserted

# Inform user of change owed
print(f"Change Owed: {-amount}")