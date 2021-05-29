'''
15. Write a Python program to read a random line from a file.
'''

import random

with open("exercise15.txt","r") as file:
    list1 = file.readlines()
file.close()

random_line = random.choice(list1).replace("\n","")

print(random_line)
    