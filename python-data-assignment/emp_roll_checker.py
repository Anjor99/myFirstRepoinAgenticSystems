# Employee details stored as a tuple
employee = (101, "Anjor", "Engineering")

# Employee roles stored as a set
roles = {"editor", "viewer", "admin"}

# Print employee info using tuple indexing
print("----- Employee Information -----")
print(f"ID         : {employee[0]}")
print(f"Name       : {employee[1]}")
print(f"Department : {employee[2]}")

# Check admin access using set membership
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
