def print_even_odd_sequence():
    for num in range(10, 20):  # Loop through numbers from 10 to 19
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

def main():
    # Call the function to print the sequence
    print_even_odd_sequence()

if __name__ == "__main__":
    main()
