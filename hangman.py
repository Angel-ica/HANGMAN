import random
from display import stages

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word=random.choice(word_list)
        self.word_guessed=['_']*len(self.word)
        self.num_letters=len(self.word)
        self.num_lives=num_lives
        self.list_of_guesses=[]
        self.max_wrong=len(stages)-1

        print(f"Let's play Hangman \n\nThere is a secret food and you have only 5 tries to guess what it is.\n \n If you try the same word twice, you will lose a life.\n Goodluck!")
        print(f"\nThe mystery word has {len(self.word)} characters")

    def check_guess(self,guess):
            if guess.upper() in self.word.upper():
                self.num_letters-=1
                for index,value in enumerate(self.word):
                    if guess in value:
                        self.word_guessed[index]=guess.upper()
                        print('\nGood guess')
                        print(self.word_guessed)
            else:
                self.num_lives-=1
                print(f"\nOops! {guess.upper()} is not in the word, you have {self.num_lives} live(s) left")
                print(stages[self.max_wrong-self.num_lives])

    
    def ask_for_input(self):
        guess=input('>> \n Guess a letter: ')
        if len(guess)==1 and guess.isalpha():
            if guess in self.list_of_guesses:
                self.num_lives-=1
                print(f"\n{guess.upper()} has already been tried, you have {self.num_lives} live(s) left\n.")
            else:
                self.list_of_guesses.append(guess.upper())
                self.check_guess(guess)
        else:
            print(f"\nInvalid letter")

def play_game(word_list):
    game=Hangman(word_list,num_lives=5)
    while True:
        game.ask_for_input()
        if game.num_lives==0:
            print(f"Sorry, you have run out of lives \n The word is {game.word.upper()}\n")
            break
        elif game.num_letters==0:
            print(f"Congratulations! You guessed right, the word is {game.word.upper()}\n")
            break


def play_again():
    play_game
    while True:
        play=input(f"Would you like to play again? Yes/No\n")
        if play.upper()=='NO':
            print('Are you sure you want to quit?\n')
            ask=input(f"Yes/No\n")
            if ask.upper()=='YES':
                break
            else:
                play_game(word_list)
        elif play.upper()=='YES':
            play_game(word_list)
            break
        else:
            print('Invalid input, Please enter yes or no\n')



if __name__=='__main__':
    with open('text.txt','r') as f:
        word_list =f.read().splitlines()

        play_game(word_list)
        play_again()
