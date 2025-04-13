import random

# Hangman stages
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''']

# Word options
word_list = ["apple", "mango", "banana", "orange", "grape", "kiwi", "peach", "pear"]

# Choose a random word
chosen_word = random.choice(word_list)
word_display = ['_' for _ in chosen_word]
guessed_letters = []
lives = len(stages) - 1

# Welcome message
print("Welcome to Hangman!")
print("Guess the fruit word.")

# Game loop
while True:
    print(" ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        lives -= 1
        print(stages[len(stages) - 1 - lives])

    # Check win condition
    if "_" not in word_display:
        print(" ".join(word_display))
        print("Congratulations! You won! 🎉")
        break

    # Check lose condition
    if lives == 0:
        print(stages[-1])
        print(f"You lost! The word was '{chosen_word}'.")
        break
