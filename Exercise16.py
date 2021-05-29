'''
16. Write a Python program to assess if a file is closed or not.

'''

with open("exercise16.txt","r") as file:
    content = file.read()
    print(file.closed)

file.close()

print(file.closed)