import random

words = ["python", "hangman", "computer", "programming", "coding"]

# Choose a random word

word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts_left = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Word to guess: ", "".join(guessed_word))

# Game loop 

while attempts_left > 0 and "_" in guessed_word :
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        attempts_left -= 1
        print(f"Wrong guess! '{guess}' is not in the word.")
        print(f"Attempts left: {attempts_left}")

    print("Word:", "".join(guessed_word))
    print("Guessed letters:", ",".join(guessed_letters))

# Final Result

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word: ", word)
else:
    print("\nGame Over! The word was: ", word)