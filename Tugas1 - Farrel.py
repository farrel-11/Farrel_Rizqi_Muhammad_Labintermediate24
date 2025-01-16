secretWord = "boren"
def hangman():
    i = 0
    while i != len(secretWord):
        userInput = input(f"Massukkan huruf "(i + 1)" :")
        
