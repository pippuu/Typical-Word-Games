# Import libraries
import random

# Functions
def choosingWord(words):
    return words[random.randint(0,4)]

def guessingTheWord(keyword):
    condition = False
    arrAns = ["_", "_", "_", "_", "_"]

    print("Word: " + arrAns[0] + arrAns[1] + arrAns[2] + arrAns[3] + arrAns[4])
    for i in range(5):
        char = input("Pick a word: ")
        for j in range(len(keyword)):
            if(char.lower() == keyword[j].lower()):
                arrAns[j] = char.lower()
        print("Word: " + arrAns[0] + arrAns[1] + arrAns[2] + arrAns[3] + arrAns[4])

    
    if(''.join(arrAns) == keyword.lower()):
        print("You found it!")
    else:
        print("Better luck next time!")


words = ['Laugh', 'Watch', 'Close', 'Agent', 'Arise']
keyword = choosingWord(words)
print(keyword)
guessingTheWord(keyword)