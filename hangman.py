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
        guess=guess.lower()
        if guess in self.word:
            print('\n Good guess')
            for index,value in enumerate(self.word):
                if value == guess:
                    self.word_guessed[index] = guess
            print('\nGood guess')
            print(self.word_guessed)
            self.num_letters-=1
        else:
            print(f"\nOops! {guess} is not in the word, you have {self.num_lives} live(s) left")
            print(stages[self.max_wrong-self.num_lives])
            self.num_lives-=1
        self.list_of_guesses.append(guess)



    def ask_for_input(self):
        guess=input('>> \n Guess a letter: ')
        if len(guess) != 1 and not guess.isalpha():
            print(f"\nInvalid letter")
        elif guess in self.list_of_guesses:
            print(f"\n{guess.upper()} has already been tried, you have {self.num_lives} live(s) left\n.")
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)


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
