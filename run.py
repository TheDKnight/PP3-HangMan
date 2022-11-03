import random 


def welcome() :
    """
    Welcome functions Takes the users name and checks it again the is alphabetic built in function of python
    It will not progress unless the correct input is inputed.
    """

    name = input("Welcome to PP3 Hangman Game Please Enter Your Name Below:\nName: ")
    while name.isalpha() == False :
        print("Please only enter alphabetic letters for your name") 
        #name = input("Please enter your name again: ")
    else: 
        print(f"Welcome {name}, You will be playing against the computer today from a randomly selected word list.")
    
    return(name) 


def randomWord():
    """
    The randomWord functions opens the words.txt file and takes a random word from the list using the import random function.
    It also strips the word of any whtie space and returns the word.
    """
    f = open('words.txt', 'r')
    word = random.choice(f.readlines()).strip()
    f.close()
    return(word)

def playAgain():
    """
    The play again function allows the user to restart the game
    or exit the program after they win or lose.
    """
    play = input("\nGame is finished, would you like to play another game?\n\nPress y for another game or n to exit").lower()
        
    if len(play) != 1 or not play.isalpha():
        print("Please enter either a y or ")
    elif play == "y" :
        main()
    elif play == "n": 
        exit()
    return(playAgain())

def main():
    """
    The main function is where the main game is run.
    It first takes the welcome value/username and then takes a random word from the random word function
    It gets the lengthh of the random word and outputs it for the user.
    It also creates a blank list for the guessed words and a blank line for the random word
    The line matchs how many words the randomword has
    """

    welcome()
    gameWord = randomWord()
    lenGameWord = len(gameWord) 
    print(f"\nThe word is {lenGameWord} Characters Long\n")
    guessed_letters = []
    blanks = len(gameWord) * '_'
    blanks = list(blanks)
    
    """
    We assign 6 lives to the user and from the input value it checks that the user has only entered 1 characters.
    It also only allows the user to input the alphabetic characters.
    It stores the values of the users guess in a list and alerts the user if they have entered it allready, 
    a list of entered guess is at the bottom of the screen.
    If the guess is in the word the guess is added to the guessed list and the blank list is updated with the guess in the correct place.
    It then prints a new join to the list.
    It alerts the user if the guess is in the word or not
    """
    lives = 5
    while lives > 0:
        guess = input("Enter A Letter \n").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease only enter a single alphabetic letter for your guess")
        elif guess in guessed_letters:
            print("\nLetter has been guessed allready")
        elif guess not in gameWord :
            lives -= 1
            guessed_letters.append(guess)
            print(f"{guess} Is not in the selcted word You have {lives} lives left")  
            print(''.join(blanks)) 
        elif guess in gameWord:
           for i in gameWord:
               for i, char in enumerate(gameWord):
                   if char == guess:
                      blanks[i] = guess
           guessed_letters.append(guess)
           print(F"{guess} is in the word\n")
           print(''.join(blanks))
           
        print(f"\nLetters Guessed Allready {guessed_letters}")

        """
        If the blanks list is the same as the random word then the user has won
        User is asked do they want to play again.
        Otherwise user loses
        """
        if ''.join(blanks) == gameWord:
            print(f'\nYou won. The secret word was: {gameWord}.')
            playAgain()
        
    else:
        print("")
        print(f'\nYou Lose. The secret word was: {gameWord}.')
        playAgain()

main()
