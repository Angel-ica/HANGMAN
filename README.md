# Hangman
Hangman is a simple word guessing game. The program randomly selects a word from a list of given words, a hangman then asks the user for a letter and checks if it is in the randomly selected word.
It starts with a default number of trials which we call lives and as we know now, a random word from the list of words.
It showcases a fun display to account for the users progress. The game terminates if the user runs out of lives but of course there's an option to play again!


```python
import random

#'word' returns a random word in word_list
word=random.choice(word_list)

#Parameters
word_list: list
    List of words to be used in the game
num_lives: 5
    Number of lives the player has.
    Note that this does not depend of the length of the word.
    
#Attributes:
word: str
    The word to be guessed picked randomly from the word_list
word_guessed: list
    A list of the letters of the word, with '_' for each letter yet guessed yet.
    For example, if the word is 'GUAVA', the word_guessed list would be ['_', '_', '_', '_', '_']
    If the player guesses 'G', the list would be ['G', '_', '_', '_', '_']
    Notee that the guess can be set to uppercase using .upper()

num_letters: int
        The number of  letters in the word that have not been guessed yet
num_lives: 5
        The number of lives the player has
list_of_guesses: list
    A list of the letters that have already been tried

#Methods
Methods are basically functions in a class. Note that all methods are functions but not all functions are methods.

def check_guess(self,guess)
        Checks if the letter is in the word. If it does, get the index and replace the '_' in word_guessed with the guess. Else, reduce the life and display the hangman.
def ask_for_input(self)
        Asks the user for a letter.
        if the length of the guess is equal to 1 and the guess is an alphabet, checks if the guess already exists in  word_guessed and reduces a life if it does. Else, append the guess to word_guessed and call the check_guess method.

#Functions
def play_game(word_list):
    prints a little introduction to the game and  continously asks the user for  an input/guess. Tells the player whether they win or lose.
def play_again():
    Plays the game again if the user agrees to

#Code Execution
if__name=='__main__':
    allows you to execute code that should run only when the file is executed as a scipt and not imported as a module.

#Context managers
with open('text.txt','r') as f:
    word_list =f.read().splitlines()

#calls the functions
        play_game(word_list)
        play_again

```

Feel free to clone this repo ;)
