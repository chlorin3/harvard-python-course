# Prompt user for file name
file = input("File name: ").strip().lower()

# Get input's part after period - extension only
extension = file.split(".")[-1]

# Depending on extension print file’s media type
match extension:
    case "gif" | "jpeg" | "png":
        print(f"image/{extension}")
    case "jpg":
        print("image/jpeg")
    case "pdf" | "zip":
        print(f"application/{extension}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")