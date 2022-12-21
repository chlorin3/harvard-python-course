input = input("Input: ")

# For each character in input
for c in input:

    # If character is NOT a vowel
    if not c.lower() in ["a", "e", "i", "o", "u"]:

        # Print this character 
        print(c, end="")

print()