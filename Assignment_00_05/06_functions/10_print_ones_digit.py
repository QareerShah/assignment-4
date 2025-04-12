def print_ones_digit(num):
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    try:
        num = int(input("Enter a number: "))
        print_ones_digit(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
