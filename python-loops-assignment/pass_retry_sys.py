valid_pass="admin123"
password=input("Enter your password: ")

while password!=valid_pass:
    print("Incorrect password. Please try again.")
    password=input("Enter your password: ")
    
print("Access granted.")