import sys
import requests

""" Expects the user to specify as a command-line argument the number of Bitcoins, n,
    that they would like to buy.
    If that argument cannot be converted to a float,
    the program should exit via sys.exit with an error message.
"""

if len(sys.argv) == 2:

    # Convert argument to a float
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Wrong usage! Argument is not a number")

    # Query the API for the CoinDesk Bitcoin Price Index
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Resposne error")

    # Get json-encoded content of a response
    try:
        data = response.json()
    except ValueError:
        sys.exit("Invalid json")

    # Convert rate to float
    try:
        rate = float(data["bpi"]["USD"]["rate_float"])
    except ValueError:
        sys.exit("Invalid rate")

    # Output the price of n Bitcoins to four decimal places, using , as a thousands separator.
    print(f"${rate * n:,.4f}")

else:
    sys.exit("Wrong usage! Provide one argument")