# Hangman Game

* Hangman is a python terminal game, which runs in the Code Inistitue mock terminal on Heroku
* The hangman game is a game where you get a random word and you need to answer correct letters in the word.
* If you guess a wrong answer you lose a life, you lose when you run out of lives.

Here is the live version of my site 

https://pp3-handy-man.herokuapp.com/

<img src = "/assets/readme.images/head.jpg">

# How to play
- The user starts by entering there name into the program.
- They are playing against the computer who selects a random word out of the list.
- They user has 6 lives to guess what the word is by selecting letters of the alphabet.
- When the user gets a correct guess the position the guess character was in the word is shown
- The user wins if they guess the word within 6 correct tries.

# Features

<img src = "/assets/readme.images/play1.jpg">

- The game loads with a welcome message 
- The user is asked to enter there name.

<img src = "/assets/readme.images/play2.jpg">

- Once the user enters there name it is displayed.
- It also lets the user know they are playing against a computer who will select a random word form a word list.
- The user is told how many characters the word is.
- They are asked to enter the first letter
<img src = "/assets/readme.images/play3.jpg">

- If the letter is not in the word a this is displayed to the user.
- The user is also notifed how many lives they have left.

<img src = "/assets/readme.images/play4.jpg">

- When the user guesses a correct letter from the word it is displayed on the screen.
- The blank word is now updated with the correct letter and the letter is put into the place of the blanks
- The user is also shown a list of words they have allready guessed

<img src = "/assets/readme.images/play5.jpg">

- If the game is lost to the computer, it will be displayed.
- You will see what the word selected was.
- You will also be asked if you would like to play another game.

<img src = "/assets/readme.images/play6.jpg">

- If the user  is successfull they are adivsed of the win.
- They are also asked if they would like to play another game.

## Future Features 

- A scoreboard could be added to the game so the user can keep track of the wins.
- A grapic interface could be added so you could see the "hang" in real time with the added parts everytime the user misses a guess.

# Data Model

I decided to use some functions to generate the input needed.
The welcome functions takes in the users name while outputting a welcome message 

The inbuilt isalpha function allows only alphabetic charectors to be entered.

The randomWord function takes a random word for a saved txt file.
The file is opened and the import random function takes a random line from the text and returns this value.

The playAgain functions is run when the user wins or loses and asks the user would they like to play another game or exit the program.


The main function is where the game is run.
It takes the value from the welcome function and the randomWord and assigns them. 
This function runs through a while loop while the user still has lives remaining,All input is run through the isAlpha functon for validation.



# Testing
## Manual Testing

<img src = "/assets/readme.images/error1.jpg">
<img src = "/assets/readme.images/error2.jpg">

For the inputs for the program i used the built in function isAlpha to validate the input. I tested this was working by inputing other characters beside the alpabetic ones. The function caught the wrong input as expected.

For the input of the single character i set it so if the user entered more than one character it would advise them they would need to enter the correct input value.

## Validation 
As the PEP8 website is offline, i installed the local version into gitpod which automatically returns any errors in the IDE.
There were no linter errors found.

# Bugs 
The main bug i had with the code was when i was making the while loop i left the input out side of the loop so i had duplicate inputs for each of the cases. I spotted this bug and fixed when i moved the input into the loop.

# Deployment 
This project was deployed using Code Institute's terminal for Heroku.

- Steps for deployment 
- Fork or clone this repo. 
- Create a new Heroku app.
- Set the buildbacks to Pyython and NodeJs in that order.
- Set the var and port to 8000 
- Link the Heroku app to the repo
- Deploy App 

# Credits
- I used the python essential project for some understanding of home python worked 
- I took the blanks function from this stack exchange https://codereview.stackexchange.com/questions/272893/hangman-game-in-python-with-nine-possible-words. 