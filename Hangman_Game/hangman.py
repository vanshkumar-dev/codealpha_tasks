import random

words = ["python", "laptop", "apple", "coding", "gaming"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")

while wrong_guesses < max_guesses:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_guesses - wrong_guesses}")

else:
    print("\nGame Over!")
    print("The word was:", word)