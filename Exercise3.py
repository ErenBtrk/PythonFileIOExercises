'''
3. Write a Python program to append text to a file and display the text.

'''

with open("exercise3.txt","a") as file:
    file.write("Hello World This is Yarasa Reis.")

file.close()

with open("exercise3.txt","r") as file:
    list1 = file.readlines()

print(list1)