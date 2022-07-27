
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.num_lives = num_lives
        self.list_letters = []
        self.word = random.choice(word_list)
        self.word_guessed = list(self.word)
        self.num_letters = len(set(list(self.word))) - len(self.list_letters)
        for index in range(len(self.word_guessed)):
            self.word_guessed[index] = "_"
        print("The mystery word has", len(list(self.word)), "characters")
        print(self.word_guessed)
        
    

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        if letter.lower() in list(self.word):
            print("Nice!", letter, "is in the word!")
            indices = [i for i, x in enumerate(list(self.word)) if x == letter.lower()]
            for index in indices:
                self.word_guessed[index] = letter.lower()
            print(self.word_guessed)    
            self.num_letters = int(self.num_letters) - 1
            
        else:
            self.num_lives = int(self.num_lives) - 1
            print("Sorry,", letter, "is not in the word. You have", self.num_lives, "lives left")
            self.add_line()
        
        pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        init_letter = input("Please choose a letter: ")
        while len(init_letter) >= 2 :
            init_letter = input("Please, enter just one character: ")
        while init_letter in self.list_letters:
            init_letter = input(f'{init_letter}' " was already tried: ")   
        
        global letter
        letter = init_letter
        self.list_letters = self.list_letters + [letter]
        self.check_letter(letter)
        
        pass
    
    
    def add_line(self):
        if self.num_lives == 4:
            print("_____")
        elif self.num_lives == 3:
            print("|")
            print("|")
            print("|")
            print("|") 
            print("|_____")
        elif self.num_lives == 2:
            print("|-----")
            print("|")
            print("|")
            print("|") 
            print("|_____")
        elif self.num_lives == 1:
            print("|-----|")
            print("|")
            print("|")
            print("|") 
            print("|_____")    
        elif self.num_lives == 0:
            print("|-----|")
            print("|     0")
            print("|    -|-")
            print("|    / \\")
            print("|_____")
        
        
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    def play_game(word_list):
        
        game = Hangman(word_list, num_lives=5)
        game.ask_letter()
        while game.num_lives >= 1:
            if game.num_letters == 0 :
                print("Congratulations, you won!")
                break
            else: game.ask_letter()    
        else: print("You ran out of lives. The word was", game.word)  
    play_game(word_list)
    
    

    
