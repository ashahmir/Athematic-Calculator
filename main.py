from art import logo
print(logo)


def add(num1, num2):
    """Performs addition on two numbers and returns their sum"""
    return num1 + num2


def sub(num1, num2):
    """Performs subtraction on two numbers and returns their difference"""
    return num1 - num2


def multiply(num1, num2):
    """Performs Multiplication on two numbers and returns their product"""
    return num1 * num2


def divide(num1, num2):
    """Performs Division on two numbers and returns their Quotient"""
    return num1 / num2


calc_functions = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}


calc_on = True
memory = 'n'
result = 0
n1 = 0
n2 = 0
while calc_on:
    if memory == '=':
        n1 = result
        operation = input("+\n-\n*\n\\\nChoose an operation: ")
        n2 = float(input("Enter the next number: "))
    else:
        n1 = float(input("Enter the first number: "))
        operation = input("+\n-\n*\n\\\nChoose an operation: ")
        n2 = float(input("Enter the Second number: "))
    result = calc_functions[operation](n1, n2)
    print(f"Result: {result}")
    memory = input(f"Type '=' to continue with calculating with {result}, or enter 'n' to start a new calculation: ")
    while memory != '=' and memory != 'n':
        print("Invalid Input")
        memory = input(f"Type '=' to continue with calculating with {result}, or enter 'n' to start a new calculation: ")
    print("\n"*100)
