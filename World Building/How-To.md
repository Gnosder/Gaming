# How-to

A doc designed around how I make maps for ttrpg.

# Theory

Each hex should be 12-miles wide, this equates to 7 mile sides, an area of 124 sq miles. A typical human moves at a speed of 3 mph and can move around 24 miles in a day (typically only moving for 2 watches); this equates to 2 hexes, however the distance is often modified by the terrain.

If the local scale is 5 mi. hexes. That equates to 

Several hex scales
- Local Hex (5 mile hexes; roughly 1-2 hours of travel, villages)
- Regional Hex (25 mile hexes; roughly 1 day of travel; multiple towns)
- Realm (125 mile hexes; roughly a week of travel; multiple regions)
- Continental (625 mile hexes; entire countries)

Table
| Name        | Size (mi) | Side (mi) | Area (sqmi) |
| ----------- | --------- | --------- | ----------- |
| Local       | 5         | 2.89      | 21.65       |
| Regional    | 25        | 14.43     | 541.27      |
| Realm       | 125       | 72.17     | 13,531.63   |
| Continental | 625       | 360.85    | 338,291.17  |


# Start Small -- Steps to world creation from small to large

1. Start with a single, 5 mile hex. This hex contains the starting point for the campaign.
2. Flesh out starting hex. Usually it will be a hub or village.
3. Determine spotting range from hex (how many hexes out can be seen).
4. Fill out terrain type for those hexes.
5. When characteres move into a new hex, generate it, then repeat steps 2-4.

# Generating Regional Hexes

1. Choose Climate, if none has already been chosen for the current atlas row.
2. Choose Primary Terrain; if an adjacent regional hex has already been filled out then the primary terrain of the current hex MUST be one of the available terrain types (primary, secondary, tertiary, wildcard) of the adjacent terrain.
3. Assign the rest of the Terrain in the hex.
    1. Assign the primary terrain to 9 full-hexes
    2. Assign the secondary terrain to 6 full-hexes
    3. Assign the tertiary or any wildcard terrains to 3 full-hexes
    4. Assign any of the primary, scondary, or tertiary terrains to the remaining 12 half-hexes

ATLAS HEX PRIMARY TERRAIN TYPE
|           | Water | Swamp | Desert | Plains | Forest | Hills  | Mountains |
| --------- | ----- | ----- | ------ | ------ | ------ | ------ | --------- |
| Water     | P     | W     | W      | W      | W      | W      |           |
| Swamp     | W     | P     |        | W      | W      |        |           |
| Desert    | W     |       | P      | W      |        | W      | W         |
| Plains    | S[1]  | S     | T      | P[4]   | S      | T      |           |
| fOREST    | T[2]  | T     |        | S      | P[5]   | W[8]   | T[11]     |
| Hills     | W     |       | S [3]  | T      | T [6]  | P [9]  | S         |
| Mountains |       |       | W      |        | W [7]  | S [10] | P [12]    |
1 Treat as coastal (beach or scrub) if adjacent to water
2 66% light forest
3 33% rocky desert or high sand dunes
4 Treat as farmland in settled hexes
5 33% heavy forest
6 66% forested hills
7 66% forested mountains
8 33% forested hills
9 20% canyon or fissure
10 40% chance of a pass
11 33% forested mountains
12 20% chance of a dominating peak; 10% chance of a mountain pass; 5% volcano

RANDOM ROLL TERRAIN (For adjacent regional hexes)
| d12   | Adjacent Hex Terrain [1] |
| ----- | ------------------------ |
| 1-6   | Primary                  |
| 7-9   | Secondary                |
| 10-11 | Tertiary                 |
| 12    | Wildcard                 |
1 Relative to current hex primary terrain type