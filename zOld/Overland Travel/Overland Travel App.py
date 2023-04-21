"""
Overland Travel App raw is a first pass of a travel generator
It will take in a few parameters:
    Party
    Mode of Travel
    Terrain
    Conditions
And output how far travel was.
"""

def main():
    
    # Main Menu
    # Show Weather (per week for current area)
    # Travel
    # Show Party

    print("Overland Traveler")
    print("-----------------")
    print()
    print("SHOW WEATHER")
    print("GENERATE TRAVEL")
    print("MANAGE PARTY")
    print()
    option = input("Choose an Option")

    # Navigate

    if option == "SHOW WEATHER":
        Weather("month")
    elif option == "GENERATE TRAVEL":
        # Show weekly weather, display travel
        OutTravel()
    elif option == "MANAGE PARTY":
        Party()
    else:
        print("Something Broke")


def Weather(TimeScale, Terrain=None):
    
    if Terrain == None:
        terrain = str(input("Terrain: "))

    # Generate Weather by Terrain. Output Temp F/C (STR), Weather (STR), Condition modifier (Int)

    condition = condition[0].value

    # Accepted inputs: day, week, month

    if TimeScale == "day":
        return condition, terrain
    if TimeScale == "week":
        print("WIP")
    if TimeScale == "month":
        print("WIP")
    else:
        print("Weather Error")


def OutTravel():
    pass

    lost = False
    terrain, terrainMod = None
    encounter = False
    condition = "Clear"
    travelMod = 1
    
    lost = Lost()
    dangerMod terrainMod = 
    encounter = Encounter(dangerMod)
    conditionMod = Weather("day")

    actualDistance = speed * terrainMod * conditionMod * travelMod

    # Output
    print(Weather("week"))
    print()
    if lost == True:
        print("The Party is Lost!")
    if encounter == True:
        print(f"""The party traveled {actualDistance} before encountering {encounterType} 
        encounter number {encouterNumber}.""")
    print(actualDistance)

def Party():
    pass

    # Find Lowest Party Speed
    speeds = []

    # Set Party Speed
    partySpeed = min(speeds)

class Character:
    def __init__(self):
        self.speed = input("Character's Travel Speed: ")
        self.navigation = input("Character's Navigation Bonus: ")
        self.survival = input("Character's Survival Bonus: ")
        self.tracking = input("Character's Tracking Bonus: ")
        self.encumbered = False
    
    def IsEncumbered(encumbered):
        if encumbered == False:
            encumbered = True
        else:
            encumbered = False