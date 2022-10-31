import random 


def welcome() :
    """
    Welcome functions Takes the users name and checks it again the is alphabetic built in function of python
    It will not progress unless the correct input is inputed.
    """

    name = input("Welcome to PP3 Hangman Game Please Enter Your Name Below :\n Name: ")
    while name.isalpha() == False :
        print("Please only enter alphabetic letters for your name") 
        name = input("Please enter your name again: ")
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


def main():
    welcome()
    gameWord = randomWord()
    lenGameWord = len(gameWord) 
    print(gameWord)
    print(f"The word is {lenGameWord} Characters Long")
    guessed_letters = []
    print(f"You have guessed {guessed_letters} Letters Allready")
    blanks = len(gameWord) * '_'
    print(blanks)
    guess = input("Enter A Letter \n".lower()) 
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a correct value")
    elif guess in guessed_letters:
        print("Letter has been guessed allready")
    elif guess in gameWord :
        print("in game world")

main()
#print(randomWord())
#print(len(randomWord()))
#welcome()