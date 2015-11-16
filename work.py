
def fillVwords(filname, aDict):
    filename = "wordlist.txt"
    filehandle = open(filname, "r")
    for word in filehandle:
        word = word.strip()
        word = word.lower()
        







def main():
    
    quizwords = open("quizwords.txt", "r")

    for word in quizwords:
        word = quizwords.read()
        word = word.replace(",","")
        newword = word.split()
        newword.sort()
    print(newword)
    


#quizwords.close()