import sys
from PIL import Image, ImageOps

# Specify exactly two command-line arguments
if len(sys.argv) != 3:
    sys.exit("Provide two command-line arguments")

# The input’s and output’s names must end in .jpg, .jpeg, or .png, case-insensitively
elif not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) or not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Input and output files must be a JPEG or PNG")

# The input’s name must have the same extension as the output’s name
elif sys.argv[1].lower().split(".")[-1] != sys.argv[2].lower().split(".")[-1]:
    sys.exit("The input's name does not have the same extension as the output's name")

else:
    # Open input file
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input file was not found")

    # Open shirt file
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt file was not found")

    # Resize and crop input image to match shirt size
    image = ImageOps.fit(image, shirt.size)

    # Overlay shirt.png (which has a transparent background) on the input
    image.paste(shirt, mask=shirt)

    # Save the result as desired output name
    image.save(sys.argv[2])