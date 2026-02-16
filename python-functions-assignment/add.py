def add(a, b):
    """
    This function takes two numbers as input and returns their sum.
    """
    return a + b

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
result = add(a, b)
print(f"The sum of {a} and {b} is: {result}")