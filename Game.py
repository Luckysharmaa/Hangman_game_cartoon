import random
cartoon = ["doremon","pokemon","hagemaru","ultr b","ninja hattori","shinchan","pakdam pakdai","oggy and the cockroaches","ben 10","chhota bheem","mighty raju"]
cartoon_to_guess = random.choice(cartoon)
word_length = len(cartoon_to_guess)
display = ['_' * word_length]
guessed_letter = []
ramaining_lives = 6

print("Welcome to Cartoon Game! let's Play ")
print(f"The cartoon name has {word_length} letter.")

while True:
    print(f"\nLives remaining : {ramaining_lives}")
    print(' '.join(display))

    if '_' not in display:
        print(f"Congratulation! You guessed the Cartoon name ' {cartoon_to_guess}',")
        break
    if 
