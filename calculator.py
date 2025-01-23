num1 = int(input("Input number 1: "))
num2 = int(input("Input number 2: "))

operation = input("What mathematical operation would you like to use?")

if operation == "add" or operation == "+":
  print(add(num1, num2))

if operation == "subtract" or operation == "-":
  print(subtract(num1, num2))

if operation == "multiply" or operation == "*":
  print(multiply(num1, num2))

if operation == "divide" or operation == "/":
  print(divide(num1, num2))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise DivisionByZeroError ("Cannot divide by 0")
    return a / b
