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
        self.J = 0; self.DT = 0; self.D = 0; self.F = 0; self.L = 0; self.B = 0
        self.PSK = 0; self.PSKT = 0; self.PWD = 0; self.PWDT = 0; self.FE = 0
        self.PFD = 0; self.BA = 0
        
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
    
def chkStock(varStore):
    """
    Variables In: JL, C, B, BL
    Variables Out: JL, B, BL
    """
    def pushOn(number):
        print("You push on with your " + str(number) + " camels.")
    
    if varStore.JL < 16:
        print(wrapText("You have only " + str(varStore.JL) + " jewels with which to "
            "barter."))
        if varStore.B > 2:
            A = getYorN(input("\nWould you like to sell a camel? "))
            if A == "Y":
                RN = random.randint(8, 16)
                print(wrapText("You get " + str(RN) + " jewels for your best camel."))
                varStore.JL+=RN; varStore.B-=1; varStore.BL-=1
            else:
                pushOn(varStore.B)
                return
        else:
            pushOn(varStore.B)
            return
    if varStore.C < 1:
        print(wrapText("You should try to replace that tent you have been wearing as "
            "a robe. It is badly torn and the Tartars find it insulting."))
    return
    
def sickness(varStore):
    """
    Variables In: PSK, PSKT, PWD, PWDT, FE, PFD, J, JL, M, F
    Variables Out: PSK, PSKT, PWD, PWDT, PFD, J, M, F
    """
    #sickness total
    if varStore.PSK > 0:
        varStore.PSKT += varStore.PSK
        varStore.PSK = 0

    #injuries total
    if varStore.PWD > 0:
        varStore.PWDT += varStore.PWD
        varStore.PWD = 0
        
    if varStore.FE == 3:
        varStore.PFD += 0.4
    
    if varStore.PSKT + varStore.PWDT + varStore.PFD < 3:
        return
         
    #70% chance of delay due to recurring illness    
    if random.random() > 0.7:
        return
        
    print(wrapText("As a result of sickness, injuries, and poor eating, you must stop and regain your health. You trade a few jewels to stay in a hut."))
    RN = int(1+3.2*(random.random()))

    if RN > 3:
        #6% chance of dying
        time.sleep(2)
        print(wrapText("\nYou stay for " + str(RN) + " months but grow steadily weaker and finally pass away."))
        varStore.J += RN
        endGamePt2(varStore)
    else:
        print(wrapText("\nYou grow steadily stronger, but it is " + str(RN*2) + " months until you are again fit to travel."))
        varStore.PSKT = 0; varStore.PWDT = 0; varStore.PFD = 0
        varStore.J += RN; varStore.M = int(varStore.M/2); varStore.F = varStore.F / 2
        if varStore.F < 3:
            varStore.F = 3
        #costs money for lodging
        if varStore.JL > 20:
            varStore.JL -= 10
        else:
            varStore.JL = int(varStore.JL/2)
        printDate(varStore)
        return
    
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
    print("\n"); waitToContinue("Press enter to begin your trek!")
    clrSc()
    
def chkForZero(varStore):
    #Can't have negative jewels
    if varStore.JL < 0:
        varStore.JL = 0
    #No negative food
    if varStore.F < 0:
        varStore.F = 0
    #No negative oil
    if varStore.L < 0:
        varStore.L = 0
    #No negative clothing
    if varStore.C < 0:
        varStore.C = 0
    #No negative medicine
    if varStore.M < 0:
        varStore.M = 0
    #No negative arrows
    if varStore.W < 0:
        varStore.W = 0
        
def printInv(varStore):
    line1 = {'leadin': '                ', 'colspc': '  ', 'col3': 'SACKS OF', 'col4':
        'SKINS OF', 'col5': 'ROBES AND', 'col6': 'BALMS AND', 'col7': 'CROSSBOW'}
    line1Txt = "{l1[leadin]}{l1[col3]}{l1[colspc]}{l1[col4]}{l1[colspc]}{l1[col5]}"\
        "{l1[colspc]}{l1[col6]}{l1[colspc]}{l1[col7]}"
    print(line1Txt.format(l1=line1))
    
    line2 = {'colspc': '  ', 'col1': 'JEWELS', 'col2': 'CAMELS', 'col3': 'FOOD', 'col4':
        'OIL', 'col5': 'SANDALS', 'col6': 'UNGUENTS', 'col7': 'ARROWS'}
    line2Txt = "{l2[col1]}{l2[colspc]}{l2[col2]}{l2[colspc]}{l2[col3]:^8}{l2[colspc]}"\
        "{l2[col4]:^8}{l2[colspc]}{l2[col5]:^9}{l2[colspc]}{l2[col6]:^9}{l2[colspc]}"\
        "{l2[col7]:^8}"
    print(line2Txt.format(l2=line2))
    
    line3 = {'colspc': '  ', 'col1': varStore.JL, 'col2': varStore.B, 'col3': varStore.F, 'col4': varStore.L, 'col5': varStore.C, 'col6': varStore.M, 'col7': varStore.W}
    line3Txt ="{l3[col1]:^6d}{l3[colspc]}{l3[col2]:^6d}{l3[colspc]}{l3[col3]:^8.1f}"\
        "{l3[colspc]}{l3[col4]:^8.1f}{l3[colspc]}{l3[col5]:^9d}{l3[colspc]}{l3[col6]:^9d}"\
        "{l3[colspc]}{l3[col7]:^8d}"
    print(line3Txt.format(l3=line3))
    print()
    
def endGamePt1(varStore):
    """
    Variables In: J
    Variables Out: None
    """
    print(wrapText("You keep going as long as you can, trying to find berries and edible "
        "plants. But this is barren country and you fall ill and, after weeks of suffering, "
        "you collapse into eternal sleep."))
    endGamePt2(varStore)
    
def endGamePt2(varStore):
    """
    Variables In: J
    Variables Out: None
    """
    print()
    varStore.J+=1
    printDate(varStore)
    print("You had the following left at the end :\n")
    printInv(varStore)
    print("You traveled for " + str(varStore.J * 2) + " months!")
    print("\nSorry, you didn't make it to Shang-tu.")
    tryAgain()

def endTrip(varStore):
    chkForZero(varStore)
    time.sleep(1); clrSc()
    for i in range(5):
        print("\n\n\n\n\n"); center("CONGRATULATIONS !")
        time.sleep(0.5); clrSc()
        time.sleep(0.5)
    print(wrapText("You have been traveling for " + str(varStore.J * 2) + " months! "
        "You are ushered into the court of the Great Kublai Khan. He surveys your meager "
        "remaining supplies: ")); print()
    printInv(varStore)
    print(wrapText("\n...and marvels that you got here at all. He is disappointed that the "
        "Pope did not see fit to send the 100 men of learning that he requested and, as a "
        "result, keeps the three of you as his personal envoys for the next 21 years. Well "
        "done!"))
    print()

def tryAgain():
    A = getYorN(input("\nWould you like to try again? "))
    if A == "Y":
        varStore.reset()
        main()
    else:
        print("\nBye for now.")
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
        varStore.J+=1; printDate(varStore)
        varStore.DT+=varStore.D
        
        #Reached end of trip
        if varStore.DT > 6000:
            endTrip(varStore)
        
        varStore.D = 40 + varStore.BA * 20 + int(random.randrange(99))
        print("You have traveled " + str(varStore.DT) + " miles.")
        print("Here is what you now have: "); printInv(varStore)
        
        #Debug
        #What about negative jewels????
        print("\n"); waitToContinue("continue")
        
        chkStock(varStore)
        sickness(varStore)
        
        endTrip(varStore)
        tryAgain()

if __name__ == '__main__':
    varStore = varStore()
    main()
