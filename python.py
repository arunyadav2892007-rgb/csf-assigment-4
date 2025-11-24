# Function to add two numbers
def add(x, y):
    """Returns the sum of x and y."""
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

# Function to divide two numbers
def divide(x, y):
    """Returns the quotient of x divided by y. Handles division by zero."""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator_main():
    """The main function to run the console calculator."""
    print("----------------------------")
    print("Simple Console Calculator")
    print("----------------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("----------------------------")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            # Ask user if they want another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input. Please select a valid operation.")

if __name__ == "__main__":
    calculator_main()
