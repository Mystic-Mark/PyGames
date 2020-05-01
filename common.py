import os
import random
import textwrap
from datetime import datetime

def randomize():
    random.seed(datetime.now())

def clrSc():
    os.system('clear')

def center(text):
    width = os.get_terminal_size().columns
    print(text.center(width))

def waitToContinue():
    center("Press enter to continue")
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