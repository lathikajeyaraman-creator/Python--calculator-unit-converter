# Interactive Calculator & Unit Converter

# Function for addition
def addition(a, b):
    return a + b

# Function for subtraction
def subtraction(a, b):
    return a - b

# Function for multiplication
def multiplication(a, b):
    return a * b

# Function for division
def division(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Function to convert kilometres to miles
def km_to_miles(km):
    return km * 0.621371

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to get valid number input
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")

# Main menu
while True:
    print("\n===== MAIN MENU =====")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- Calculator ---")
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Choose operation: ")

        if operation == "1":
            print("Result:", addition(a, b))
        elif operation == "2":
            print("Result:", subtraction(a, b))
        elif operation == "3":
            print("Result:", multiplication(a, b))
        elif operation == "4":
            print("Result:", division(a, b))
        else:
            print("Invalid operation!")

    elif choice == "2":
        print("\n--- Unit Converter ---")
        print("1. Kilometres to Miles")
        print("2. Celsius to Fahrenheit")

        conversion = input("Choose conversion: ")

        if conversion == "1":
            km = get_number("Enter kilometres: ")
            print("Miles:", km_to_miles(km))

        elif conversion == "2":
            c = get_number("Enter Celsius: ")
            print("Fahrenheit:", celsius_to_fahrenheit(c))

        else:
            print("Invalid conversion!")

    elif choice == "3":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please try again.")
