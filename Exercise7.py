'''
7. Write a Python program to read a file line by line store it into an array.

'''

with open("exercise7.txt","r") as file:
    list1 = []
    for line in file:
        list1.append(line)

print(list1) 