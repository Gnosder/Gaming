#! python3

''' 
Loot.py
A generator to practice my abilities and for use at the table.
Set parameters and generate 3 loot piles (choose 1)

'''

# Set Parameters
def settings():
    '''
    SKIP System: Fugue, PF, PF2, 5E, etc
    SKIP Method: FFoD
    Trove size: HD, Tier, etc
    Coins: All, Heavy, Lite, None
    Goods: Balanced, Trade+, Art+, No Trade, No Art
    Num to Gen: 1-6
    All fields will be converted to drop down so no need to validate
    '''
    print("System: Fugue")
    print("Method: Fist Full of Dice")
    tier_int = input("What Tier is the Loot? (1-7): ")
    troveSize_int, tierName_str = findTroveSize(tier_int)
    print("Tier is: " + tierName_str)
    print("Trove Size: " + troveSize_int)
    coinAmount_int = input("How much of the tove should be coins? (All, Mix, None): ")
    print("Amount of Coins: " + coinAmount_int)
    numToGen_int = input("How many troves should be generated? (1-6): ")
    print("Number to Generate is: " + numToGen_int)
    return troveSize_int, coinAmount_int, numToGen_int, tier_int

# Find Trove Size
def findTroveSize():
    '''
    In: tier_int
    Do: look up int on table to find size and name
    Out: troveSize_int, tierName_str
    '''

# init roller
def prep(troveSize, coinAmount):
    '''
    In: Trove Size, Coins
    Out: Coin Dice, Item Dice
    '''
    itemDice = troveSize - coinAmount
    coinDice = coinAmount
    return itemDice, coinDice

# Roll Coins
def coinsMain(coinDice, tier):
    '''
    In: Coin Dice, System
    Do: Roll coins and apply system mod
    Out: Coins Final 
    '''
    import random
    randomValue = random.randint(coinDice, coinDice * 6)
    coinMultiplier = tier
    coinRaw = randomValue * coinMultiplier
    # make the raw amount into cp, sp, gp etc and add a bit so it's not even
    coinAmount = coinRaw
    return coinAmount

# Roll Items
def itemsMain():
    '''
    In: Item Dice, Goods
    Do: Roll item dice to determine items
        Roll # of items
        Find Quality for each item
        Find each item's Rarity 
        Find each item's Type
        Further determine item's type as needed
    Out: Items Final (item1,item2)
    '''

# Output Results
def lootOut():
    """
    In: Coins Final, Items Final
    Do: Make results readable
    Out: Print results
    """

# Main
def main():
    '''
    In:
    Do: Flow control
    Out: None
    '''
    troveSize, coinAmount, numToGen, tier = settings()
    for x in numToGen:
        itemDice,coinDice = prep(troveSize, coinAmount)
        coinsFinal = coinsMain(coinDice, tier)
        itemsFinal = itemsMain(itemDice)
        lootOut(coinsFinal, itemsFinal)

