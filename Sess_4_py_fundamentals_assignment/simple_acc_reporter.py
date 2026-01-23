try:
    val=float(input("Enter an accuracy value: "))
    print(f"Model accuracy is {val}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")