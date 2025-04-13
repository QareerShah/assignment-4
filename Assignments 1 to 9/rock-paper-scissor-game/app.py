import random 
print("Welcome to the Number Guessing Game!")

choices = ['rock', 'paper', 'scissor']
user_score = computer_score = 0
print("let's play!")

while True:
    user_input = input("Enter your choice (rock, paper, scissor) or 'Q' to quit: ").lower()

    if user_input == 'q':
        print(f"final score - you : {user_score}, computer: {computer_score}")
        print("Thanks for playing!")
        break
    if user_input not in choices:
        print("Invalid choice, please try again.")
        continue
    computer = random.choice(choices)
    print(f"computer chose {computer}")
    if user_input == computer:
        print("It's a tie!")
    elif (user_input == 'rock' and computer == 'scissor') or \
         (user_input == 'paper' and computer == 'rock') or \
         (user_input == 'scissor' and computer == 'paper'):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"current score - you : {user_score}, computer: {computer_score}")


