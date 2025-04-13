import random 

def main():
    secret_number = random.randint(0, 99)
    print("Welcome to the Guess My Number game!")

    while True:
        try:
            guess = int(input("Enter your guess (0-99): "))
            
            if guess > secret_number:
                print("Your guess is too high\n")

            elif guess < secret_number:
                print("Your guess is too low\n")
            else:
                print("Congratulations! You've guessed the number!")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 99.")

if __name__ == "__main__":
    main()