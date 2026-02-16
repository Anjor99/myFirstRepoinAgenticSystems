contact_book = {
 "Ravi": "9876543210",
 "Anita": "9123456780",
 "Anjor": "9988776655"
}

user_options = {
    "1": "View all contacts",
    "2": "Search for a contact",
    "3": "Exit"
}

while True:
    # Displaying the menu (1: View all contacts, 2: Search for a contact, 3: Exit)
    print("\nContact Book Menu:")
    for key, value in user_options.items():
        print(f"{key}. {value}")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        # Display all contacts
        print("\nAll Contacts:")
        for name, number in contact_book.items():
            print(f"{name}: {number}")
    
    elif choice == "2":
        # Search for a contact
        search_name = input("Enter the name to search: ")
        if search_name in contact_book:
            print(f"{search_name}'s contact number is: {contact_book[search_name]}")
        else:
            print(f"{search_name} not found in contact book.")
    
    elif choice == "3":
        # Exit the program
        print("Exiting the contact book. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

