def main():

    # Init lists of tuples
    # Terrain list
    # Terrain, Highwaymod, RoadMod, TracklessMod, navigationDC, ForageDC
    terrainList = [
        ("Desert", 1, .5, .5, 12, 20),
        ("Forest(Sparse", 1, 1, .5, 14, 14),
        ("Forest(Medium)", 1, 1, .5, 16, 14),
        ("Forest(Dense)", 1, 1, .5, 18, 14),
        ("Hills", 1, .75, .5, 14, 12),
        ("Jungle", 1, .75, .25, 16, 14),
        ("Moor", 1, 1, .75, 14, 16),
        ("Mountains", .75, .75, .5, 16,18),
        ("Plains", 1, 1, .75, 12, 12),
        ("Swamp", 1, .75, .5, 15, 16),
        ("Tundra, Frozen", 1, .75, .75, 12, 18)
    ]

    # Travel Mode List
    travelModeList = [
        ("Normal", 1),
        ("Cautious Travel", .75),
        ("Exploration", .5),
        ("Foraging", .5),
        ("Leading Mount", .75),
        ("River Crossing", .75)
    ]

    # Weather Conditions list
    weatherConditionList = [
        ("None", 1),
        ("Giant Terrain", .75),
        ("Poor Visibility (Fog, dark", .5),
        ("Cold or Hot Climate", .75),
        ("Storm, normal", .75),
        ("Storm, powerful", .5),
        ("Hurricane", .1),
        ("Snow cover, Light", .5),
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

    # Determine terrain mod: Search list of tuples for item, return correct modifier
    terrainMod = [item for item in terrainList if item[0] == terrain][0][pathtype]


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
    partyCompass = bool(input("Is the guide using a compass? (T/F): "))
    
    # Ask for Survival
    partySurvival = int(input("Highest Survival Score in Party: "))
    
    # Ask for Tracking
    partyTracking = int(input("Tracking Score of guide: "))
 
    # Determine Lost and Veer
    lost = False

    # Determine Encounter
    encounter = False
    # Encounter 1 in 8
    # if rand 1 in 8 is 1 encounter = True
    # Hex Feature 1 in 2
    # if rand 1 in 2 is 1 encounter = "Landmark Discovered"

    # Determine Distance Traveled
    distanceTraveled = partySpeed * travelModeMod * weatherConditionMod * terrainMod
    if distanceTraveled > 12:
        leftHex = True

    # Output
    print()
    print("Overland Travel Results")
    print("Terrain = ", terrain)
    print("Condition = ", weatherCondition)
    print("Lost = ", lost)
    print("Encounter = ", encounter)
    print("Distance Traveled = ", distanceTraveled + " miles")
    print("Left hex =", leftHex)

main()





