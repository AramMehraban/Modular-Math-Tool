import math_operations as math_ops

def main():
    print("Willkommen beim Modular Math Tool 🧮")

    try:
        a = float(input("Gib die erste Zahl ein: "))
        b = float(input("Gib die zweite Zahl ein: "))

        print(f"{a} + {b} = {math_ops.add(a, b)}")
        print(f"{a} - {b} = {math_ops.subtract(a, b)}")
        print(f"{a} * {b} = {math_ops.multiply(a, b)}")
        print(f"{a} / {b} = {math_ops.divide(a, b)}")

    except ValueError:
        print("Fehler: Bitte eine gültige Zahl eingeben.")

if __name__ == "__main__":
    main()