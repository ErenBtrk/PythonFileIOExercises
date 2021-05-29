'''
2. Write a Python program to read first n lines of a file.

'''

with open("exercise2.txt","r") as file:
    for index in range(3):
        print(file.readline(),end="")


