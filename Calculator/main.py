from art import logo

# Add
def add(a,b):
    return a + b
# Subtraction
def sub(a,b):
    return a - b
# multiplication
def multiply(a,b):
    return a * b
# division
def division(a,b):
    return a / b
operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : division,
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation? ")
        num2 = float(input("What's next number? "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        choice = input(f"Type Y to calculate with {result} or N for starting the program Again?").lower()
        if choice == "y":
            num1 = result
        else :
            should_continue = False
            calculator()
calculator()