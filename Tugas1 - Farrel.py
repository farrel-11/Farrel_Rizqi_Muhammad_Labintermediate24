secret_word = "boren"
i = 0

def hangman():
    global secret_word
    global i
    guesses = ""  
    while True:
        guess = input("Guess a letter: ").lower() 

        if len(guess) != 1:
            print("Enter only one letter.")
            continue
        if not ('a' <= guess <= 'z'): 
            print("Enter only letters.")
            continue
        if guess == secret_word[i]:
            print("Correct!")
            guesses += guess
            i+= 1
        else:
            print("Incorrect.")
        if all(letter in guesses for letter in secret_word):
            print(f"You win! The answer is: {secret_word}")
            break

hangman()