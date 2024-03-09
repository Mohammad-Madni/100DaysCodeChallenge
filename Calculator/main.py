from art import logo
print(logo)

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
num1 = int(input("What's the first number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number? "))
calculation_function = operations[operation_symbol]
result = calculation_function(num1,num2)


print(f"{num1} {operation_symbol} {num2} = {result}")