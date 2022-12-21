def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    """ ...vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters. """
    # Check length of vanity plate
    if not 2 <= len(s) <= 6:
        return False

    # i is character's index in string
    i = 0
    alpha_allowed = True

    for c in s:
        """ No periods, spaces, or punctuation marks are allowed. """
        # If character is not alphanumeric return false
        if not c.isalnum():
            return False

        """ All vanity plates must start with at least two letters. """
        # If it's first or second character in str and it is not alphabetic return false
        if i < 2 and not c.isalpha():
            return False

        """ Numbers cannot be used in the middle of a plate; The first number used cannot be a 0. """
        # If character is equal zero and alphabetic characters are allowed (so it's first number in str) return false
        if c == "0" and alpha_allowed:
            return False

        # If character is digit (other than 0) and it's first number in str, make alphabetic chars not allowed
        elif c.isdigit() and alpha_allowed:
            alpha_allowed = False

        # If character is alphabetic and they're not allowed (because there was a digit before)
        elif c.isalpha() and not alpha_allowed:
            return False

        i += 1

    return True


main()