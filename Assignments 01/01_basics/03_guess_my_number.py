import random

def main():
  
    secret_number = random.randint(0, 5)
    
    print("I am thinking of a number between 0 and 99...")

    while True:
        guess = int(input("Enter a guess: "))
        
        if guess < secret_number:
            print("Your guess is too low\n")
        elif guess > secret_number:
            print("Your guess is too high\n")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break


if __name__ == "__main__":
    main()
