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