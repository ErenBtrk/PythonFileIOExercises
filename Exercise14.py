'''
14. Write a Python program to combine each line from first file
with the corresponding line in second file.

'''

with open("exercise14-1.txt","r") as file1,open("exercise14-2.txt","r") as file2:
    for line1,line2 in zip(file1,file2):
        line1 = line1.replace("\n","")
        print(f"{line1} - {line2}",end = "")
            
file1.close()
file2.close()