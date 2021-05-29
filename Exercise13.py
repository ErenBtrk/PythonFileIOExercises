'''
13. Write a Python program to copy the contents of a file to another file .

'''


with open("exercise13.txt","r") as file:
    content = file.readlines()
file.close()

with open("copy.txt","w") as file:
    file.write(str(*content))
file.close()


