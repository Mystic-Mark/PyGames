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
        self.PFD = 0; self.BA = 0; self.BL = 0; self.CZ = 0; self.HX = 1
        self.DZ = -1; self.FQ = 0; self.SR = 0
        
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
    print("\n"); waitToContinue("continue")
    print(wrapText(" From Venice you have also packed clothing, weapons (crossbows), and "
        "medicines (balms and unguents); however, your provisions will be depleted as you "
        "go along and you must replenish them. The selection and price of supplies is quite "
        "different in various regions, so you must barter wisely. As a merchant, you are "
        "not skilled in fishing or hunting, although occasionally you might be able to try "
        "to get some food in this way."))
    print("\n"); waitToContinue("continue")

def getInitSupplies(varStore):
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
    checkAnswerRange(varStore)
    varStore.BA = varStore.A
    print("\n");print(wrapText("You will need at least 7 camels, but not more than 12."))
    varStore.A1 = 7; varStore.A2 = 12
    varStore.A = getIntAns("How many camels do you want to buy? ")
    checkAnswerRange(varStore)
    varStore.B = varStore.A
    varStore.JL = varStore.JL - varStore.BA * varStore.B
    varStore.A2 = 3 * varStore.B - 6
    #Food & Cost, amount of oil camels can carry
    print(wrapText(" One large sack of food costs 2 jewels. You will need at least 8 sacks "
        "to get to Babylon (Baghdad); you can carry a maximum of " + str(varStore.A2) + \
        " sacks."))
    varStore.A = getIntAns("How many do you want? ")
    checkAnswerRange(varStore)
    varStore.F = varStore.A
    varStore.JL = varStore.JL - varStore.A * 2
    varStore.A2 = 3 * varStore.B - varStore.A
    #Oil - Amount and Cost
    print("\n");print(wrapText("A skin of oil costs 2 jewels each. You should have at least "
        "6 full skins for cooking in the desert. Your camels can carry " + str(varStore.A2) + 
        " skins."))
    varStore.A1 = 5
    varStore.A = getIntAns("How many do you want? ")
    checkAnswerRange(varStore)
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
        
def barterSupplies(varStore):
    """
    Variables In: JL, A
    Variables Out: A1, A2, B, BL, BA, JL
    """
    print("You have " + str(varStore.JL) + " jewels.")
    A_s = getYorN(input("\nDo you want to barter here? "))
    
    if A_s == "Y":
        RN = int(17 + 8 * random.random())
        print("Camels cost " + str(RN) + " jewels here.")
        varStore.A1 = 0; varStore.A2 = int(varStore.JL / RN)
        varStore.A = getIntAns("How many do you want? ")
        checkAnswerRange(varStore)
        #Lower Quality Animals along route
        varStore.B += varStore.A
        varStore.BL += varStore.A
        varStore.BA -= varStore.A
        varStore.JL = varStore.JL - varStore.A * RN
        RN = int(2 + 4 * random.random())
        print("Sacks of food cost " + str(RN) + " jewels.")
        
        while True:
            varStore.A2 = int(varStore.JL / RN)
            varStore.A = getIntAns("How many do you want? ")
            checkAnswerRange(varStore)
            varStore.F += varStore.A
            if varStore.F + varStore.L > 3 * varStore.BL:
                print("Camels can't carry that much.")
                varStore.F -= varStore.A
            else:
                break
        
        varStore.JL = varStore.JL - varStore.A * RN
        RN = int(2 + 4 * random.random())
        print("Skins of oil cost " + str(RN) + " jewels.")
        
        while True:
            varStore.A2 = int(varStore.JL / RN)
            varStore.A = getIntAns("How many do you want? ")
            checkAnswerRange(varStore)
            varStore.L += varStore.A
            if varStore.F + varStore.L > 3 * varStore.BL:
                print("Camels can't carry that much.")
                varStore.L -= varStore.A
            else:
                break
                
        varStore.JL = varStore.JL - varStore.A * RN
        RN = int(8 + 8 * random.random())
        print("A set of clothes costs " + str(RN) + " jewels.")  
        varStore.A2 = int(varStore.JL / RN)
        varStore.A = getIntAns("How many do you want? ")
        checkAnswerRange(varStore)
        varStore.C += varStore.A
        varStore.JL = varStore.JL - varStore.A * RN
        print("You can get a bottle of balm for 2 jewels. ")  
        varStore.A2 = int(varStore.JL / 2)
        varStore.A = getIntAns("How many do you want? ")
        checkAnswerRange(varStore)
        varStore.JL = varStore.JL - 2 * varStore.A
        varStore.M += varStore.A
        varStore.A2 = varStore.JL
        RN = int(6 + 6 * random.random())
        print("You can get " + str(RN) + " arrows for 1 jewel.")  
        varStore.A = getIntAns("How many jewels do you want to spend on arrows? ")
        checkAnswerRange(varStore)
        varStore.JL -= varStore.A
        varStore.W = varStore.W + RN * varStore.A
        
        if varStore.C > 1:
            varStore.CZ = 0            
    
    print("\nHere is what you now have:")
    printInv(varStore)
    return
    
def noClothes(varStore):
    print(); print(wrapText("You were warned about getting more modest clothes. "
        "Furthermore, your sandals are in shreds.")); print()
    if varStore.CZ == 1:
        text = "Word has been received about your disreputable appearance. The people " \
        "are not willing to deal with you and they stone you. You are badly wounded and " \
        "vow to get new clothes as soon as possible."
        clothesDict = {"PWD": 1.5, "CZ": 1}
    else:
        text = "The Tartars chase you from town and "
        if random.random() > 0.2:
            text = text + "warn you not to return."
            clothesDict = {"CZ": 1}
        else:
            text = text + "stone you. You are badly wounded and vow to get new clothes " \
                "as soon as possible."
            clothesDict = {"PWD": 1.5, "CZ": 1}
    print(wrapText(text))
    dictToObjectStore(varStore, clothesDict)

def eatFood(varStore):
    def eatHowMuch():
        text = " (1) Reasonably well (can walk further; Less chance of sickness)"
        print("On the next stage of your journey, how do you want to eat :")
        while True:
            print(text)
            A = getIntAns(" (2) Adequately, or (3) Poorly? ")
            if A  > 0 and A < 4:
                return A
            else:
                text = "That's not a choice. Now then... \n (1) Eat Well,"

    if varStore.F < 3:
        outOfFood(varStore)
    while True:
        A  =  eatHowMuch()
        varStore.FE = 6 - A
        if varStore.FE <= varStore.F:
            varStore.FR = int(0.5 + 10 * (varStore.F - varStore.FE)) / 10
            if varStore.FR > 3:
                break
            if varStore.FR == 1:
                X_s = "."
            else:
                X_s = "s."
            print("Your food reserve will then be just " + str(varStore.FR) + " sack" + X_s)
            if A == 3:
                break
            A_s = getYorN(input("Do you want to change your mind about how much you will "\
                "eat? "))
            if A_s == "N":
                break
        else:
            print("You don't have enough food to eat that well. Try again.")
    varStore.F -= varStore.FE
    varStore.D = varStore.D - (A - 1) * 50
    varStore.FQ = varStore.FP + varStore.FE
    varStore.FP = varStore.FE
    
def outOfFood(varStore):
    print("You don't have enough food to go on.")
    if varStore.JL > 14:
        RN = int(5 + 4 * random.random())
        varStore.A1 = 1; varStore.A2 = int(varStore.JL / RN)
        print(wrapText("You should have bought food at the market. Now it will cost you " \
            + str(RN) + " jewels per sack."))
        varStore.A = getIntAns("How many sacks do you want? ")
        checkAnswerRange(varStore)
        varStore.F += varStore.A
        varStore.JL = varStore.JL - varStore.A * RN
        if varStore.F >= 3:
            return
        print(wrapText("You still don't have enough food and there is nothing to hunt."))
    if varStore.B > 0:
        A_s = getYorN(input("\nDo you want to eat a camel? "))
        if A_s == "N":
            endGamePt1(varStore)
        else:
            varStore.B -= 1
            RN = int(3 + 2 * random.random())
            varStore.F += RN
        text = "You manage to get about " + str(RN) + " sacks of food out of it."
        print(wrapText(text))
        return
    print("You don't even have a camel left to eat.")
    endGamePt1(varStore)
    
def desertSections(varStore):
    """
    Variables In: DT, L
    Variables Out: DZ, L, PSK, D, M
    """
    varStore.DZ = 0
    # No deserts at far ends
    if varStore.DT < 2100 or varStore.DT > 5900:
        return
    # Tigris River Valley
    if varStore.DT > 2600 and varStore.DT < 4100:
        return
    # No desert in the middle
    if varStore.DT < 4100:
        X_s = "Dasht-e-Kavir (Persian)"
    elif varStore.DT > 5399:
        X_s = "Gobi (Cathay)"
    else:
        X_s = "Taklimakan (Lop)"
    print(wrapText("You are in the " + X_s + " desert."))
    
    if varStore.L < 3:
        print("You ran out of oil for cooking.")
        if varStore.L > 1 and random.random() > 0.5:
            varStore.L = 0
        else:
            print(wrapText("You get horribly sick from eating raw and undercooked food."))
            varStore.L = 0
            varStore.PSK = 1
            varStore.D -= 80
            varStore.M -= 1
    else:
        varStore.L -= 3
        print("Use 3 skins of oil for cooking.")

    onCaseList = {
            1: specialCamelSick,
            2: scenario2310,
            3: scenario2420,
            4: scenario2450,
            5: scenario2480,
            6: scenario2510
        }
    
    indexNum = random.randint(1, 7)
    
    response = onCase(onCaseList, indexNum)
    if response == "notInList":
        print("You get through this stretch of desert without mishap!")
    else:
        response(varStore)
    
    varStore.DZ = 1
    chkForZero(varStore)
    
def specialEvents(varStore):
    RN = int(sum(varStore.EPT) * random.random())
    i = 1
    while RN > varStore.EP[i-1]:
        i += 1
    
    onCaseList = {
            1: specialCamelInjury,
            2: specialCamelSick,
            3: scenario2310,
            4: scenario2340,
            5: scenario2360,
            6: scenario2380,
            7: scenario2400,
            8: scenario2420,
            9: scenario2450,
            10: scenario2480,
            11: scenario2540,
            12: scenario2570,
            13: scenario2600,
            14: scenario2660
        }

    indexNum = i
    response = onCase(onCaseList, indexNum)
    response(varStore)

def specialCamelSick(varStore):
    print(wrapText("One of your camels is very sick and can't carry a full load."))
    while True:
        A = getIntAns("Want to (1) Keep it with you, (2) Slaughter it, or (3) Sell it: ")
        if A == 1:
            varStore.BSK = varStore.J + 2
            checkCarryCapacity(varStore)
            break
        elif A == 2:
            specialCamelKill(varStore)
            break
        elif A == 3:
            specialCamelSell(varStore)
            break
        else:
            print("That is not a choice. Again, please.")

def specialCamelInjury(varStore):
    text = "A camel injures its leg. Do you want to (1) Nurse it along or"
    while True:
        print(wrapText(text))
        A = getIntAns("(2) Abandon it, or (3) Sell it: ")
        if A == 1:
            varStore.BSK = varStore.J + 2
            checkCarryCapacity(varStore)
            break
        elif A == 2:
            specialCamelKill(varStore)
            break
        elif A == 3:
            specialCamelSell(varStore)
            break
        else:
            text = "That is not a choice. Answer (1) Nurse it along or"
    
def specialCamelKill(varStore):
    varStore.B -= 1
    checkCarryCapacity(varStore)
    varStore.FC = 3 * varStore.BL - varStore.F - varStore.L
    if varStore.FC <= 0:
        return
    else:
        print("You kill the camel for food.")
    if varStore.FC > 2:
        varStore.FC = 3
    varStore.F += varStore.FC
    if varStore.FC == 1:
        X_s = ""
    else:
        X_s = "s"
    print(wrapText("You get the equivalent of " + str(varStore.FC) + " sack" + X_s + " of "
        "food."))

def specialCamelSell(varStore):
    varStore.B -= 1
    print(wrapText("It is a poor beast and you can get only 10 jewels for it."))
    varStore.JL += 10
    checkCarryCapacity(varStore)
    
def checkCarryCapacity(varStore):
    varStore.BL = varStore.B
    if varStore.BSK <= varStore.J:
        # if sick camel reduce load, speed
        varStore.BL = varStore.B - 0.6
        varStore.BA -= 1
    if varStore.F + varStore.L <= 3 * varStore.BL:
        return
    print("You have too large a load for your camels. ")
    varStore.FC = int(varStore.F + varStore.L - 3 * varStore.BL + 0.9)
    if varStore.FC == 1:
        X_s = ""
    else:
        X_s = "s"
    print("You'll have to sell " + str(varStore.FC) + " sack" + X_s + " of food or skin"\
        + X_s + " of oil.")
    # How much to sell of food and oil
    FS = int(varStore.FC / 2)
    LS = varStore.FC - FS
    while LS > varStore.L:
        LS -= 1
        FS += 1
    while FS > varStore.F:
        FS -= 1
        LS += 1
    # Decrease food and oil, add jewels
    varStore.F -= FS
    varStore.L -= LS
    varStore.JL = varStore.JL + FS + LS
    text = "You sell " + str(FS) + " of food, " + str(LS) + " of oil for which you"\
        " get only " + str(FS + LS) + " jewel" + X_s + "."
    print(wrapText(text))
    
def scenario2310(varStore):
    print(wrapText("Long stretch with bad water. Costs time to find clean wells."))
    varStore.D -= 50
    
def scenario2340(varStore):
    print(wrapText("You get lost trying to find an easier route."))
    varStore.D -= 100

def scenario2360(varStore):
    print(wrapText("Heavy rains completely wash away the route."))
    varStore.D -= 90
    
def scenario2380(varStore):
    print(wrapText("Some of your food rots in the humid weather."))
    varStore.F -= 1
    
def scenario2400(varStore):
    print(wrapText("Marauding animals got into your food supply."))
    varStore.F -= 1

def scenario2420(varStore):
    print(wrapText("A fire flares up and destroys some of your food and clothes."))
    varStore.F -= 0.4; varStore.C -= 1
    chkForZero(varStore)
    if varStore.L < 1:
        return
    else:
        varStore.L -= 0.5
    
def scenario2450(varStore):
    print(wrapText("Two camels wonder off. You finally find them after spending "
        "several days searching for them."))
    varStore.D -= 20
    
def scenario2480(varStore):
    print(wrapText("You get a nasty burn from an oil fire."))
    varStore.PWD = 0.5
    useBalm(varStore)
    
def scenario2510(varStore):
    print(wrapText("High winds, sand storms, and ferocious heat slow you down."))
    varStore.D -= 70
    
def scenario2540(varStore):
    print(wrapText("A gash in your leg looks infected. It hurts like the blazes."))
    useBalm(varStore)
    varStore.D -= 50
    varStore.PWD = 0.7
    
def scenario2570(varStore):
    print(wrapText("Jagged rocks tear your sandals and clothing. You'll have to get "
        "replacements as soon as you can."))
    varStore.C -= 1
    varStore.D -= 30
    
def scenario2600(varStore):
    RN = int(random.random() * varStore.FQ)
    if RN < 2:
        print(wrapText("All of you have horrible stomach cramps and intestinal disorders "
            "and are laid up for over a month."))
        varStore.D -= 275
    elif RN < 3.5:
        print(wrapText("You're running a high fever and your muscles feel like jelly. "
            "Your party slows down for you."))
        varStore.PSK = 0.7
        varStore.D -= 125
    else:
        return
    
def scenario2660(varStore):
    print(wrapText("Blood-thirsty bandits are attacking your small caravan! You grab "
        "your crossbow..."))
    shootCrossbow(varStore)
    if varStore.W > 5:
        if varStore.SR <= 1:
            print(wrapText("Wow! Sensational shooting. You drove them off with no "
                "losses."))
            varStore.W -= 4
            return
        elif varStore.SR <= 3:
            print(wrapText("With practice you could shoot the crossbow, but most of "
                "your shots missed. An iron mace got you in the chest. They took some "
                "jewels."))
            varStore.PWD = 1
            varStore.JL -= 5
            useBalm(varStore)
            varStore.W = varStore.W - 3 - 2 * varStore.SR
            chkForZero(varStore)
            return
        else:
            print(wrapText("Better stick to trading; your aim is terrible."))
    else:
        print(wrapText("You try to drive them off, but you run out of arrows. They grab "
            "some jewels and food."))
        varStore.F -= 1
        chkForZero(varStore)
    # 80% chance of surviving attack
    if random.random() <= 0.8:
        print(wrapText("You caught a knife in the shoulder. That's going to take quite "
            "a while to heal."))
        useBalm(varStore)
        varStore.PWD = 1.5
        varStore.JL -= 10
        varStore.W = varStore.W - 4 - 2 * varStore.SR
        chkForZero(varStore)
        return
    else:
        print(wrapText("They are savage, evil barbarians - they kill you and take your "
            "remaining camels and jewels."))
        varStore.JL = 0; varStore.B = 0
        varStore.W -= 4; chkForZero(varStore)
        endGamePt2(varStore)
    
def useBalm(varStore):
    RN = int(1 + 2 * random.random())
    if RN > 1:
        X_s = "s"
    else:
        X_s = ""
    if random.random() > 0.5:
        XA_s = "balm"
    else:
        XA_s = "unguent"
    varStore.M = varStore.M - RN
    
    if varStore.M < 0:
        varStore.M = 0
        print(wrapText("You need more " + XA_s + " to treat your wound."))
        if varStore.JL > 7:
            print(wrapText("Fortunately, you find some nomads who offer to sell you 2 "
                "bottles of " + XA_s + " for the outrageous price of 4 jewels each."))
            A = getYorN(input("\nDo you want to buy it? "))
            if A == "Y":
                print(wrapText("It works well and you're soon feeling better."))
                varStore.M = 0
                varStore.JL -= 8
                return
        else:
            print(wrapText("But, alas, you don't have enough jewels to buy any."))
        text = "Your wound is badly infected, "
        
        if random.random() < 0.8:
            print(wrapText(text + "but you push on for the next village."))
            varStore.PWD = 3
            return
        else:
            print(wrapText(text + "but you keep going anyway."))
            print();print(wrapText("Unfortunately, the strain is too much for you and, "
                "after weeks of agony, you succumb to your wounds and die in the "
                "wilderness."))
            endGamePt2(varStore)
    else:
        print(wrapText("You use " + str(RN) + " bottle" + X_s + " of " + XA_s + 
            " treating your wound."))
    
def initHuntSkill(varStore):
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

def huntForFood(varStore):
    if varStore.W < 15:
        print("You don't have enough arrows to hunt for food.")
        return
    a = int(1 + 3 * random.random())
    print("There goes a " + varStore.FA_s[a-1] + "... ")
    varStore.W -= 15; shootCrossbow(varStore)
    if varStore.SR <= 1:
        print("With shooting that good, the Khan will want you in his army.")
        varStore.FA = 3
    elif varStore.SR <= 3:
        print("Not bad, you finally brought one down.")
        varStore.FA = 2
    else:
        print("Were you too excited? All your shots went wild.")
        return
    print("Your hunting yields " + str(varStore.FA) + " sacks of food.")
    varStore.F += varStore.FA

    
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
        varStore.A = getIntAns("Your answer please? ")

def main():
    randomize()
    title()
    scenario(varStore)
    getInitSupplies(varStore)
    initHuntSkill(varStore)
    
    while True:
        varStore.J+=1; printDate(varStore)
        varStore.DT+=varStore.D
        
        # Reached end of trip
        if varStore.DT > 6000:
            endTrip(varStore)
        
        varStore.D = 40 + varStore.BA * 20 + int(random.randrange(99))
        print("You have traveled " + str(varStore.DT) + " miles.")
        print("Here is what you now have: "); printInv(varStore)
        
        # Debug
        # What about negative jewels????
        print("\n"); waitToContinue("continue")
        # -continue debug
        
        chkStock(varStore)
        sickness(varStore)
        
        # Camel recover yet?
        if varStore.BSK == varStore.J:
            varStore.BSK = 99; varStore.BL = varStore.B; varStore.BA += 1
        
        # Barter for supplies
        if varStore.J > 1 and varStore.JL > 1:
            barterSupplies(varStore)
        
        # no clothes?
        if varStore.C == 0:
            noClothes(varStore)
            
        # eating routine
        eatFood(varStore)
        
        # 18% chance to hunt for food
        if varStore.DZ == 0 and random.random() < 0.18:
            huntForFood(varStore)
        
        # Desert Sections
        print()
        desertSections(varStore)
        
        # Event Happens
        if varStore.DZ == 0:
            specialEvents(varStore)
        
        chkForZero(varStore)
        
        #endTrip(varStore)
        #tryAgain()

if __name__ == '__main__':
    varStore = varStore()
    main()
