'''
5. Write a Python program to read a file line by line and store it into a list.

'''

with open("exercise5.txt","r") as file:
    list1 = file.readlines()
file.close()

for item in list1:
    print(item,end = '')