camelCase = input("camelCase: ").strip()
snake_case = ""

# For each character in camelCase
for c in camelCase:

    # If a character is uppercase
    if c.isupper():

        # Add underscore and lowercased character to snake_case str
        snake_case += "_" + c.lower()

    # Otherwise just add character to snake_case str
    else:
        snake_case += c

print(snake_case)
