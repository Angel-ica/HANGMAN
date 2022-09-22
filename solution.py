import random

with open('file.txt','r') as file:
    word_list=file.readlines()
    word=random.choice(word_list)
    print(word)

    guess=input('guess a letter: ')
    if guess==1 and guess.isalpha():
        print('Good guess')
    else:
        print('oops! not a valid letter')
    