from common import (randomize, clrSc, center, waitToContinue, wrapText)
class varStore:
    EP = list()
    EPT = [6, 4, 4, 6, 6, 6, 6, 4, 4, 1, 6, 8, 18, 10]
    for i in range(len(EPT)):
        if i == 0:
            EP.insert(i, EPT[i])
        else:
            EP.insert(i, EPT[i] + EP[i-1])
    MO = ["March", "May", "July", "September", "November", "January"]
    JL, C, W, M, FP, BSK = 300, 2, 30, 5, 5, 99 #Inital quantities of stuff


def initialize():
    pass

def scenario(varStore):
    center("The Journey of Marco Polo - 1271\n\n")
    print(wrapText(" Starting from Venice in 1271 you travel by sailing ship to the "
        "port of Armenia. Upon arrival, you prepare for a 6000-mile trek to "
        "the court of the Great Kublai Khan in Shang-tu, Cathay. Having set "
        "aside " + str(varStore.JL) + " precious jewels to finance your planned 3-year trip "
        ", you must barter for the following supplies in Armenia :"))
    print(wrapText("\n * Camels (Sturdier animals will cost more. You will probably "
        "want 8 to 10 camels to carry your many supplies.)"))
    print(wrapText("\n * Food (You must barter for food as you travel along. However, "
        "prices tend to be lower in port cities, so you should pack, in a good supply "
        "at the start."))
    print(wrapText("\n * Oil for lamps and cooking (Over much of the trip, you will be "
        "able to use wood to build fires. However, in the Persian, Lop, and Gobi deserts "
        "you will need oil."))
    print("\n"); waitToContinue(); clrSc()
    print(wrapText(" From Venice you have also packed clothing, weapons (crossbows), and "
        "medicines (balms and unguents); however, your provisions will be depleted as you "
        "go along and you must replenish them. The selection and price of supplies is quite "
        "different in various regions, so you must barter wisely. As a merchant, you are "
        "not skilled in fishing or hunting, although occasionally you might be able to try "
        "to get some food in this way."))
    print("\n"); waitToContinue(); clrSc

# Start Program
randomize()
clrSc()
center("The Journey of Marco Polo, 1271\n")
center("(c) David H. Ahl, 1986\n")
center("Ported to Python by Mark Rapp, 2020")
print('\n' * 2); waitToContinue()
clrSc()
varStore = varStore()
scenario(varStore)