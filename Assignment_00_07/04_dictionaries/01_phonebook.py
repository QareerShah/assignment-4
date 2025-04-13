def main():
    phonebook = {}

    while True:
        action = input("Do you want to add or search a contact? (add/search/exit): ").lower()
        
        if action == "add":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Added {name} to phonebook.\n")
        
        elif action == "search":
            name = input("Enter name to search: ")
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}\n")
            else:
                print("Contact not found.\n")

        elif action == "exit":
            print("Exiting phonebook.")
            break

        else:
            print("Invalid option. Please choose 'add', 'search', or 'exit'.\n")

if __name__ == "__main__":
    main()
