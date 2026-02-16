def isEvenOrOdd(n):
    """
    This function takes a number as input and returns "Even" if the number is even,
    and "Odd" if the number is odd.
    """
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter a number: "))
result = isEvenOrOdd(number)
print(f"The number {number} is {result}.")