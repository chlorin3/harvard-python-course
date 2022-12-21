def main():
    time = convert(input("What time is it? ").strip())

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    h = float(h)
    m = float(m)

    if m != 0:
        m = 60 / 100 / m

    return h + m

if __name__ == "__main__":
    main()