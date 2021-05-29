'''
10. Write a Python program to count the frequency of words in a file.

'''

freqList = {}

with open("exercise10.txt","r") as file:
    for line in file:
        splittedLine = line.replace("."," ").split()
        for word in splittedLine:
            if(word in freqList):
                freqList[word] += 1
            else:
                freqList[word] = 1
    

print(freqList)