# 1. Addition function
def add(a, b):
    return a + b


# 2. Subtraction function
def subtract(a, b):
    return a - b


# 3. Multiplication function
def multiply(a, b):
    return a * b


# 4. Division function
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
