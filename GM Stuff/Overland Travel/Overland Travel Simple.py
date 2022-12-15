# Import Modules
import random

def main():

    # Init lists of tuples
    # Terrain list
    # Terrain, Highwaymod, RoadMod, TracklessMod, navigationDC, ForageDC
    terrainList = [
        ("Desert", 1, .5, .5, 12, 20),
        ("Forest, Sparse", 1, 1, .5, 14, 14),
        ("Forest, Medium", 1, 1, .5, 16, 14),
        ("Forest, Dense", 1, 1, .5, 18, 14),
        ("Hills", 1, .75, .5, 14, 12),
        ("Jungle", 1, .75, .25, 16, 14),
        ("Moor", 1, 1, .75, 14, 16),
        ("Mountains", .75, .75, .5, 16,18),
        ("Plains", 1, 1, .75, 12, 12),
        ("Swamp", 1, .75, .5, 15, 16),
        ("Tundra", 1, .75, .75, 12, 18)
    ]

    # Travel Mode List
    travelModeList = [
        ("Normal", 1),
        ("Cautious", .75),
        ("Exploration", .5),
        ("Foraging", .5),
        ("Leading Mount", .75),
        ("River Crossing", .75)
    ]

    # Weather Conditions list
    weatherConditionList = [
        ("Normal", 1),
        ("Giant Terrain", .75),
        ("Poor Visibility", .5),
        ("Cold", .75),
        ("Hot", .75),
        ("Storm", .75),
        ("Storm, powerful", .5),
        ("Hurricane", .1),
        ("Snow cover", .5),
        ("Snow cover, Heavy", .25)
    ]

    #User Inputs
    
    # Ask for Terrain Type
    print("Accepted Terrains:")
    for item in terrainList:
        print(item[0], end=", ")
    terrain = str(input("\nTerrain Type: "))
    try:
        a = [item for item in terrainList if item[0] == terrain][0]
    except IndexError:
        print("Terrain Error")
        return

    # Ask for Path Type
    print("Accepted Paths: Highway, Road/Trail, Trackless")
    pathtype = str(input("Path Type: "))
    if pathtype == "Highway":
        pathtype = 1
    elif pathtype == "Road/Trail":
        pathtype = 2
    elif pathtype == "Trackless":
        pathtype = 3
    else:
        print("Pathtype Error")
        return

    # Determine terrain mod: Search list of tuples for item, return correct modifier and DC
    terrainMod = [item for item in terrainList if item[0] == terrain][0][pathtype]
    terrainDC = [item for item in terrainList if item[0] == terrain][0][4]
    terrainForagingDC = [item for item in terrainList if item[0] == terrain][0][5]


    # Ask for Weather Condition
    print("Accepted Weather Conditions: ")
    for item in weatherConditionList:
        print(item[0], end=", ")
    weatherCondition = str(input("\nWeather Condition: "))
    try:
        a = [item for item in weatherConditionList if item[0] == weatherCondition][0]
    except IndexError:
        print("Weather Error")
        return

    # Determine Weather Condition Mod
    weatherConditionMod = [item for item in weatherConditionList if item[0] == weatherCondition][0][1]

    
    # Ask for party Travel Mode
    print("Accepted Party Travel Modes: ")
    for item in travelModeList:
        print(item[0], end=", ")
    travelMode = str(input("\nParty Travel Mode: "))
    try:
        a = [item for item in travelModeList if item[0] == travelMode][0]
    except IndexError:
        print("Travel Mode Error")
        return

    # Determine Travel Mode Mod
    travelModeMod = [item for item in travelModeList if item[0] == travelMode][0][1]

    
    # Ask for Party Speed
    partySpeed = int(input("Speed of the SLOWEST party member: "))
    
    # Ask for Party Navigation
    partyNavigation = int(input("Navigation score of party guide: "))
    
    # Check for Compass
    partyVeer = True
    partyCompass = bool(input("Is the guide using a compass? (T/F): "))
    if partyCompass:
        partyNavigation = partyNavigation +2
        partyVeer = False

    # Ask for Tracking
    partyTracking = int(input("Tracking Score of guide: "))
 
    # Determine Lost and Veer: Navigation check vs DC
    lost = False
    if random.randint(1,19) + partyNavigation < terrainDC:
        lost = True
        if partyVeer:
            rand = random.randint(1,9)
            if rand < 5:
                partyVeerDirection = "left"
            elif rand >6:
                partyVeerDirection = "right"
            else:
                partyVeerDirection = "straight"

    # Determine Encounter
    encounter = False
    if travelMode == "Cautious":
        rand = random.randint(1,12)
    elif travelMode == "Exploring":
        rand = random.randint(1,4)
    else:
        rand = random.randint(1,8)
    encounterRoll1 = random.randint(1, 8)
    encounterRoll2 = str(random.randint(1, 100)) + "%"
    if rand == 1:
        encounter = True
        if random.randint(1,2):
            encoutnerType = ["Landmark", encounterRoll1]
        else:
            encoutnerType = [encounterRoll2, encounterRoll1]

    # Determine Distance Traveled
    distanceTraveledRand = random.randint(2,12) + 3
    distanceTraveled = partySpeed * travelModeMod * weatherConditionMod * terrainMod * distanceTraveledRand
    if distanceTraveled > 12:
        leftHex = True

    # Output
    print()
    print("Overland Travel Results")
    print("Terrain = ", terrain)
    print("Condition = ", weatherCondition)
    print("Lost = ", lost)
    if lost:
        print("The party veers ", partyVeerDirection, ".")
    print("Encounter = ", encounter)
    if encounter:
        print("Encounter Type: ", encoutnerType[0])
        print("Encounter Roll: ", encoutnerType[1])
    print("Distance Traveled = ", distanceTraveled, " miles")
    print("Left hex =", leftHex)
    if travelMode == "Foraging":
        print("Foraging DC: ", terrainForagingDC)

main()





