# Paradox Generator will take in a paradox value and output the effects.

import random

def TakeInputs():
    rawParadox = int(input("How much paradox? "))
    areaInstability = int(input("How unstable is the area? "))
        if not areaInstability:
            areaInstability = 0
    return rawParadox, areaInstability

def ParadoxRoller(rawParadox):
    # This fucntion is just to roll dice and determine a random number.
    paradoxRoll = Roll2D6() + rawParadox
    return paradoxRoll

def ParadoxEffect(paradoxRoll, rawParadox, areaInstability):
    # Determine paradox effect.
    if paradoxRoll < 6:
        print("Suffer %s stress" % rawParadox)
    elif paradoxRoll <12:
        print("The local area gains %s instability." % rawParadox)
    elif paradoxRoll <18:
        WildMagic(rawParadox, areaInstability)
    else:
        # Rip a hole to a random plane if area instability is >10 otherwise reduce rawParadox by 1 and do wild magic.
        if areaInstability > 10:
            RipHole()
        else:
            rawParadox = rawParadox - 1
            WildMagic(rawParadox, areaInstability)

def WildMagic(rawParadox, areaInstability):

    enemyRicochet = 0
    allyRicochet = 0
    paradoxBonus = 0

    for x in range(rawParadox):

        wildRoll = Roll2D6()

        if wildRoll < 5:
            enemyRicochet += 1
        elif wildRoll < 7:
            paradoxBonus += 1
        elif wildRoll == 7:
            areaInstability += 1
        elif wildRoll < 10:
            paradoxBonus -= 1
        else:
            allyRicochet +=1

    if paradoxBonus >= 0:
        paradoxBonusFinal = "gains +%s" % paradoxBonus
    else:
        paradoxBonusFinal = "loses -%s" % paradoxBonus
        
        print("""The area's instability increases to %s, the spell %s to its roll and it targets %s additional allies 
        and %s additional enemies.""" % areaInstability, paradoxBonusF, allyRicochet, enemyRicochet)
        
def RipHole():

    planarRoll = random.randint(1,20)

    if planarRoll % 2 == 0:
        print("A portal to the Feywild rips open for %s hours." % rawParadox)
    elif planarRoll in [3,7,13]:
        print("A portal to the Abyss rips open for %s hours." % rawParadox)
    elif planarRoll == 5:
        print("A portal to the Plane of Water rips open for %s hours." % rawParadox)
    elif planarRoll == 9:
        print("A portal to the Plane of Earth rips open for %s hours." % rawParadox)
    elif planarRoll == 11:
        print("A portal to the Plane of Air rips open for %s hours." % rawParadox)
    elif planarRoll == 13:
        print("A portal to the Plane of Fire rips open for %s hours." % rawParadox)
    else:
        print("A Doom Rift rips open for %s hours." % rawParadox)

def RollD6():
    return random.randint(1,6)
    
def Roll2D6():
    return RollD6() + RollD6()

def Main():
    rawParadox, areaInstability = TakeInputs()
    ParadoxEffect(ParadoxRoller(rawParadox), rawParadox, areaInstability)

# run on execute
if __name__ == "__main__":
    Main()