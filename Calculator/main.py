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
num2 = int(input("What's the second number? "))
for i in operations:
    print(i)