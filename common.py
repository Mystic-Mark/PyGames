import os
import random
from datetime import datetime

def randomize():
    random.seed(datetime.now())

def cls():
    os.system('clear')

def center(text):
    width = os.get_terminal_size().columns
    print(text.center(width))

def waitToContinue():
    center("Press enter to continue.")
    input()
