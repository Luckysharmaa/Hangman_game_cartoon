import random

# List of Cartoon Name
cartoon = ["doremon","pokemon","hagemaru","ultr b","ninja hattori","shinchan","pakdam pakdai"
           ,"oggy and the cockroaches","ben 10","chhota bheem","mighty raju"]

# Choose a random Cartoon from the list
cartoon_to_guess = random.choice(cartoon)
word_length = len(cartoon_to_guess)
display = ['_'] * word_length
guessed_letters = []
remaining_lives = 6

print("Welcome to Hangman Game! Let's play with Cartoon!.")
print(f"The cartoon title has {word_length} letters.")

while True:
    print(f"\nLives remaining: {remaining_lives}")
    print(' '.join(display))

    if '_' not in display:
        print(f"Congratulations! You guessed the cartoon '{cartoon_to_guess}'.")
        break

    if remaining_lives == 0:
        print(f"Game Over! The cartoon was '{cartoon_to_guess}'.")
        break

    guess = input("Guess a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in cartoon_to_guess.upper():
        indices = [i for i, letter in enumerate(cartoon_to_guess.upper()) if letter == guess]
        for index in indices:
            display[index] = cartoon_to_guess[index]
    else:
        remaining_lives -= 1
        print(f"'{guess}' is not in the cartoon title.")
