from pprint import pprint
import os

class varStore:
    pass

dict1 = {"CZ": 0}
dict2 = {"PWD": 1.5, "CZ": 1}

def dictToObjectStore(object, dictList):
    for key, value in dictList.items():
        setattr(object, key, value)

varStore = varStore()

os.system('clear')

dictToObjectStore(varStore, dict1)
print("Contents of varStore onject after loading Dictionary 1:")
print("CZ from dictionary 1 is: " + str(varStore.CZ))
print("DEBUG: ", end=""); pprint(vars(varStore))

dictToObjectStore(varStore, dict2)
print("\nContents of varStore onject after loading Dictionary 2:")
print("CZ from dictionary 2 is: " + str(varStore.CZ))
print("DEBUG: ", end=""); pprint(vars(varStore))

print("\nTesting text string concat:")
text = "This is part1 of the string "
text = text + "and this is part2."
print(text)