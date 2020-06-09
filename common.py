import os
import random
import textwrap
from datetime import datetime, timedelta
import time

def randomize():
    random.seed(datetime.now())

def clrSc():
    os.system('clear')

def center(text):
    #width = os.get_terminal_size().columns
    width = 70
    print(text.center(width))

def waitToContinue(text):
    if text == "continue":
        center("Press enter to continue")
    else:
        center(text)
    input()

def wrapText(value):
    wrapper = textwrap.TextWrapper(width=70,break_long_words=False,replace_whitespace=False)
    return wrapper.fill(text=value)
    
def getYorN(answer):
    while True:
        answer = get1stLtrAns(answer)
        if answer != "Y" and answer != "N":
            answer = input("Don't understand answer. Enter 'Y' or 'N' please: ")
            answer = get1stLtrAns(answer)
        else:
            return answer
    
def get1stLtrAns(answer):
    if answer == "":
       return "Y"
    else:
       answer = answer[0]
       
    if answer >= "A" and answer <= "Z":
       return answer
    elif answer >= "a" and answer <= "z":
       return answer.upper()
    else:
       return "0"

def getIntAns(question):
    while True:
        getAns = input(question)
        try:
            return int(getAns)
            break
        except:
            print("Incorrect input, try again.")

def dictToObjectStore(object, dictList):
    for key, value in dictList.items():
        setattr(object, key, value)
        
def onCase(onCaseList, indexNum):
    func = onCaseList.get(indexNum, "notInList")
    return func
       
def end():
    exit()