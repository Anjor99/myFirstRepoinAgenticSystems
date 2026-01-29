# Access Control System

# Age Input
age=int(input("Enter your age: "))

# ID Input
id_input=input("Do you have an ID? (yes/no): ").strip().lower()

# Validate ID input
while id_input not in ["yes", "no"]:
    print("Invalid input. Please enter 'yes' or 'no'.")
    id_input=input("Please enter 'yes' or 'no': ").strip().lower()

# ID Flag    
has_id=id_input=="yes"

# Access Decision
if age>=18 and has_id:
    print("Entry allowed")
else:
    print("Entry Denied")