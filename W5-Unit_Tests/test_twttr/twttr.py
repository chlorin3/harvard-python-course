def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    new_word = ""

    # Go through each letter in word
    for c in word:

        # If character is NOT a vowel
        if not c.lower() in ["a", "e", "i", "o", "u"]:

            # Add character to new word
            new_word += c

    return new_word


if __name__ == "__main__":
    main()
