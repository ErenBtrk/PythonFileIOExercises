'''
8. Write a python program to find the longest words.
'''

import re

with open("exercise8.txt","r") as file:
    list1 = file.readlines()

maxLength = 0
words = []

for item in list1:
    splittedLine = item.replace(".","").split()
    for word in splittedLine:
        words.append(word)
        if(len(word) >= maxLength):
            maxLength = len(word)


longestWords = []
for item in words:
    if(len(item) == maxLength):
        longestWords.append(item)

print(longestWords)
    
