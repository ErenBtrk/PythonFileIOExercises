'''
12. Write a Python program to write a list to a file.

'''

list1 = [9,8,7,6,5,4,3,2,1,0]

with open("exercise12.txt","w") as file:
    for num in list1:
        file.write(str(num)+'\n')

file.close()

