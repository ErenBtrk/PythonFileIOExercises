'''
21. Write a Python program to create a file where all letters of
English alphabet are listed by specified number of letters on each line.
 
'''

numOfLetters = int(input("Please enter number of letters on each line : "))


with open("exercise21.txt","w") as file:
    i = 0
    for index in range(26):
        file.write(chr(index+65))
        i += 1
        if(i == numOfLetters):
            file.write("\n")
            i = 0

