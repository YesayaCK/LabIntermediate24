def hangman():
    word="software"
    guess=["_"]*8
    attempts=10

    while attempts > 0 and "_" in guess: 
        print("\nKata yang harus ditebak: ", " ".join(guess))
        huruf = input("Tebak satu huruf: ").lower()

        if huruf in word:
            for i in range(len(word)):
                if word[i] == huruf:
                    guess[i] = huruf
            print("Exellent guess")
        else:
            attempts-=1
            print(f"Wrong answer, attemps left:{attempts}")
            
    if "_" in guess:
        print("You lost! The word was:", word)
    else:
        print("You guessed it! The word is:", word)
            
hangman()