secret_word = "boren"

def hangman():
    guesses = ""  # Initialize guesses within the function
    while True:
        guess = input("Guess a letter: ").lower() 
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue
        if not ('a' <= guess <= 'z'): 
            print("Please enter only letters.")
            continue
        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses += guess

        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect.")
        if all(letter in guesses for letter in secret_word):
            print("You win!")
            break
        if len(guesses) == 6:
            print("You lose! The word was:", secret_word)
            break

hangman()