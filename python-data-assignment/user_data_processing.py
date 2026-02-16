# Function to calculate average score
def calculate_average(scores):
    return sum(scores) / len(scores)


# Function to check admin access
def has_admin_access(roles):
    return "admin" in roles


# Function to process users and return results
def process_users(users):
    results = []

    for user in users:
        name = user["name"]
        scores = user["scores"]
        roles = user["roles"]

        average = calculate_average(scores)
        admin_status = has_admin_access(roles)

        # storing as tuple (example use of tuple)
        results.append((name, average, admin_status))

    return results

def input_user(user_number):
    name = input(f"Enter user {user_number} name: ")
    scores_input = input(f"Enter user {user_number} scores separated by spaces: ")
    scores = [int(score) for score in scores_input.split()]
    roles = {"admin", "editor", "viewer"}
    final_roles = roles.copy()  # Create a copy to modify based on user input
    # ask user to validate each access
    for role in roles:
        access = input(f"Does the user have {role} access? (yes/no): ")
        
        while access.lower() not in ["yes", "no"]:
            access = input(f"Please enter 'yes' or 'no'. Does the user have {role} access? (yes/no): ")
            
        if access.lower() != "yes":
            final_roles.remove(role)
    
    return {"name": name, "scores": scores, "roles": final_roles}


# Main function
def main():
    try:
        # List of users (user input)
        users = []
        num_users = int(input("Enter the number of users to process: "))
        for i in range(num_users):
            user_data = input_user(i+1)
            users.append(user_data)

        # Process user data
        processed_data = process_users(users)

        # Print output
        for name, avg, is_admin in processed_data:
            print(f"Name: {name}")
            print(f"Average Score: {avg:.1f}")
            print(f"Admin Access: {is_admin}")
            print()
    except ValueError:
        print("Invalid input.")

# Run program
if __name__ == "__main__":
    main()
