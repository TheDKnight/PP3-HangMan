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


def randomWord():
    """
    The randomWord functions opens the words.txt file and takes a random word from the list using the import random function.
    It also strips the word of any whtie space.
    """
    f = open('words.txt', 'r')
    word = random.choice(f.readlines()).strip()
    f.close()
    print(len(word))
    return(word)



#print(randomWord())
welcome()