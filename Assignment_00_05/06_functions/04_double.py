def double(num):
    return num * 2

def main():
    # Ask the user for a number
    user_input = float(input("Enter a number: "))
    
    # Call the double function and print the result
    result = double(user_input)
    print(f"Double that is {result}")

if __name__ == "__main__":
    main()
