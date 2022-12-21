from pyfiglet import Figlet, FigletFont
import sys
from random import choice

# Get list of all available fonts
fonts = FigletFont.getFonts()

# Check if two command-line arguments were provided, the first of the two
# should be -f or --font, and the second of the two should be the name of the font
if len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    f = Figlet(font=sys.argv[2])

# If zero command-line arguments, choose random font
elif len(sys.argv) == 1:
    f = Figlet(font=choice(fonts))

# Otherwise display error message and exit program
else:
    sys.exit("Wrong usage! Provide two arguments or none and make sure font exists!")

# Prompt user for input
text = input("Input: ").strip()
# Print user's input with new font
print(f"Output:\n {f.renderText(text)}")
