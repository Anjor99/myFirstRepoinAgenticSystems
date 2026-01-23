try:
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    while True:
        active_status=input("Are you an active user? (y/n): ").strip().lower()
        if active_status in ('y', 'n'):
            is_active = active_status == 'y'
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")
    print(f"User {name} is {age} years old. Active status: {is_active}")
except ValueError:
    print("Invalid input. Please enter a valid age.")