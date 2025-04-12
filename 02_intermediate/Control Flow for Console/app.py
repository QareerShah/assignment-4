import random

NUM_ROUNDS = 5

def get_valid_guess():
    while True:
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        if guess in ['higher', 'lower']:
            return guess
        else:
            print("Please enter either 'higher' or 'lower'.")

def main():
    print("🎮 Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\n🚀 Round {round_num}")
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")

        guess = get_valid_guess()

        if user_number == computer_number:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        elif (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")

    print("\n🎉 Thanks for playing!")

    # Endgame performance evaluation
    if score == NUM_ROUNDS:
        print("🌟 Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("👍 Good job, you played really well!")
    else:
        print("🙃 Better luck next time!")

if __name__ == "__main__":
    main()
