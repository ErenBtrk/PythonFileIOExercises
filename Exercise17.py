'''
17. Write a Python program to remove newline characters from a file.

'''

newContent = []

with open("exercise17.txt","r+") as file:
    content = file.readlines()
    for line in content:
        line = line.replace("\n","")
        newContent.append(line)

print(newContent)




