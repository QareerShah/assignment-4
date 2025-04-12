# Problem #1: List Practice
def list_practice():
   
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    print(f"Length of the list: {len(fruit_list)}")
    
    # Add 'mango' at the end of the list.
    fruit_list.append('mango')
    
    # Print the updated list.
    print(f"Updated list: {fruit_list}")

# Problem #2: Index Game
def access_element(lst, index):
    # Check if the index is valid
    if index < 0 or index >= len(lst):
        return "Index out of range."
    return lst[index]

def modify_element(lst, index, new_value):
    # Check if the index is valid
    if index < 0 or index >= len(lst):
        return "Index out of range."
    lst[index] = new_value
    return lst

def slice_list(lst, start, end):
    # Handle invalid slice indices
    if start < 0 or end > len(lst) or start > end:
        return "Invalid slice indices."
    return lst[start:end]

def index_game():
    # Initialize an example list to simulate user input or prior context
    game_list = ['apple', 'banana', 'orange', 42, 'grape']

    print("Welcome to the Index Game!")
    print("Choose an option:")
    print("1: Access an element")
    print("2: Modify an element")
    print("3: Slice the list")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        index = int(input(f"Enter an index (0 to {len(game_list)-1}): "))
        print(access_element(game_list, index))

    elif choice == 2:
        index = int(input(f"Enter an index (0 to {len(game_list)-1}): "))
        new_value = input("Enter the new value: ")
        print(modify_element(game_list, index, new_value))

    elif choice == 3:
        start = int(input(f"Enter the start index (0 to {len(game_list)-1}): "))
        end = int(input(f"Enter the end index (0 to {len(game_list)-1}): "))
        print(slice_list(game_list, start, end))

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

def main():
   
    print("Running List Practice...\n")
    list_practice()
    print("\n")

   
    index_game()

if __name__ == "__main__":
    main()
