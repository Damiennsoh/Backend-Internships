while True:
    menu = input('''Select one of the following options below:
    r - Register a new user
    v - View a user
    d - Delete a user
    tu - Display total number of users
    e - Exit
    : ''').lower()

    # Creating a function to add new user
    def new_user():
        '''Allow a user to add a new user to the address.txt file.
        Prompt a user for the following: 
        - A full username of the person who is to be adrded,
        - A phone number,
        - Email address,
        - Age.'''
        user_name = input("What is the user's name? : ")
        user_contact = input("What is the user's contact number?: ")
        user_email = input("What is the user's email number?: ")
        user_age = input("What is the user's age?: ")

        newuser_details = {
            "user_name": user_name,
            "phone no.": user_contact,
            "email": user_email,
            "age": user_age,
        }

        # Append new user details to the output text file
        with open("address.txt", "a") as address_file:
            address_file.write(str(newuser_details) + "\n")
        print("New user added successfully!")

    def view_user():
        '''Display all users and their details from the address.txt file.'''
        with open("address.txt", "r") as address_file:
            for line in address_file:
                user_details = eval(line)
                print("User Details:")
                print("-------------")
                for key, value in user_details.items():
                    print(f"{key}: {value}")
                print()

    # Function to to delete a user from the address book
    def delete_user():
        '''Delete a user's details from the address.txt file.'''
        user_name = input("Enter the name of the user you want to delete: ")

        # Read all user details from the file and store them in a list of dictionaries
        with open("address.txt", "r") as address_file:
            user_details_list = [eval(line) for line in address_file]

        # Check if the user with the matching name exists in the list
        user_exists = any(user['user_name'] ==
                          user_name for user in user_details_list)

        if user_exists:
            # Find the user with the matching name and remove their details from the list
            updated_user_details_list = [
                user for user in user_details_list if user['user_name'] != user_name]

            # Write the updated list of user details back to the file
            with open("address.txt", "w") as address_file:
                for user in updated_user_details_list:
                    address_file.write(str(user) + "\n")
            print("User deleted successfully!")
        else:
            print("Invalid name. Please try again.")

    # function to display total number of users within the address book.

    def total_users():
        '''Display all users in the address book.'''
        user_count = 0

        # Read all user details from the file and display them
        with open("address.txt", "r") as address_file:
            for line in address_file:
                user_details = eval(line)
                # print(user_details)
                user_count += 1
        print("Total number of users:", user_count)

    if menu == 'r':
        new_user()
    elif menu == 'v':
        view_user()
    elif menu == 'd':
        delete_user()
        pass
    elif menu == 'tu':
        total_users()
    elif menu == 'e':
        print("Exiting the program")
        break
    else:
        print("Invalid option. Please try again.")
