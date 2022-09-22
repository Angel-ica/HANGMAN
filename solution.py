import random

with open('file.txt','r') as file:
    word_list=file.readlines()
    word=random.choice(word_list)
    #print(word)
def check_guess(guess):
    if guess.lower() in word:
        print(f"good guess, {guess} in word")
    else:
        print(f"sorry, {guess} not in word. Try again")

def ask_for_input():
    while True:    
        guess=input('guess a letter: ')
        if guess==1 and guess.isalpha():
            print('Good guess')
        else:
            break
        print('oops! not a valid letter')
    check_guess(guess)

ask_for_input()
