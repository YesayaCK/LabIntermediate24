def hangman (secret_word):
    word = secret_word.lower()
    guess = ["_"]*len(word)
    guessed = []
    attempts = 6

    while attempts > 0 and "_" in guess: 
        print("\nKata yang harus ditebak: ", " ".join(guess))
        print("Huruf yang sudah ditebak: ",",".join(guessed))
            
        huruf = input("Tebak satu huruf: ").lower()

        if huruf in guessed:
            print("Kamu sudah menebak huruf ini, coba huruf yang lain")
            continue
        guessed.append(huruf)

        if huruf in word:
            for i in range(len(word)):
                if word[i] == huruf:
                    guess[i] = huruf
            print("Tebakan kamu benar")
        else:
            attempts-=1
            print(f"Tebakan salah, kesempatan tersisa:{attempts}")
            
    if "_" in guess:
        print("Kamu kalah, jawaban yang benar adalah:", word)
    else:
        print("Kamu berhasil menebaknya, jawabannya adalah:", word)
    
secret_word = input("Masukkan kata rahasia:")
            
hangman(secret_word)