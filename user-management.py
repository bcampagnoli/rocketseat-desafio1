def add_user(users, name, phone, email):
    user = {"name": name, "phone": phone, "email": email, "favorite": False}
    users.append(user)
    print(f"User {name} added to the list!")

def show_users(users):
    if not users:
        print("\nNo users found.")
        return

    print("\nUser List")
    for index, user in enumerate(users, start=1):
        status = "?" if user["favorite"] else " "
        print(f"{index}. [{status}] Name: {user['name']} / Phone: {user['phone']} / Email: {user['email']}")

def update_user(users, index, new_name, new_phone, new_email):
    try:
        new_index = int(index) - 1
        if new_index >= 0 and new_index < len(users):
            if new_name: users[new_index]["name"] = new_name
            if new_phone: users[new_index]["phone"] = new_phone
            if new_email: users[new_index]["email"] = new_email
            print(f"User {index} updated successfully!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Please enter a valid number.")

def add_favorite(users, index):
    try:
        new_index = int(index) - 1
        if new_index >= 0 and new_index < len(users):
            users[new_index]["favorite"] = True
            print(f"User {index} marked as a Favorite!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Please enter a valid number.")

def show_favorites(users):
    favorites = [user for user in users if user["favorite"]]
    if not favorites:
        print("\nNo favorite users found.")
        return

    print("\nFavorite Users List")
    for index, user in enumerate(favorites, start=1):
        print(f"{index}. Name: {user['name']} / Phone: {user['phone']} / Email: {user['email']}")

def delete_user(users, index):
    try:
        new_index = int(index) - 1
        if new_index >= 0 and new_index < len(users):
            removed_user = users.pop(new_index)
            print(f"User {removed_user['name']} deleted!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Please enter a valid number.")

users = []
while True: 
    print("\nMenu:")
    print("1. Add User")
    print("2. Show Users")
    print("3. Edit User")
    print("4. Mark User as Favorite")
    print("5. Show Favorite Users")
    print("6. Delete an User")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter a name: ").strip()
        phone = input("Enter a phone number: ").strip()
        email = input("Enter an email: ").strip()
        add_user(users, name, phone, email)

    elif choice == "2":
        show_users(users)

    elif choice == "3":
        show_users(users)
        index = input("Enter the user index to update: ").strip()
        new_name = input("Enter the new name (leave blank to keep the current one): ").strip()
        new_phone = input("Enter the new phone number (leave blank to keep the current one): ").strip()
        new_email = input("Enter the new email (leave blank to keep the current one): ").strip()
        update_user(users, index, new_name, new_phone, new_email)

    elif choice == "4":
        show_users(users)
        index = input("Enter the user index to mark as Favorite: ").strip()
        add_favorite(users, index)

    elif choice == "5":
        show_favorites(users)

    elif choice == "6":
        show_users(users)
        index = input("Enter the user index to delete: ").strip()
        delete_user(users, index)

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid option! Please choose a valid one.")
