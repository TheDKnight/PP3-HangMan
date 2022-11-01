import random 


def welcome() :
    """
    Welcome functions Takes the users name and checks it again the is alphabetic built in function of python
    It will not progress unless the correct input is inputed.
    """

    name = input("Welcome to PP3 Hangman Game Please Enter Your Name Below :\n Name: ")
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
    #print(len(word))
    
    return(word)

def playAgain():
    play = input("\nGame is finished, would you like to play another game?\n\npress y for another game or n to exit \n").lower()
        
    if len(play) != 1 or not play.isalpha():
        print("Please enter either a y or ")
    elif play == "y" :
        main()
    elif play == "n": 
        exit()
    return(playAgain())
def main():
   # welcome()
    gameWord = randomWord()
    lenGameWord = len(gameWord) 
    #print(gameWord)
    print(f"\nThe word is {lenGameWord} Characters Long")
    guessed_letters = []
    
    blanks = len(gameWord) * '_'
    blanks = list(blanks)
    
    
    lives = 5
    while lives > 0:
        guess = input("Enter A Letter \n").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a correct value")
           # guess = input("Enter A Letter \n".lower()) 
        elif guess in guessed_letters:
            print("Letter has been guessed allready")
            #guess = input("Enter A Letter \n".lower()) 
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
           print(F"{guess} is in the word")
           print(''.join(blanks))
           
        print(f"Letters Guessed Allready {guessed_letters}")

        if ''.join(blanks) == gameWord:
            print(f'You won. The secret word was: {gameWord}.')
            playAgain()
        
    else:
        print("")
        print(f'you lose \n The secret word was: {gameWord}.')
        playAgain()

main()
#print(randomWord())
#print(len(randomWord()))
#welcome()