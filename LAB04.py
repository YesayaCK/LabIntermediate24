import random
def hangman(secret_word):
    word = secret_word.lower()
    guess = ["_"] * len(word)
    guessed = []
    attempts = 6

    while attempts > 0 and "_" in guess:
        print("\nKata yang harus ditebak:", " ".join(guess))
        print("Huruf yang sudah ditebak:", ", ".join(sorted(guessed)))
        
        huruf = input("Tebak satu huruf: ").lower()

        if not huruf.isalpha() or len(huruf) != 1:
            print("Masukkan satu huruf saja!")
            continue

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
            attempts -= 1
            print(f"Tebakan salah, kesempatan tersisa: {attempts}")
            
    if "_" in guess:
        print("Kamu kalah, jawaban yang benar adalah:", word)
    else:
        print("Kamu berhasil menebaknya, jawabannya adalah:", word)

def main():
    word_list = ["Prasmul", "Software", "Indonesia"]
    
    while word_list:
        secret_word = random.choice(word_list)
        word_list.remove(secret_word)  
        
        hangman(secret_word)
        
        if not word_list:
            print("Kata sudah habis, permaianan selesai!")
            break

        choice = input("Apakah ingin bermain lagi? (yes/no): ").lower()
        if choice != "yes":
            print("Permainan selesai!")
            break

if __name__ == "__main__":
    main()
