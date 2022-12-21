def main():
    print(convert(input()))

def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

if __name__ == "__main__":
    main()