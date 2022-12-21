# Prompt user for input
x, y, z = input("Expression: ").split(" ")

# Convert str to float
x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(f"{x / z:.1f}")