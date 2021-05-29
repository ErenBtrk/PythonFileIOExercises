'''
1. Write a Python program to read an entire text file.

'''

with open("deneme.txt","r") as file:
    list1 = file.readlines()

file.close()


print(list1)