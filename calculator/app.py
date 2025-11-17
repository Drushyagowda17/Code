def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    op = input("Operation (+ - * /) or q: ")
    if op == "q":
        break
    a = float(input("First number: "))
    b = float(input("Second number: "))
    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(sub(a, b))
    elif op == "*":
        print(mul(a, b))
    elif op == "/":
        print(div(a, b))
    else:
        print("Invalid")
