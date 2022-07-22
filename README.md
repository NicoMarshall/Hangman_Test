# Hangman_Test
A program that lets the user play the popular game "Hangman", by iteratively asking for a letter guess and checking if it is contained in the (randomly chosen) word.
Written in Python using Visual Studio Code.

**Milestone 1:**
Completing the ask_letter method. The user is asked for an input, which is checked to see if it is just once character and hasn't already been tried. If these checks are
passed, the check_letter method is called.
```
def ask_letter(self):
        init_letter = input("Please choose a letter: ")
        while len(init_letter) >= 2 :
            init_letter = input("Please, enter just one character: ")
        while init_letter in self.list_letters:
            init_letter = input(f'{init_letter}' " was already tried: ")   
        
        global letter
        letter = init_letter
        self.list_letters = self.list_letters + [letter]
        Hangman.check_letter(self,letter)
```        
**Milestone 2:**
Completing the check_letter method. This tests if the letter guessed by the user is in the word or not.
```
def check_letter(self, letter) -> None:
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
            Hangman.add_line(self)    
```
Depending on whether the guess is correct or not, the number of letters left to guess or the number of lives the user has left is reduced by 1.

**Milestone 3:**
Completing the add_line method. This prints a new visual everytime an incorrect guess is made, depending on the number of lives left. The last visual that outputs 
when the number of lives = 0 (so user loses) is the full hangman drawing:
```
 elif self.num_lives == 0:
            print("|-----|")
            print("|     0")
            print("|    -|-")
            print("|    / \\")
            print("|_____")
```
**Milestone 4:**
Coding the logic of the game in the play_game function. This uses a while loop to iteratively call the 3 methods within the Hangman class, until all the letters in the word 
are guessed or the user runs out of lives. Each outcome prints a final message.
```
def play_game(word_list):
    
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    while game.num_lives >= 1:
        if game.num_letters == 0 :
            print("Congratulations, you won!")
            break
        else: game.ask_letter()    
    else: print("You ran out of lives. The word was", game.word)
    ```
    
