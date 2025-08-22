# On Equipment and Loot

This document is designed as a complete inventory and economy system that can be inserted into any game. The ideal is that it will be accompanied by an app that can be tailored per game.

The base of this document was the system I created for Fugue. This is roughly an SP fiat system that uses Bulk and Supply.

I want to rewrite this document to be system agnostic.

TODO
[] Remove system specific language
[] Add Technology level and rarity to items. Tie the two together to make it simple. Or class items as a type of good.


# Equipment

## Currency

The base currency is the Silver Piece (SP) these typically weigh around 9 grams and are standardized throughout a realm or city. While the styling of the coin can change the metal itself tends to have a set value, thus sp from different areas are typically interchangable. 

Some other common coinage is the Copper Peice (CP), which is generally 1/10 the value of the SP, and the Gold Peice (GP), which is generally 10 times the value of the SP. However, local forces can impact these values. For example, in the kingdom of Gaxton 1gp is worth 50sp (due to the rarity of gold in the area).

Other metal and alloys are sometimes used, such as platnium, electrum, rose gold, etc. The value of these coins usually relates to the rarity of the materials used. Platnium is typically worth 100sp, electrum is worth 3sp, and rose gold is worth 8sp.

While some areas use bank notes they are not common and are typically not accepted outside the area in which they are issued.

50 coins weigh about a pound and 500 coins is 1 bulk. It's not important to keep exact track of the weight of coins, simple round down to the nearest bulk. E.g. 999 coins is 1  bulk, not 2.

## Encumbrance 

Creatures can only carry so much. The amount a being can carry is a function of the weight of the item, the size of the item, and the item's general akwardness to carry. This can add up quickly and become cumbersome and so the method of carrying items is simplified as Bulk. 1 Bulk is generally 2-5 kilograms (~5-10 pounds) while an item of a few grams is negligable, everything between the 2 is considered light (L). 10 L items are 1 bulk, rounding down any fractions. E.g. 9 L items is negligable.

While bulk is generally thought of in terms of weight it is important to remember that weight is only one factor. Light, but cumbersome objects can have bulks far larger than their weight. E.g. a 10 ft pole, even though it weighs less than a kg is considered bulk 2 because it is so akward to carry.

Some items have a different bulk depending on if they are worn/in use or if they are stowed.

### Encumbrance Limits

Each creature or object has a limit to the amount it can carry. This is depected by 2 thresholds. The base threshold for being encumbered (typically reducing movement speed, agility, and reaction) and a higher threshold, usually double the first, for being overburdened which typically has a severe penalty to the above attributes.

A good default is that a typical character of human propotions should be able to carry around 10 bulk before becoming encumbered and 20 before being overburdened. With each size catagory greater than medium multiplying the bulk limits by 10. Each size categoriy less than small should decrease the base limit by 3 to a minimum of L.

Note that each charcter, in addition to their bulk limits, only has so much space to carry items. A fully unequiped human can only hold items in their hands (typically only 1 large item or a half dozen small items). Items can be worn that increase the ammount the character can carry, up to their limits.

### Technology Level

Each world and culture (and sometimes settlement within a culture) has a technology level rated on a 1 to 9 scale. Items of a tech level greater than the area's technology level cannot be purchased.

Note that tech levels often refer the to the lowest level an item can be found in.

| Level | Rough example    |
| ----- | ---------------- |
| 1     | Primative        |
| 2     | Bronze Age       |
| 3     | Medevil Age      |
| 4     | Age of Discovery |
| 5     | Industrial Age   |
| 6     | Digital Age      |
| 7     | Inter Planetary  |
| 8     | Intra Galactic   |
| 9     | Hyper Advanced   |

### Item Quality

The prices listed here are for items of average quality and with little to no adornment. The chart below shows the average cost of items of varying qualities and adornments. As quality increases it becomes harder and harder to list a set price, the chart below is mearly a starting point. Poor items typically wear out twice as fast on average and have double the chance to break. High quality items can infer a +1 bonus on their actions. Higher quality items do not.

| Quality     | Price Modifier |         Likely effects         |
| :---------- | :------------: | :----------------------------: |
| Poor        |      x.75      |      Double break chance       |
| Average     |       x1       |              None              |
| High        |       x2       |      Slight bonus to use       |
| Lavish      |       x5       | Bonus to status if worn openly |
| Engraved    |       x2       |                                |
| Bejewled    |       x4       | Bonus to status if worn openly |
| Custom Work |       x2       |   Bonus depends on the work    |

### Item Breakage

Every item has a chance to break or become worn through use. For most items this will not be an issue as simple items can last a long time even without maintenance. However there comes a time when even the most robust tool can break.

When a tool is used improperly, poorly over a short time (days), used without maintenance (months), used with maintenance (years) it has a chance to break. Each time an item has a chance to break there is a 1 in 6 chance it does so and must be replaced or repaired before it can be used again.

#### Repairing an item

When repairing an item there is a chance it degrades one level of quality unless attended to by an expert which costs, on average,  x.75 the initial cost of the item. Non-expert repairs have a 1 in 6 chance of reducing the quality by 1 step. Items reduced below poor quality are unuseable.

## Equipment Lists

### Containers

Cointainers, as their name implies, hold items. 

| Item                   | Price | Bulk(w) | Capacity | Tech Level | Carry Slot    |
| ---------------------- | ----- | ------- | -------- | ---------- | ------------- |
| Backpack, Standard     | 3sp   | 1 (0)   | 8        | 2          | Back          |
| Backpack, Large        | 7sp   | 2 (0)   | 12       | 3          | Back          |
| Backpact, Porter       | 9sp   | 3 (1)   | 16       | 2          | Back          |
| Bandolier, Standard    | 4sp   | 1 (0)   | *        | 2          | Body          |
| Bandolier, 12 Apostles | 8sp   | 1 (0)   | *        | 4          | Body          |
| Barrel, Standard       | 6sp   | 2       | 40       | 1          | Hands         |
| Beltpouch              | 5cp   | -       | 1*       | 1          | Waist         |
| Chest, Standard        | 10sp  | 6       | 20       | 2          | Hands         |
| Quiver                 | 5sp   | 1 (0)   | 1        | 1          | Waist or Back |
| Sack / Dufflebag       | 2sp   | 1       | 20       | 1          | Hands         |
| Saddlebag              | 1sp   | 2 (0)   | 12       | 2          | Mount         |
| Satchel                | 2sp   | 1 (0)   | 6        | 1          | Hand or Body  |
| Scabbard               | 2sp   | L (0)   | *        | 2          | Waist         |
| Scroll Case            | 1sp   | L       | 1*       | 2          |               |
| Shot and Powder bag    | 1sp   | 1       | 1        | 4          |               |
| Waterskin              | 1sp   | L       | 1*       | 1          |               |

Backpack: A container for holding items. Comes in 3 general sizes.
Bandolier: Can hold upto 6 L items that are kept ready for rapid use.
12 Apostles: A special bandolier that holds 12 premeasured shots of powder and has a shot bag that can hold 50 bullets. Reduces reload time in half.
Barrel: A rounded wooden barrel that holds around 50 gallons.
Belt Pouch: Only L items can be stored in the belt pouch.
Chest: A sturdy rectangular wooden box that holds around 25 gallons of materials and often has a basic lock on it.
Quiver: Can carry Arrows or Bolts or other similar ammunition.
Sack: A large bag that can hold a large amount of material and can be compressed for easy storage.
Saddle Bag: A large bag made for riding animals.
Satchel: A small bag often carried in one hand or worn about the shoulders.
Scabbard: Can hold 1 small or medium weapon one-handed weapon.
Scroll Case: A small tube used for storing rolled up papers and scrolls. Only unbound papers of L size can be put in one.
Shot and Powder bag: A small pouch that can hold 50 bullets and a powderhorn with 50 shots.
Waterskin: A liquid holder that can carry about half a gallon of liquid. Roughly 2 standard water rations.

### Gear

| Item                | Price | Bulk | Tech Level |
| ------------------- | ----- | ---- | ---------- |
| Bredroll            | 2sp   | L    | 1          |
| Block and Tackle    | 2sp   | 1    | 2          |
| Compass             | 25sp  | L    | 3          |
| Cookware            | 1sp   | L    | 1          |
| Flint and Steel     | 1sp   | L    | 1          |
| Hourglass           | 100sp | L    | 4          |
| Ladder(10ft)        | 10sp  | 3    | 1          |
| Lantern             | 3sp   | L    | 3          |
| Magnifying Glass    | 60sp  | L    | 4          |
| Manacles            | 10sp  | L    | 2          |
| Merchant's Scale    | 125sp | 1    | 3          |
| Mirror, Hand        | 10sp  | L    | 3          |
| Mug                 | 5cp   | L    | 1          |
| Musical Instrument* | var   | var  | 1          |
| Pole(10ft)          | 1sp   | 2    | 1          |
| Ration              | 3sp   | L    | 1          |
| Supply              | 5sp   | L    | 1          |
| Spyglass            | 250sp | L    | 4          |
| Tent, Pup           | 5sp   | 1    | 2          |
| Tent, 2-person      | 15sp  | 3    | 2          |
Bedroll: A sleeping skin or bag. Something to sleep on and maybe a blanket and pillow depending on quality.
Block and Tackle: Useful for lifting heavy items. A properly anchored block and tackle doubles the amount of bulk a character can lift.
Compass: Grants bonus to navigation checks and automatically determine direction of travel. Note non-magical compasses rely on there being a magnetic pole. If there is not or if something interfers with it, the compass is useless.
Cookware: In this context a simple collection of a pot or pan and some cooking tools.
Flint and Steel: A firestarter of some description.
Hourglass: A glass vessel holding sand that can be used as a timer of a certain increment determined at creation.
Ladder: A simiple straight ladder that must be leaned against a surface.
Lantern: A pint of oil in a lantern burns for 1 turn. Lanterns come in two main types, bullseye and hooded. Bullseye lanterns cast light in a 60ft cone infront of them and can be covered without disrupting the flame. Hooded lanterns cast light 30ft around themselves and can be covered witout disterbing the flame.
Magnifying Glass: A specially made lens that can make small details visible. Often grants a bonus to careful study or investigation.
Manacles: Simple wrist restarints with a simple lock.
Merchant's Scale: A well calibrated set of scales and weights of known values.
Mirror, Hand: A small glass mirror or polised metal surface one can see themself in.
Mug: A cup.
Musical Instrument: This is a broad class of items within which the price and bulk can vary greatly. However, for simple hand instruments (flute, harp, drum, lute) the price ranges from a few copper to a few silver and the bulk is usually L with larger instruments (lute, guitar) being 1 bulk.
Pole: A simple, wooden pole.
Ration: An abstracted item reprsenting appropriate food and water for a creature.
Supply: An abstracted item representing all the varius adventuring items that competent adventuers pack. Generally at any point a character can spend a number of supply on any of the items listed on the supply chart. If there is ever any doubt as to whether a character remembered to pack an item they can make a luck save against the supply cost of the item + 10.
Tent: Pup tents are large enough to hold only a single small or medium creature and keep them reasonably protected from the elements.

### Magical Items

| Item               | Price          | Bulk | Tech Level |
| ------------------ | -------------- | ---- | ---------- |
| Spellbook          | 100sp          | 1    | 3           |
| Holy Symbol, Wood  | 12sp           | L    | 1           |
| Holy Symbol, Metal | 31sp           | L    | 2           |
| Reagents           | *              | *    | *           |
| Scroll             | Force x 100sp  | L    | 2           |
| Wand               | Force x 2000sp | L    | 2           |

Spellbook: A specially constructed and preparred book for storing spells and magical learnings.
Holy Symbol: Often a specially made and blessed symbol of a God or religion.
Reagents: A catch all used for magical materials, see the On Magic section for more information.
Scroll: An often one use item usually written on paper that contains a single spell.
Wand: A small hand held object that can be used to cast or enhance spells.

### Written Items
 | Item            | Price | Bulk | Tech Level |
 | --------------- | ----- | ---- | ---------- |
 | Book, Empty     | 10sp  | 1    | 3          |
 | Book, Reference | 60sp  | 1    | 3          |
 | Map, Sketch     | 5cp   | L    | 2          |
 | Map, Detailed   | 20sp  | L    | 3          |

### Supplies
| Item                  | Supply | Tech Level |
| --------------------- | :----: | ---------- |
| Arrow(10) or bolt (5) |   1    | 1          |
| Bandage               |   1    | 1          |
| Caltrops(bag)         |   1    | 2          |
| Chalk                 |   1    | 2          |
| Crowbar               |   1    | 2          |
| Grappling Hook        |   1    | 2          |
| Lard                  |   1    | 1          |
| Long Tool             |   10   | 1          |
| Oil (1pt)             |   1    | 2          |
| Piton (10)            |   1    | 2          |
| Powder (10)           |   1    | 4          |
| Repair Kit            |   1    | 2          |
| Rope (50ft)           |   10   | 2          |
| Short Tool            |   5    | 1          |
| Bullet and shot(1)    |   1    | 4          |
| Signal Whistle        |   1    | 2          |
| Torch                 |   1    | 1          |
| Vial                  |   1    | 2          |

### Profession Tools
| Item      | Price | Bulk | Description                 | Tech Level |
| --------- | ----- | ---- | --------------------------- | ---------- |
| Alchemist | 75sp  | 2    |                             | 3          |
| Artisan   | 50sp  | 2    | Type chosen when purchased. | 2          |
| Climbing  | 10sp  | 2    |                             | 2          |
| Disguise  | 10sp  | L    |                             | 2          |
| Healer    | 5sp   | 1    |                             | 1          |
| Riding    | 25sp  | 2    |                             | 2          |
| Scribe    | 3sp   | L    |                             | 3          |
| Snare     | 5sp   | 2    |                             | 1          |

Attempting to perform a check without proper tools imposes disadvantage and may not be possible.

### Animals
| Item          | Price | Tech Level |
| ------------- | ----- | ---------- |
| Dog           | 1sp   | 1          |
| Horse, Riding | 100sp | 1          |
| Horse, War    | 500sp | 2          |
| Horse, Work   | 80sp  | 2          |
| Livestock     | var   | 1          |

### Pack Animals and carts
| Animal        | Price  | Carry Capacity | Movement Speed |
| ------------- | ------ | -------------- | -------------- |
| Donkey        | 25sp   | 70 Bulk        | 30ft           |
| Mule          | 50sp   | 100 Bulk       | 40ft           |
| Horse, Riding | 80sp   | 100 Bulk       | 50ft           |
| Horse, Draft  | 200sp  | 150 Bulk       | 40ft           |
| Cart          | 50sp   | x20 Bulk       | 40ft           |
| Wagon         | 150sp* | x35 Bulk       | 30ft           |


Carts: Often single axle vehicle pulled by a single animal and can allow the animal to pull up to its maximum load.
Wagon: Multi-axle vehciles that can be pulled by multiple animals. To determine how much a wagon can carry, add up the max carry load of all the animals and multiply it by 35. When a wagon is purchased its size is set to the number of animals that call pull it. A wagon's base price is increased by 10% for each animal that can pull it after the first. Attempting to pull a cart or wagon with more animals than its rated for has a chance to break the vehicle and only allows additional animals to apply half their carry capacity to the total amount.


### Vehicles

| Item            | Price   | Tech Level |
| --------------- | ------- | ---------- |
| Cart            | 50sp    | 2          |      
| Coach           | 500sp   | 4          |      
| Wagon           | 150sp   | 3          |      
| Chariot         | 250sp   | 2          |      
| Boat, Raft      | 5sp     | 1          |      
| Boat, Canoe     | 30sp    | 1          |      
| Boat, Rowboat   | 100sp   | 2          |      
| Ship, Riverboat | 1000sp  | 3          |      
| Ship, Sailboat  | 6000sp  | 4          |      
| Ship, Cog       | 15000sp | 4          |      

### Services - Transportation (per 5 miles)

| Item         | Price | Tech Level |
| ------------ | ----- | ---------- |
| Caravan      | 3sp   | 2          |
| Carriage     | 10sp  | 3          |
| Ferry        | 1sp   | 2          |
| Sailing Ship | 2sp   | 2          |

### Services - Loding (per day)

| Item                      | Price |
| ------------------------- | ----- |
| Barn                      | 1cp   |
| Inn, Poor                 | 1sp   |
| Inn, Average              | 5sp   |
| Inn, Fancy                | 25sp  |
| Inn, Extravagant          | 100sp |
| Rent, 1 month (per 10'sq) | 30sp  |

### Services - Training

Price and Time can vary.

| Item                      | Price         | Time             |
| ------------------------- | ------------- | ---------------- |
| Skill - Beginner          | 250sp         | 3 Days           |
| Skill - Intermediate      | 1000sp        | 8 Days           |
| Skill - Advanced          | 1500sp        | 14 days          |
| Language                  | 300sp         | 22 days          |
| Retrain Class             | Level x 500sp | 4 days per level |
| Retrain Skill or Language | 450sp         | 5 days           |

### Services - Professional (Per day)

| Item            | Price                  |
| --------------- | ---------------------- |
| Spell Casting   | Caster's Level x 200sp |
| Scribing        | 16sp                   |
| Laborer         | 1sp                    |
| Skilled Laborer | 8sp                    |
| Musician        | 11sp                   |
| Actor           | 10sp                   |

### Armor

| Catagory | Item             | Price  | Bulk (Worn) | Abilities   | Tech Level |
| -------- | ---------------- | ------ | ----------- | ----------- | ---------- |
| Light    | Padded Armor     | 25sp   | 2 (1)       | Concealable | 1          |
|          | Studded Leathers | 60sp   | 2 (1)       |             | 2          |
| Medium   | Chain Shirt      | 80sp   | 2 (2)       |             | 3          |
|          | Breastplate      | 300sp  | 4 (2)       |             | 2          |
| Heavy    | Splint Armor     | 750sp  | 6 (3)       | Bastion     | 4          |
|          | Plate Armor      | 2000sp | 8 (4)       | Bastion     | 4          |
| Shield   | Shield, Standard | 25sp   | 1           |             | 1          |
|          | Shield, Tower    | 50sp   | 2           |             | 1          |

Heavy armor must be custom fitted to a particular individual imposes a penalty to stealth and doubles all fatigue loss.

Shield: Grants at least +4 defense or adds one if defense is +4 or greater. Ignores the first instance of shock each round.
Tower shield: As shield and grants half cover against ranged attacks or full cover with full defense.

Bastion: A item with this property protects the wearer from all slashing and piercing damage that cannot penetrate the metal.
Concealable: An item with this property can be worn as and under cloths with no penalty.


### Melee Weapons

| Weapon Class | Abilities                   | Price | Bulk | Example Weapons                     |
| :----------- | :-------------------------- | ----- | :--: | ----------------------------------- |
| Covert       | S and one of: LL, PM, T     | 10sp  |  L   | Shiv, Stilleto, Sap, Throwing Star  |
| Light        | Advantage                   | 20sp  |  1   | Short Sword, Rapier, Daggers        |
| Large        | V                           | 40sp  |  2   | Bastard Sword, battleaxe, warhammer |
| Very Large   | 2h                          | 50sp  |  3   | Great Sword, Great Axe, Caber       |
| Reach        | L,Can't be Counter attacked | 30sp  |  2   | Poleaxe, Spear, Glaive              |

### Ranged Weapons

| Weapon Class   | Range | Abilities  | Price | Bulk | Example Weapons                   | Tech Level |
| -------------- | ----- | ---------- | ----- | ---- | --------------------------------- | ---------- |
| Bow            | Short | 2h         |       | 1    | Shortbow, Hunting Bow             | 1          |
| Longbow        | Long  | 2h, C      |       | 2    | English Longbow, Seige Bow        | 2          |
| Crossbow       | Short | 2h, AP, SR |       | 1    | Crossbow                          | 3          |
| Firearm, Short | Close | AP         |       | 1    | Flintlock Pistol, Revolver        | 4          |
| Firearm, Long  | Long  | AP         |       | 2    | Matchlock Musket or Hunting Rifle | 4          |
Arrows are L and stack up to 20 for 1 Bulk.
Bolts are L and stack up to 10.

The range and abilities listed are for the basic version of the weapon, more advanced weapons may have different ranges or abilities.

#### Weapon Traits

2H: Two Handed. Requires two-hands.
AP: Armor Piercing. This weapon ignores non-magical armor.
C: Cumbersome. Attacks against target's within 30ft are at -2.
H: Heavy. Weapons with the Heavy trait deal extra damage, but their negative abilites are often heightened.
L: Long. This weapon has reach and can attack from 10ft away.
LL: Less Leathal. Foes brought to zero stamina with this weapon can be left alive.
N: Numerous. Up to 5 of these weapons can be readied at once.
PM: Precisely Murderous. When used to execute a target deals double damage.
R: Reload. Takes a move action to reload
S: Subtle. Can easily be hidden.
SR: Slow Reload. Takes 3 rounds to reload.
SS:  Single Shot. Takes 10 rounds to reload.
T: Throwable. Can be thrown up to 30ft but deals no shock.
V: Versitile. Can be used one handed or two handed. Does increased damage if used 2 handed.

## Retainers

Retainers are NPCs hired to aid characters in their journies, no matter what those might be. From brave porters to swarthy workmen to skilled professionals retainers cover a large base. In game terms retainers have a price, a loyalty, and a benefit. As the game goes on and retainers are interacted with they can become more important and/or connected to the characters, this can come with benefits.

### Non-adventuring Retainers
| NAME                   | Daily Wage | Monthly Daily | Description | Bonus*                               |
| :--------------------- | ---------- | ------------- | ----------- | ------------------------------------ |
| Accountant             | 50sp       | 200sp         |             | x1.5 property value                  |
| Craftsman              | 10sp       | 100sp         |             | x1.5 workshop value                  |
| Usher                  | --         | 150sp         |             | x1.5 property value                  |
| Coachman               | 5sp        | 75sp          |             | x1.5 stable value                    |
| Guard                  | 5sp        | 75sp          |             | x1.5 defenses value/score            |
| Scholar                | 10sp       | 100sp         |             | x1.5 Library value                   |
| Alchemist              | 20sp       | 250sp         |             | x1.5 Laboratory value                |
| Mage                   | 50sp       | 375sp         |             | x1.5 to anywhere                     |
| Animal Handler         | 4sp        | 125sp         |             | x1.5 Animal Pen value                |
| Laborer                | 2sp        | --            |             | Needed 1 per XX SP value of upgrades |
| Physician              | 15sp       | 275sp         |             | x1.5 Healing Speed                   |
| Servant                | --         | 50sp          |             | Needed 1 per XX SP value of Manor    |
| Mayor                  | --         | 250sp         |             | x1.5 to village value                |
| Entertainer            | 5sp        | 100sp         |             |                                      |
| Artisasn               | 15sp       | 130sp         |             | Need 1 per XX SP value of work       |
| Professional Assistant | **         | **            |             | Need 1 per XX sp value of area       |
|                        |            |               |             |                                      |

* Modifiers are to the BASE value of the area. Multiple instances of the same role do not stack.
Non-adventuring retainers are typically attached to a specific area or role and grant a bonus to the value of that area or role. In the case of servants and assistants, if the number needed is not met than the area or role losses its bonus. For laborers and Artisans the work cannot begin or progress without the required number.
** Professional Assistant is a catch all title for any assisstants that may be needed. I.e. an assistant Alchemist, assistant physician, etc. They typically expect to be paid 75% of what their supervisor is paid.

### Adventuring Retainers
| Name       | Base Share | Description                                                                                   | Bonus |
| ---------- | ---------- | --------------------------------------------------------------------------------------------- | ----- |
| Porter     | 1          | Strong backs that carry goods or drive pack animals                                           |       |
| Teamster   | 2          | Loads and manages porters and pack animals                                                    |       |
| Guard      | 1          | Trained soldiers that protect caravans and expeditions.                                       |       |
| Guide      | 2          | Skilled survivalists or knowledgable locals who help expeditions get to where they are going. |       |
| Mercenary  | 2          | Trained soldiers who will do most anything for a paycheck                                     |       |
| Explorer   | 2          | Learned professionals, scientists, and researchers                                            |       |
| Adventurer | *          | Brave individuals that delve the darkplaces for loot and glory                                |       |

* Adventuruers are sometimes also called cohorts and, while always of a lower level than player characters, typically receive the same shares as the PCs.

#### Sidebar: Shares

A share is a portion of the wealth recovered from an expedition. Each person has a share value. At the end of an expidention divide the total loot by the sum of everyone's shares to determine how much of the loot each share is worth. Player characters can generally set their own shares but values of 5 or 6 are common among more community minded individuals (pirates and the like) while other some particularly greedy individuals can have as much as 100 shares. 
Pay is generally considered important for adventurers and large disparities in pay between the lowest and highest paid members can breed resentment and lower retainer loyalty.

#### Retainer Loyalty

All retainers have a loyalty to their employers that will change over time. Well treated and/or paid retainers' loyalty will increase while mistreated or poorly paid retainers' loyalty will decrease. Loyalty is set when a retainer is hired and changes when they get paid or something happens to effect their loyalty. Note: Its easier to lose loyalty than it is to gain it.
Events that can effect loyalty are changes in pay or living situation, deaths of other retainers (especially if the employer is complicit), poor treatment, scndalous or illegal events, changes in employer.

#### Retainer Death Benefits

Death is always a risk for any expedition. Its common for retainers to request benefits be paid to family or next of kin in the event of their death. These death benefits are generally expected to be 300% ( or 3 times) their expected pay. The benefits are usually taken out of the leader's pay.

#### Hiring Retainers

When hiring retainers roll 3d6 and add the hiring character's Charisma and any other bonuses or penalties listed below (hiring event 4.2.1) and then consult the hiring chart 4.2.2.

Chart 4.2.1
| Hiring Event                                             | Modifier |
| :------------------------------------------------------- | :------: |
| Pay is 50% more than expected                            |    +1    |
| Pay is 10% less than expected                            |    -1    |
| Employer has a positive reputation                       |    +1    |
| Employer has a negative reputation                       |    -2    |
| The position is going to last more than a month          |    +1    |
| The position comes with room and board                   |    +1    |
| If living quarters are expected and they are 50% larger  |    +1    |
| If living quarters are expected and they are 10% smaller |    -1    |
| The position is going to last more than a year           |    +2    |

A modifier can effect a roll more than once. For example if the pay is 50% less than normal then a -5 applies.
To get the bonus for positions lasting more than a month or year a contract is typically created specifying that, in the event the employment ends, the employee is entitled to up to half the remaining pay.

Chart 4.2.2
| Roll | Accept Position | Loyalty/Morale |
| :--: | :-------------: | :------------: |
|  3   |       No        |       2        |
|  4   |                 |       3        |
|  5   |                 |       4        |
|  6   |                 |       5        |
|  7   |                 |       6        |
|  8   |                 |       6        |
|  9   |                 |       7        |
|  10  |                 |       7        |
|  11  |       Yes       |       7        |
|  12  |                 |       7        |
|  13  |                 |       8        |
|  14  |                 |       8        |
|  15  |                 |       9        |
|  16  |                 |       10       |
|  17  |                 |       11       |
|  18  |                 |       12       |

# Loot

Throughout their adventures characters will collect a plethora of unique and different items. These come in several broad catagories: Equipment (that which can be used) both mundane and magical, Treasure (gems, coins, art, and jewlrey), titles (names and deeds), and property. Mundane equipment was covered in the previous chapter. This chapter will focus on magical items, treasure, titles, and property.

## Magical Items
### Potions
Single Use magical potions.
| Potion     | Price | Effect           |
| :--------- | :---: | :--------------- |
| Vigor      |       | Restore stamina  |
| Mana       |       | Restore Mana     |
| Stone Skin |       | Increase Defense |
|            |       |                  |

In general potions can be used up to force 3 and cost the same as scrolls.

### Scrolls
Single use spells. They do not expend mana as the mana is spent when the scroll is created. Alternativly, mana can be expended to keep the scroll intack. Each cast after the first in a day has an increasing chance to destroy the scroll.

### Wands
Similar to Scrolls but multi-use.

### Armaments
Weapons and Armor

### Wonderous Items
Misc items that grant a wide varety of effects.

### Materia
Anceint soul crystals that impart knowledge to those who own them.

### Crafting Magic Items
Creation of magic items and their formulas.

## Treasure

### Sidebar: Money and Value
Trade bars: Sometimes metal is cast in bars of standard weights. A 2 lb bar is worth 100 coins of its metal and a 5lb bar is worth 250 coins.

### Sidebar: Sellling Loot
Selling loot can be a time consuming process which usually entails trips to many different businesses to find buyers. It talkes a full day to sell loot, which entails visiting numerous shops and haggelling. At the end of the day the GM will generate a list of the prices people are willing to pay for each item and the character selling them can decide to sell each item or keep it.

### Coins
The value of a coin is typically denoted by its metal content and size. However they can have different values in different areas. Further, some coins hold special value to collectors and historians.

### Goods
Goods is a broad category but typically refers to 'trade goods' or items that are typically traded. This can be in food, water, spices, raw materias such a wood, metal, or cloth. This can also be finished goods such as furnature. Goods can be perishable, meaning they rot relativly quickly, decaying meaning they lose some potency with time but may not be useless, and timeless where only extreme time can damage them.

### Gems and Art
Whereas goods are used to meet needs, art exists to create culture. Art generally increases in value the older it is.

## Titles
Titles are given in recognition of deeds, inherited from family, purchased, even even given to oneself. They come in many forms and as many places. Every region of every world has their own customs and norms around the giving and receiving of titles.
In general titles themselves mean very little on their own, but they can mean a great deal to the people or culture that imparted it. Being called the "Savior of Havenshire" may not mean much 1000 miles from havenshire, but to the citizens of havenshire it probably means a great deal. 
Reputations and privlages are much the same. They tend to only matter to those they are about or impact. All that is to say that its not possible to make a list of possible titles. 
### Reputations
Whenever you interact
### Privlages
### Sample Titles

## Property
Thoughout their careers characters can gain property which generally falls into two categories: Luxery and Commercial. Luxery properties exist for prestige and comfort, these a things like apartments, villas, and palaces. Commercial property on the other hand is anything that can generate income like stores, mines, businesses.
Characters can also make investsments in businesses and ventures. While similar to commercial property in that investsments generate income they are almost always independent of the characters (meaning there is little they can do to influence them), Investsments generally 
### Luxery Property
Luxery Property has 2 main game benefits: the first is establishing and enhancing ones lifestyle, the second is granting downtime and rest bonuses.

If a person rests in a nice place they can get bonuses to FP refresh, temporary  stamina, temporary mana, short duration consumables, grit or even more. All these bonuses fade the next time you take a long rest.

#### Lifestyle
Everyone who lives needs a place to do it. Add to that food, water, cloting, and the other necceities that make life worth living and you have a great many needs that need to be met. All that together is called Lifestyle and its broken up into brackets.

| Lifestyle    | Cost | Benefits                                    |
| :----------- | :--: | :------------------------------------------ |
| Wretched     |      | No FP Refresh, reputation: homeless         |
| Squalid      |      | 1 FP Refresh, reputation: poor              |
| Poor         |      | 2 FP Refresh                                |
| Modest       |      | Full FP Refresh                             |
| Comfortable  |      | Full FP Refresh + 1                         |
| Wealthy      |      | Full FP Refresh + 1, Reputation: Wealthy    |
| Aristocratic |      | Full FP Refresh + 2, Reputation: Aristocrat |

### Commercial Property
### Investments