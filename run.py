# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random 

def randomWord():
    f = open('words.txt', 'r')
    word = random.choice(f.readlines()).strip()
    f.close()
    print(len(word))
    return(word)
print(randomWord())
