'''
18. Write a Python program that takes a text file as input and returns
the number of words of a given text file.
Note: Some words can be separated by a comma with no space.

'''

import re

def numOfWords(fileName):
    with open(fileName+".txt","r") as file:
        content = re.split(" |\n",file.read())
        print(content)
    return len(content)

textFileName = input("Please enter file name : ")

print(f"number of words = {numOfWords(textFileName)}")