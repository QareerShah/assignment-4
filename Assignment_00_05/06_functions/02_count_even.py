def count_even(lst):
    # Count even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    print("Number of even numbers:", even_count)

def main():
    # Initialize an empty list to store user input
    numbers = []
    
    # Populate the list with user input
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        if user_input == "":
            break  # Exit if the user presses Enter without typing a number
        
        # Convert input to an integer and append to the list
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    
    # Call the count_even function to print the count of even numbers
    count_even(numbers)

if __name__ == "__main__":
    main()
