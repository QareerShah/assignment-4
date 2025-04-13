import random

print("Welcome to the Number Guessing Game!")

low = 1
high = 10

print("Think of a number between 1 to 10. and computer will guess the number.")

if low <= high:
    computer_guess = random.randint(low, high)
    print(f"Computer guessed: {computer_guess}")

    while True:
        user_input = input("Is the guess too high (H), too low (L), or correct (C)? ").strip().upper()

        if user_input == 'H':
            high = computer_guess - 1
            computer_guess = random.randint(low, high)
            print(f"Computer guessed: {computer_guess}")
        elif user_input == 'L':
            low = computer_guess + 1
            computer_guess = random.randint(low, high)
            print(f"Computer guessed: {computer_guess}")
        elif user_input == 'C':
            print("Yay! The computer guessed your number.")
            break
        else:
            print("Invalid input. Please enter H, L, or C.")


if low > high:
    print("Invalid range. Please try Again.")