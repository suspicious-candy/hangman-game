import random
from words import words
win=0
lose=0

def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.lower()


def hangman(word):
    global lose
    global win
    word=str(word)
    wordlist= {}
    displaylist=[]
    life=6
    used=''
    for i in range(0,len(word)):
        wordlist[i]=word[i]
        displaylist.append("_")

    letters_remaining= len(set(wordlist))

    while life>0 and letters_remaining>0:

        user=str(input("enter letter ")).strip().lower()
        while user in used :
            print("all ready used letter")
            user=str(input("enter letter ")).strip().lower()
        while len(user)>1:
            print("use only one word")
            user=str(input("enter letter ")).strip().lower()
        used+=user


        if user in wordlist.values():
            for key in wordlist:
                if(wordlist[key] == user):
                    displaylist[key]=user
                    letters_remaining-=1
        else:
            life-=1
        displayString="".join(displaylist)
        print (f'{displayString} life remaining = {life}')

    if(life==0):
        lose +=1
        print(f'you lose!!! The word was {word}')
        print(f'Score So Far wins:{win} lose:{lose}')
    if(letters_remaining==0):
        win+=1
        print("you win")
        print(f'Score So Far wins:{win} lose:{lose}')

def game():
    toplay = 'y'
    while toplay == 'y':
        toplay = input("Do you wanna play (y/n)? ").strip().lower()
        if toplay == 'y':
            hangman(get_valid_word(words))
        elif toplay == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' to play or 'n' to exit.")

game()