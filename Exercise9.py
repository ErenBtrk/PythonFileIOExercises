'''
9. Write a Python program to count the number of lines in a text file.
'''

with open("exercise9.txt","r") as file:
    lineCount = 0
    while file.readline():
        lineCount += 1
file.close()

print(lineCount)
