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
        self.J = 0
        
        # Future Variables for Store
        #self.HX = 1 # VARIABLE STUB
        #self.J = 1 # VARIABLE STUB
        #self.A, self.A1, self.A2 = 2, 1, 3 # VARIABLE STUB
        
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
    print('\n' * 2); waitToContinue("continue")
    clrSc()

def scenario():
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
    print("\n"); waitToContinue("continue")
    print(wrapText(" From Venice you have also packed clothing, weapons (crossbows), and "
        "medicines (balms and unguents); however, your provisions will be depleted as you "
        "go along and you must replenish them. The selection and price of supplies is quite "
        "different in various regions, so you must barter wisely. As a merchant, you are "
        "not skilled in fishing or hunting, although occasionally you might be able to try "
        "to get some food in this way."))
    print("\n"); waitToContinue("continue")

def getInitSupplies():
    """
    Variables In: JL
    Variables Out: A, A1, A2, B, BA, BL, JL, L
    """
    #Camels - number, cost, amount they can carry
    varStore.A1 = 17; varStore.A2 = 24
    print(wrapText(" After three months at sea, you have arrived at the seaport "
        "of Laiassus, Armenia. There are many merchants in the port city and you can easily "
        "get the supplies you need. Several traders offer you camels at prices between " + 
        str(varStore.A1) + " and " + str(varStore.A2) + " jewels each."))
    varStore.A = getIntAns("How much do you want to pay for a camel? ")
    checkAnswerRange()
    varStore.BA = varStore.A
    print("\n");print(wrapText("You will need at least 7 camels, but not more than 12."))
    varStore.A1 = 7; varStore.A2 = 12
    varStore.A = getIntAns("How many camels do you want to buy? ")
    checkAnswerRange()
    varStore.B = varStore.A
    varStore.JL = varStore.JL - varStore.BA * varStore.B
    varStore.A2 = 3 * varStore.B - varStore.A
    #Oil - Amount and Cost
    print("\n");print(wrapText("A skin of oil costs 2 jewels each. You should have at least "
        "6 full skins for cooking in the desert. Your camels can carry " + str(varStore.A2) + 
        " skins."))
    varStore.A1 = 5
    varStore.A = getIntAns("How many do you want? ")
    checkAnswerRange()
    varStore.BL = varStore.B
    varStore.L = varStore.A
    varStore.JL = varStore.JL - 2 * varStore.L
    
def initHuntSkill():
    """
    Variables In: None
    Variables Out: HX
    """
    print("\n"); print(wrapText("Before you begin your journey, please rank your skill "
        "with the crossbow on the following scale:"))
    print(" (1) Can hit a charging boar at 300 paces")
    print(" (2) Can hit a deer at 50 paces")
    print(" (3) Can hit a sleeping woodchuck at 5 paces")
    print(" (4) Occasionally hit your own foot when loading")
    while True:
       varStore.HX = getIntAns("How do you rank yourself? ")
       if varStore.HX  > 0 and varStore.HX < 5:
           break
       else:
           print("Please enter 1, 2, 3 or 4")
    print("\n"); waitToContinue("Press any key to begin your trek!")
    clrSc()

def tryAgain():
    A = getYorN(input("\nWould you like to try again? "))
    if A == "Y":
        varStore.reset()
        main()
    else:
        print("\nBye for now.")
        end()

def printDate():
    """
    Variables In: J, MO_s
    Variables Out: None
    """
    MO = varStore.J
    while MO > 6:
        MO = MO - 6
    YR = 1271 + int(varStore.J/6)
    print("\nDate: " + varStore.MO_s[MO-1] + " " + str(YR))
    
def shootCrossbow():
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

def checkAnswerRange():
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
        varStore.A = getIntAns("Your answer please? ")

def main():
    randomize()
    title()
    scenario()
    getInitSupplies()
    initHuntSkill()
    
    while True:
        varStore.J+=1; printDate()
        tryAgain()

if __name__ == '__main__':
    varStore = varStore()
    main()
