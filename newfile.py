#Alicia Williams
#Partner's Name...
#CIS-125 FA 15
#Week 9 Assignment
#newfile.py

import string

#This puts letters of the word in alphabetical order
def sortLetters(word):
    word = word.lower()
    listWord = list(word)
    listWord.sort()
    sortLetters = ''.join(listWord)
    return sortLetters

#pulls up dictionary and letters only starting with v
def createDictionary(fileName, dictionary): #fileName is placeholder for wordList.txt
    fileHandle = open(fileName, 'r')
    for line in fileHandle:
        line = line.strip()
        line = line.strip(string.punctuation)
        word = line.lower()
        if word[0] == 'v':
            sortedWord = sortLetters(word)
            dictionary[sortedWord] = word
    fileHandle.close()

#opens quizwords and finds its anagram
def findAnagrams(fileName, dictionary):
    fileHandle = open(fileName, 'r')
    for line in fileHandle:
        line = line.strip()
        line = line.strip(string.punctuation)
        quizword = line.lower()
        print(quizword, dictionary[sortLetters(quizword)])
    fileHandle.close()

#main function that calls the functions
def main():
    aDict = {}
    filename = 'wordList.txt'
    quizListName = 'quizwords.txt'
    createDictionary(filename, aDict)
    findAnagrams(quizListName, aDict)
    

main()