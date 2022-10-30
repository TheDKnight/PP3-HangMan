# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random 

f = open('words.txt', 'r')
lines = random.choice(f.readlines() )
f.close()
print(lines)
