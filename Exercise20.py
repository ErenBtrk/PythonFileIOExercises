'''
20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

'''

for index in range(26):
    open(chr(index+65)+'.txt',"x")


########################################################################################

# import string, os
# if not os.path.exists("letters"):
#    os.makedirs("letters")
# for letter in string.ascii_uppercase:
#    with open(letter + ".txt", "w") as f:
#        f.writelines(letter)