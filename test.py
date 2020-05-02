from common import *

class varStore:
    def __init__(self):
        self.EP = list()
        self.EPT = [6, 4, 4, 6, 6, 6, 6, 4, 4, 1, 6, 8, 18, 10]
        self.MO_s = ["March", "May", "July", "September", "November", "January"]
        self.JL, self.C, self.W, self.M, self.FP, self.BSK = \
            300, 2, 30, 5, 5, 99 #Inital quantities of stuff
        self.SW_s = ["SPLAT","SPRONG","TWACK","ZUNK"] #Shooting words
        self.FA_s = ["wild boar","big stag","black bear"] #Hunting animals
        
        # Future Variables for Store
        self.HX = 1 # VARIABLE STUB
        self.J = 1 # VARIABLE STUB
        self.A, self.A1, self.A2 = 2, 1, 3 # VARIABLE STUB
        
        self.setupEP()
    
    def reset(self):
        self.__init__()
    
    def setupEP(self):
        for i in range(len(self.EPT)):
            if i == 0:
                self.EP.insert(i, self.EPT[i])
            else:
                self.EP.insert(i, self.EPT[i] + self.EP[i-1])

def title():
    clrSc()
    center("The Journey of Marco Polo, 1271\n")
    center("(c) David H. Ahl, 1986\n")
    center("Ported to Python by Mark Rapp, 2020")
    print('\n' * 2); waitToContinue()
    clrSc()

def scenario(varStore):
    """
    Variables In: JL
    Variables Out: None
    """
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
    print("\n"); waitToContinue()
    print(wrapText(" From Venice you have also packed clothing, weapons (crossbows), and "
        "medicines (balms and unguents); however, your provisions will be depleted as you "
        "go along and you must replenish them. The selection and price of supplies is quite "
        "different in various regions, so you must barter wisely. As a merchant, you are "
        "not skilled in fishing or hunting, although occasionally you might be able to try "
        "to get some food in this way."))
    print("\n"); waitToContinue()

def getInitSupplies(varStore):
    """
    Variables In: None
    Variables Out: A1, A2
    """
    varStore.A1 = 17; varStore.A2 = 24
    print("\n");print(wrapText(" After three months at sea, you have arrived at the seaport "
        "of Laiassus, Armenia. There are many merchants in the port city and you can easily "
        "get the supplies you need. Several traders offer you: "))
    print("\n camels at prices between " + str(varStore.A1) + " and " + str(varStore.A2) + " jewels each.")

def tryAgain():
    A = getYorN(input("\nWould you like to try again? "))
    if A == "Y":
        varStore.reset()
        main()
    else:
        print("Bye for now.")
        end()

def printDate(varStore):
    """
    Variables In: J, MO_s
    Variables Out: None
    """
    MO = varStore.J
    while MO > 6:
        MO = MO - 6
    YR = 1271 + int(varStore.J/6)
    print("\nDate: " + varStore.MO_s[MO-1] + " " + str(YR))
    
def shootCrossbow(varStore):
    """
    Variables In: SW_s, HX
    Variables Out: SR
    """
    RN = random.randint(1, 4)
    S = varStore.SW_s[RN-1]
    FMT = '%H:%M:%S'
    S1 = datetime.now().time().strftime("%H:%M:%S")
    while True:
        X = input("Type this word: " + S + " >> ")
        if X.upper() == S:
            break
        else:
            print("That's not it. Try again.")
    S2 = datetime.now().time().strftime("%H:%M:%S")
    tdelta = datetime.strptime(S2, FMT) - datetime.strptime(S1, FMT)
    getSec = int(tdelta.total_seconds())
    if getSec < 0:
        getSec = getSec + 86401
    varStore.SR = getSec - varStore.HX #shooting response

def checkAnswerRange(varStore):
    """
    Variables In: A, A1, A2
    Variables Out: A
    """
    while True:
        if varStore.A >= varStore.A1 and varStore.A <= varStore.A2:
            return
        elif varStore.A < varStore.A1:
            X = "few"
        else:
            X = "many"
        print("That is too " + X + ". ", end="")    
        while True:
            getAns = input("Your answer please? ")
            try:
                varStore.A = int(getAns)
                break
            except:
                print("Incorrect input, try again.")

def main():
    randomize()
    title()
    scenario(varStore)
    getInitSupplies(varStore)
    
    while True:
        tryAgain()

if __name__ == '__main__':
    varStore = varStore()
    main()



