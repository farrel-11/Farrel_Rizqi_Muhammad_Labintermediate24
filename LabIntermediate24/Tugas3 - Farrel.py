secret_word = "boren"

def hangman():
    guesses = ""
    chances = 6
    while chances > 0:
        word_display = ""
        for letter in secret_word:
            if letter in guesses:
                word_display += letter
            else:
                word_display += "_"
        print(f"Word: {word_display}")  

        if word_display == secret_word: 
            print(f"You win! The word was: {secret_word}")
            return

        print(f"Chances left: {chances}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Enter only one letter.")
            continue
        if not ('a' <= guess <= 'z'):
            print("Enter only letters.")
            continue
        if guess in guesses:
            print("You already guessed that letter.")
            chances -= 1  
            continue

        guesses += guess

        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect.")
            chances -= 1  

    print(f"You lose! The word was: {secret_word}") 

hangman()