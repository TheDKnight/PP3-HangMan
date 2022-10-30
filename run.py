import random 


def welcome() :
    name = input("Welcome to PP3 Hangman Game Please Enter Your Name Below :\n Name: ")
    while name.isalpha() == False :
        print("Please only enter alphabetic letters for your name") 
        name = input("Please enter your name again: ")
    else: 
        print(f"Welcome {name}, You will be playing against the computer today from a randomly selected word list.")


def randomWord():
    f = open('words.txt', 'r')
    word = random.choice(f.readlines()).strip()
    f.close()
    print(len(word))
    return(word)



#print(randomWord())
welcome()