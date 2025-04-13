def add_three_copies(my_list, data):
    for _ in range(3):
        my_list.append(data)

def main():
    # Get input from user
    message = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    # Show list before adding
    print("List before:", my_list)

    # Call the function
    add_three_copies(my_list, message)

    # Show list after adding
    print("List after:", my_list)

if __name__ == '__main__':
    main()
