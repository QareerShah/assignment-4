def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")

    while True:
        repeats_input = input("Enter a number of times to repeat your message: ")
        if repeats_input.isdigit():
            repeats = int(repeats_input)
            break
        else:
            print("Please enter a valid number!")

    print_multiple(message, repeats)

if __name__ == "__main__":
    main()
