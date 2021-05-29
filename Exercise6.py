'''
6. Write a Python program to read a file line by line store it into a variable.

'''

with open("exercise6.txt","r") as file:
    list1 = file.readlines()

print(list1)