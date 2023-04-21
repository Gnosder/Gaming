# GM Magic App

An app to support and simplifiy the life of game masters (specifically me).

## Features
[] Party Tracker
    [] Add character
    [] Create Parties
    [] Set Active Party
[] Map
    [] Create Map
    [] Import Map
    [] Export Map
    [] Add key to Map
    [] Plot Travel Route
    [] Resolve Travel (w/ break points)
    [] Multiple Scales
    [] Save Map
    [] Navigate Saved Maps
[] Ledger
    [] Track unlooted items
    [] Track looted items
    [] Support identifying items
    [] Generate Simple Items
    [] Track party Encumbrance
[] Initiative Tracker
    [] Add party
    [] Add adversary
    [] Generate initiative for non-PC
    [] Track initiative slot and round
    [] Track pertinant information
[] Adversay Tracker
    [] Add adversary
    [] Import Adversary
    [] Generate simple adversary
[] Session Tracker
    [] Add / take session notes
    [] Export session notes (as plain text)
    [] Compile notes into campaign notes
[] Adventure Notes
    [] Add adventure
    [] Track adventure progress
    [] Create /track clocks and timers
    [] ALWAYS accessible
[] Check roller
    [] Roll simple checks
    [] Roll party perception and other secret rolls
[] Settings
    [] Set system

## Work Flow

I want to add the party to the app. Add/create a world map with a key. Be able to plot a course on the map and have travel details generated. Be able to switch into initiative easily. Have my notes alaways visible.

## Features in Detail

### Party Tracker

This app should allow a GM to add characters w/ important stats. GMs should be able to sort characters into parties and mark an "active party". The tracker should feed information to other apps.

### Map

The map should use a standard Hex format and scale. It should allow you to upload or create a map. It should allow you to create a key for each hex. It should be able to mark temporary things (like the party's location). It should be able to build a travel route and generate travel information.

Has multiple scales. Hexes for overworld and grid for zoomed in (e.g.dungeon/town).

### Ledger

The ledger should track party spoils. Both those the party has and those it does not have. Spoils should have encumbrance, value (both approximate and real), and have un/identified tag. The ledge should be able to auto generate simple loot.

### Initiative Tracker

The tracker should accept a party and adversaries. It should track damage, conditions, durations, and initiative order. It should be able to roll initiative for adversaries as well as check for surprise and morale.

### Adversay Tracker

Similar to the party tracker but for tracking enemies (or allies). Tracks more information and able to send it to the initiative tracker. Can generate simple enemies.

### Session Tracker

A space for taking session notes.

### Adventure Notes

A place to hold adventure notes. Should ALWAYS be easily accessible.

### Check roller

A simple die roller to make checks. Has the ability to roll secret checks for the party (i.e. perception)