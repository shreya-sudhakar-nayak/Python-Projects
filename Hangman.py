import random
import sys

wordList=["DEATH","DARKNESS","CHAOS","PAINFUL","SUFFERING","TORTURE","NEGATIVITY",
          "DESPAIR","SHAMELESS","LONELINESS","HATEFUL","FAITHLESS","DISHONOURABLE",
          "REJECTION","SADNESS","WORTHLESS","COWARD","PATHETIC"]

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
guess_word=[]
secretWord=random.choice(wordList)
length_word=len(secretWord)
letter_storage=[]

def newFunc():
    while True:
        gameChoice=input("Wanna play?\n").upper()
        if gameChoice=="YES" or gameChoice=="Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("Why did you open this then?")
        else:
            print("YES or NO only!")
            continue
newFunc()

def change():
    for character in secretWord: 
        guess_word.append("_") 
    if length_word<=6:
        print("Difficulty: EASY")
    elif length_word==7 or length_word==8:
        print("Difficulty: MEDIUM")
    elif length_word>=9:
        print("Difficulty: HARD") 
    print("The word you need to guess has", length_word, "characters")
    print(guess_word)

def guessing():
    guess_taken=1
    while guess_taken<length_word:
        guess=input("Pick a letter:\n").upper()
        if not guess in alphabet: 
            print("Enter a letter from A-Z alphabet:")
        elif guess in letter_storage: 
            print("Useless! You have already guessed that letter!")
        else: 
            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for i in range(0,length_word):
                    if secretWord[i]==guess:
                        guess_word[i]=guess
                        print(guess_word)
                if not '_' in guess_word:
                    print("You won!")
                    break
            else:
                print("Do you wanna die? Try harder!!!")
                guess_taken+=1
                if guess_taken==length_word:
                    print("""You're DEAD! Game Over!\n
                    The secret word was""", secretWord)
change()
guessing()

guess_word_1=[]
secretWord_1=random.choice(wordList)
length_word_1=len(secretWord_1)
letter_storage_1=[]

def newFunc1():
    while True:
        gameAgain=input("Wanna play again?\n").upper()
        if gameAgain=="YES" or gameAgain=="Y":
            break
        elif gameAgain=="NO" or gameAgain=="N":
            sys.exit("Nice playin' with ya!")
        else:
            print("YES or NO only!")
            continue
newFunc1()

def change1():
    for character in secretWord_1: 
        guess_word_1.append("_") 
    if length_word_1<=6:
        print("Difficulty: EASY")
    elif length_word_1==7 or length_word_1==8:
        print("Difficulty: MEDIUM")
    elif length_word_1>=9:
        print("Difficulty: HARD") 
    print("The word you need to guess has", length_word_1, "characters")
    print(guess_word_1)

def guessing1():
    guess_taken_1=1
    while guess_taken_1<length_word_1:
        guess_1=input("Pick a letter:\n").upper()
        if not guess_1 in alphabet: 
            print("Enter a letter from A-Z alphabet:")
        elif guess_1 in letter_storage_1: 
            print("Useless! You have already guessed that letter!")
        else: 
            letter_storage_1.append(guess_1)
            if guess_1 in secretWord_1:
                print("You guessed correctly!")
                for i in range(0,length_word_1):
                    if secretWord_1[i]==guess_1:
                        guess_word_1[i]=guess_1
                        print(guess_word_1)
                if not '_' in guess_word_1:
                    print("You won!")
                    break
            else:
                print("Do you wanna die? Try harder!!!")
                guess_taken_1+=1
                if guess_taken_1==length_word_1:
                    print("""You're DEAD! Game Over!\n
                    The secret word was""", secretWord_1) 
change1()
guessing1()













