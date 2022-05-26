import random
from Hangman.hangmanKelimeler import words

def randomWords():
    word = random.choice(words)

    print(list(word))

    empty = len(word)* "_"
    empty = " ".join(empty)

    print(empty)

    letter = input("Lütfen bir harf giriniz: ")
    letter = letter.upper()
    for i in word:
        if i == letter:
            letterNumber = word.find(i)
            print(i)
            i.join(empty[letterNumber + letterNumber-1])
            print(empty) 

randomWords()


















