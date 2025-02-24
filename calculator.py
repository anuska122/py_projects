# Calculator

def get_number(number):
    """Prompt the user to input a valid integer or float."""
    while True:
        operand = input(f"Enter number {number}: ")
        try:
            if '.' not in operand:
                return int(operand)  # Convert to int if no decimal point
            else:
                return float(operand)  # Convert to float if decimal point is present
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate(a, b, operator):
    """Perform the desired arithmetic operation."""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Invalid operator. Please use one of +, -, *, /.")
        return None

def main():
    """Main program loop for the calculator."""
    print("Welcome to the Calculator!")
    print("Available operators: +, -, *, /")
    print("Type 'exit' anytime to quit.")

    while True:
        # Get the first number
        a = get_number(1)
        
        # Get the operator
        while True:
            operator = input("Enter an operator (+, -, *, /): ")
            if operator.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                return
            if operator in ['+', '-', '*', '/']:
                break
            else:
                print("Invalid operator. Please use one of +, -, *, /.")

        # Get the second number
        b = get_number(2)

        # Perform the calculation
        result = calculate(a, b, operator)
        if result is not None:
            print(f"Result: {result}")

main()