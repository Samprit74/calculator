import math

def calculator():
    print("Welcome to the Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")
    print("6. Logarithm (log)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")

    choice = input("Enter choice (1-9): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero.")
        elif choice == '5':
            if num2 != 0:
                print(f"{num1} % {num2} = {num1 % num2}")
            else:
                print("Error! Division by zero for modulo.")

    elif choice == '6':
        num = float(input("Enter a number: "))
        base = input("Enter base (default is e, enter '10' for log10): ") or "e"
        if base == '10':
            print(f"log10({num}) = {math.log10(num)}")
        else:
            print(f"log({num}) = {math.log(num)}")

    elif choice in ['7', '8', '9']:
        angle = float(input("Enter angle in degrees: "))
        angle_rad = math.radians(angle)
        
        if choice == '7':
            print(f"sin({angle}) = {math.sin(angle_rad)}")
        elif choice == '8':
            print(f"cos({angle}) = {math.cos(angle_rad)}")
        elif choice == '9':
            print(f"tan({angle}) = {math.tan(angle_rad)}")

    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()
