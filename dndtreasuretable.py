#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mallen
#
# Created:     08/01/2013
# Copyright:   (c) mallen 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    print loot_gen(5,2)

def loot_gen(level, treaslev):
    #level is either the challenge rating of a single monster or the encoutner rating of a group
    #treaslev is the treasure rating of the encounter or monster, standard is 1
    treasure = []
    count = 0
    while count < treaslev:
        roll = dper()
        if level <= 1:
            if roll <= 14:
                treasure += []
                count += 1
            elif roll <= 29:
                treasure += [str(dieroll(1,6)*1000) + "cp"]
                count += 1
            elif roll <= 52:
                treasure += [str(dieroll(1,8)*100) + "sp"]
                count += 1
            elif roll <= 95 and roll >= 91:
                treasure += [str(dieroll(2,8)*10) + "gp"] + [gems(1)]
                count += 1
            elif roll <= 95:
                treasure += [str(dieroll(2,8)*10) + "gp"]
                count += 1
            elif roll <= 100:
                treasure += [str(dieroll(1,4)*10) + "pp"] + [art(1)] + [magicitem(1,"minor")]
                count += 1
        elif level == 2:
            if roll <= 13:
                treasure += []
                count += 1
            elif roll <= 23:
                treasure += [str(dieroll(1,10)*1000) + "cp"]
                count += 1
            elif roll <= 43:
                treasure += [str(dieroll(2,10)*100) + "sp"]
                count += 1
            elif roll <= 95 and roll >= 86:
                treasure += [str(dieroll(4,10)*10) + "gp"] + [gems(dieroll(1,3))] + [magicitem(1,"minor")]
                count += 1
            elif roll <= 95 and roll >= 82:
                treasure += [str(dieroll(4,10)*10) + "gp"] + [gems(dieroll(1,3))]
                count += 1
            elif roll <= 95:
                treasure += [str(dieroll(4,10)*10) + "gp"]
                count += 1
            elif roll <= 100:
                treasure += [str(dieroll(2,8)*10) + "pp"] + [art(dieroll(1,3))] + [magicitem(1,"minor")]
                count += 1
        elif level == 3:
            if roll <= 11:
                treasure += []
                count += 1
            elif roll <= 21:
                treasure += [str(dieroll(2,10)*1000) + "cp"]
                count += 1
            elif roll <= 41:
                treasure += [str(dieroll(4,8)*100) + "sp"]
                count += 1
            elif roll <= 95 and roll >= 80:
                treasure += [str(dieroll(1,4)*100) + "gp"] + [gems(dieroll(1,3))] + [magicitem(1,"minor")]
                count += 1
            elif roll <= 95 and roll >= 78:
                treasure += [str(dieroll(1,4)*100) + "gp"] + [gems(dieroll(1,3))]
                count += 1
            elif roll <= 95:
                treasure += [str(dieroll(1,4)*100) + "gp"]
                count += 1
            elif roll <= 100:
                treasure += [str(dieroll(1,10)*10) + "pp"] + [art(dieroll(1,3))] + [magicitem(1,"minor")]
                count += 1
        elif level == 4:
            if roll <= 11:
                treasure += []
                count += 1
            elif roll <= 21:
                treasure += [str(dieroll(3,10)*1000) + "cp"]
                count += 1
            elif roll <= 41:
                treasure += [str(dieroll(4,12)*1000) + "sp"]
                count += 1
            elif roll <= 95 and roll >= 68:
                treasure += [str(dieroll(1,6)*100) + "gp"] + [gems(dieroll(1,4))] + [magicitem(1,"minor")]
                count += 1
            elif roll <= 95 and roll >= 61:
                treasure += [str(dieroll(1,6)*100) + "gp"] + [gems(dieroll(1,4))]
                count += 1
            elif roll <= 95:
                treasure += [str(dieroll(1,6)*100) + "gp"]
                count += 1
            elif roll <= 100:
                treasure += [str(dieroll(1,8)*10) + "pp"] + [art(dieroll(1,4))] + [magicitem(1,"minor")]
                count += 1
        elif level >= 5:
            if roll <= 10:
                treasure += []
                count += 1
            elif roll <= 19:
                treasure += [str(dieroll(1,4)*10000) + "cp"]
                count += 1
            elif roll <= 38:
                treasure += [str(dieroll(1,6)*1000) + "sp"]
                count += 1
            elif roll <= 95 and roll >= 68:
                treasure += [str(dieroll(1,8)*100) + "gp"] + [gems(dieroll(1,4))] + [magicitem(dieroll(1,3),"minor")]
                count += 1
            elif roll <= 95 and roll >= 61:
                treasure += [str(dieroll(1,8)*100) + "gp"] + [gems(dieroll(1,4))]
                count += 1
            elif roll <= 95:
                treasure += [str(dieroll(1,8)*100) + "gp"]
                count += 1
            elif roll <= 100:
                treasure += [str(dieroll(1,10)*10) + "pp"] + [art(dieroll(1,4))] + [magicitem(dieroll(1,3), "minor")]
                count += 1
    return treasure


def gems(number):
    treasure = []
    roll = dper()
    count = 0
    while count < number:
        if roll <= 25:
            treasure += [str(dieroll(4,4)) + "gp in gems"]
            count += 1
        elif roll <= 50:
            treasure += [str(dieroll(2,4)*10) + "gp in gems"]
            count += 1
        elif roll <= 70:
            treasure += [str(dieroll(4,4)*10) + "gp in gems"]
            count += 1
        elif roll <= 90:
            treasure += [str(dieroll(2,4)*100) + "gp in gems"]
            count += 1
        elif roll <= 99:
            treasure += [str(dieroll(4,4)*100) + "gp in gems"]
            count += 1
        else:
            treasure += [str(dieroll(2,4)*1000) + "gp in gems"]
            count += 1
    return treasure

def art(number):
    roll = dper()
    treasure = []
    count = 0
    while count < number:
        if roll <= 10:
            treasure += [str(dieroll(1,10)*10) + "gp in art"]
            count += 1
        elif roll <= 25:
            treasure += [str(dieroll(3,6)*10) + "gp in art"]
            count += 1
        elif roll <= 40:
            treasure += [str(dieroll(1,6)*100) + "gp in art"]
            count += 1
        elif roll <= 50:
            treasure += [str(dieroll(1,10)*100) + "gp in art"]
            count += 1
        elif roll <= 60:
            treasure += [str(dieroll(2,6)*100) + "gp in art"]
            count += 1
        elif roll <= 70:
            treasure += [str(dieroll(3,6)*100) + "gp in art"]
            count += 1
        elif roll <= 80:
            treasure += [str(dieroll(4,6)*100) + "gp in art"]
            count += 1
        elif roll <= 85:
            treasure += [str(dieroll(5,6)*100) + "gp in art"]
            count += 1
        elif roll <= 90:
            treasure += [str(dieroll(1,4)*1000) + "gp in art"]
            count += 1
        elif roll <= 95:
            treasure += [str(dieroll(1,6)*1000) + "gp in art"]
            count += 1
        elif roll <= 99:
            treasure += [str(dieroll(2,4)*1000) + "gp in art"]
            count += 1
        else:
            treasure += [str(dieroll(2,6)*1000) + "gp in art"]
            count += 1
    return treasure

def magicitem(number,grade):
    #this refers to a minor magic item
    count = 0
    treasure = []
    while count < number:
        roll = dper()
        if grade == "minor":
            if roll <= 4:
                treasure += [armornshield("minor")]
                count += 1
            elif roll <= 9:
                treasure += [weapon("minor")]
                count += 1
            elif roll <= 44:
                treasure += [potion("minor")]
                count += 1
            elif roll <= 46:
                treasure += [ring("minor")]
                count += 1
            elif roll <= 81:
                treasure += [scroll("minor")]
                count += 1
            elif roll <= 91:
                treasure += [wand("minor")]
                count += 1
            else:
                treasure += [wonder("minor")]
                count += 1
        elif grade == "meduim":
            pass
        elif grade == "major":
            pass
    return treasure


def armornshield(grade):
    if grade == "minor":
        roll = dper()
        if roll <= 60:
            treasure = "+1 " + shieldtype()
        elif roll <= 80:
            treasure = "+1 " + armortype()
        elif roll <= 85:
            treasure = "+2 " + shieldtype()
        elif roll <= 87:
            treasure = "+2 " + armortype()
        elif roll <= 89:
            treasure = specarmor("minor")
        elif roll <= 91:
            treasure = specshield("minor")
        else:
            roll = dper()
            if roll <= 60:
                treasure = "+1 " + shieldtype() + shieldability("minor")
            elif roll <= 80:
                treasure = "+1 " + armortype() + armorability("minor")
            elif roll <= 85:
                treasure = "+2 " + shieldtype() + shieldability("minor")
            elif roll <= 87:
                treasure = "+2 " + armortype() + armorability("minor")
            elif roll <= 89:
                treasure = "+1 " + specarmor("minor")
            elif roll <= 91:
                treasure = "+1 " + specshield("minor")
            else:
                roll = dieroll(1,2)
                if roll == 1:
                    treasure = "+3" + shieldtype()
                else:
                    treasure = "+3" + armortype()
    return treasure


def weapon(grade):
    if grade == "minor":
        roll = dper()
        if roll <= 70:
            treasure = "+1 " + weapontype("minor", 0)
        elif roll <= 85:
            treasure = "+2 " + weapontype("minor", 0)
        elif roll <= 90:
            treasure = specweapon("minor")
        elif roll <= 100:
            roll = dper()
            if roll <= 70:
                treasure = "+1 " + weapontype("minor", 1)
            elif roll <= 85:
                treasure = "+2 " + weapontype("minor", 1)
            elif roll <= 90:
                treasure = "+1 " + specweapon("minor")
            elif roll <= 100:
                treasure = "+3 " + weapontype("minor", 0)
    elif grade == "meduim":
        pass
    elif grade == "major":
        pass
    return treasure

def weapontype(grade, ability):
    #ability is to determine if the item gets and ability 1 is yes 0 is no
    roll = dper()
    if ability == 0:
        if roll <= 70:
            roll = dper()
            if roll <= 4:
                treasure = "Dagger"
            elif roll <= 14:
                treasure = "Greataxe"
            elif roll <= 24:
                treasure = "Greatsword"
            elif roll <= 28:
                treasure = "Kama"
            elif roll <= 41:
                treasure = "Longsword"
            elif roll <= 45:
                treasure = "Mace, Light"
            elif roll <= 50:
                treasure = "Mace, Light"
            elif roll <= 54:
                treasure = "Nunchaku"
            elif roll <= 57:
                treasure = "Quarterstaff"
            elif roll <= 61:
                treasure = "Rapier"
            elif roll <= 66:
                treasure = "Scimitar"
            elif roll <= 70:
                treasure = "Shortspear"
            elif roll <= 74:
                treasure = "Siangham"
            elif roll <= 84:
                treasure = "Bastard Sword"
            elif roll <= 89:
                treasure = "Short Sword"
            elif roll <= 100:
                treasure = "Dwarven Waraxe"
        elif roll <= 80:
            roll = dper()
            uncommlist["Axe, Orc Double", "Axe, Orc Double", "Axe, Orc Double", "Battleaxe", "Battleaxe", "Battleaxe", "Battleaxe", "Chain, Spiked", "Chain, Spiked", "Chain, Spiked", "Club", "Club", "Crossbow, Hand", "Crossbow, Hand", "Crossbow, Hand", "Crossbow, Hand", "Crossbow, Repeating", "Crossbow, Repeating", "Crossbow, Repeating", "Dagger, Punching", "Dagger, Punching", "Falchion", "Falchion", "Flail, Dire", "Flail, Dire", "Flail, Dire", "Flail, Heavy", "Flail, Heavy", "Flail, Heavy", "Flail, Heavy", "Flail, Heavy", "Flail", "Flail", "Flail", "Flail", "Gauntlet", "Gauntlet", "Gauntlet, Spiked", "Gauntlet, Spiked", "Glaive", "Glaive", "Greatclub", "Greatclub", "Guisarme", "Guisarme", "Halberd", "Halberd", "Halberd", "Spear", "Spear", "Spear", "Spear", "Spear", "Spear", "Hammer, Gnome Hooked", "Hammer, Gnome Hooked", "Hammer, Gnome Hooked",
            "Hammer, Light", "Hammer, Light", "Handaxe", "Handaxe", "Kukri", "Kukri", "Kukri", "Lance", "Lance", "Lance", "Longspear", "Longspear", "Longspear", "Morning Star", "Morning Star", "Morning Star", "Net", "Net", "Pick, Heavy", "Pick, Heavy", "Pick, Light", "Pick, Light", "Ranseur", "Ranseur", "Sap", "Sap", "Scythe", "Scythe", "Shuriken, 50", "Shuriken, 50", "Sickle", "Sickle", "Sword, Two-Bladed", "Sword, Two-Bladed", "Sword, Two-Bladed", "Trident", "Trident", "Urgrosh, Dwarven", "Urgrosh, Dwarven", "Urgrosh, Dwarven", "Warhammer", "Warhammer", "Warhammer", "Whip", "Whip", "Whip"]
            treasure = uncommlist[roll - 1]
        elif roll <= 100:
            roll = dper()
            if roll <= 10:
                roll = dper()
                if roll <= 50:
                    treasure = "Arrows, 50"
                elif roll <= 80:
                    treasure = "Bolts, 50"
                elif roll <= 100:
                    treasure = "Bullets, 50"
            elif roll <= 15:
                treasure = "Throwing Axe"
            elif roll <= 25:
                treasure = "Crossbow, Heavy"
            elif roll <= 35:
                treasure = "Crossbow, Light"
            elif roll <= 39:
                treasure = "Dart"
            elif roll <= 41:
                treasure = "Javelin"
            elif roll <= 46:
                treasure = "Shortbow"
            elif roll <= 51:
                treasure = "Shortbow, Composite (+0)"
            elif roll <= 56:
                treasure = "Shortbow, Composite (+1)"
            elif roll <= 61:
                treasure = "Shortbow, Composite (+2)"
            elif roll <= 65:
                treasure = "Sling"
            elif roll <= 75:
                treasure = "Longbow"
            elif roll <= 80:
                treasure = "Longbow, Composite"
            elif roll <= 85:
                treasure = "Longbow, Composite (+1)"
            elif roll <= 90:
                treasure = "Longbow, Composite (+2)"
            elif roll <= 95:
                treasure = "Longbow, Composite (+3)"
            elif roll <= 100:
                treasure = "Longbow, Composite (+4)"
    elif ability == 1:
        if roll <= 70:
            roll = dper()
            if roll <= 4:
                treasure = "Dagger" + meleewability("minor")
            elif roll <= 14:
                treasure = "Greataxe" + meleewability("minor")
            elif roll <= 24:
                treasure = "Greatsword" + meleewability("minor")
            elif roll <= 28:
                treasure = "Kama" + meleewability("minor")
            elif roll <= 41:
                treasure = "Longsword" + meleewability("minor")
            elif roll <= 45:
                treasure = "Mace, Light"+ meleewability("minor")
            elif roll <= 50:
                treasure = "Mace, Light" + meleewability("minor")
            elif roll <= 54:
                treasure = "Nunchaku" + meleewability("minor")
            elif roll <= 57:
                treasure = "Quarterstaff" + meleewability("minor")
            elif roll <= 61:
                treasure = "Rapier" + meleewability("minor")
            elif roll <= 66:
                treasure = "Scimitar" + meleewability("minor")
            elif roll <= 70:
                treasure = "Shortspear" + meleewability("minor")
            elif roll <= 74:
                treasure = "Siangham" + meleewability("minor")
            elif roll <= 84:
                treasure = "Bastard Sword" + meleewability("minor")
            elif roll <= 89:
                treasure = "Short Sword" + meleewability("minor")
            elif roll <= 100:
                treasure = "Dwarven Waraxe" + meleewability("minor")
        elif roll <= 80:
            roll = dper()
            uncommlist = ["Axe, Orc Double", "Axe, Orc Double", "Axe, Orc Double", "Battleaxe", "Battleaxe", "Battleaxe", "Battleaxe", "Chain, Spiked", "Chain, Spiked", "Chain, Spiked", "Club", "Club", "Crossbow, Hand", "Crossbow, Hand", "Crossbow, Hand", "Crossbow, Hand", "Crossbow, Repeating", "Crossbow, Repeating", "Crossbow, Repeating", "Dagger, Punching", "Dagger, Punching", "Falchion", "Falchion", "Flail, Dire", "Flail, Dire", "Flail, Dire", "Flail, Heavy", "Flail, Heavy", "Flail, Heavy", "Flail, Heavy", "Flail, Heavy", "Flail", "Flail", "Flail", "Flail", "Gauntlet", "Gauntlet", "Gauntlet, Spiked", "Gauntlet, Spiked", "Glaive", "Glaive", "Greatclub", "Greatclub", "Guisarme", "Guisarme", "Halberd", "Halberd", "Halberd", "Spear", "Spear", "Spear", "Spear", "Spear", "Spear", "Hammer, Gnome Hooked", "Hammer, Gnome Hooked", "Hammer, Gnome Hooked",
            "Hammer, Light", "Hammer, Light", "Handaxe", "Handaxe", "Kukri", "Kukri", "Kukri", "Lance", "Lance", "Lance", "Longspear", "Longspear", "Longspear", "Morning Star", "Morning Star", "Morning Star", "Net", "Net", "Pick, Heavy", "Pick, Heavy", "Pick, Light", "Pick, Light", "Ranseur", "Ranseur", "Sap", "Sap", "Scythe", "Scythe", "Shuriken, 50", "Shuriken, 50", "Sickle", "Sickle", "Sword, Two-Bladed", "Sword, Two-Bladed", "Sword, Two-Bladed", "Trident", "Trident", "Urgrosh, Dwarven", "Urgrosh, Dwarven", "Urgrosh, Dwarven", "Warhammer", "Warhammer", "Warhammer", "Whip", "Whip", "Whip"]
            treasure = uncommlist[roll - 1] + meleewability("minor")
        elif roll <= 100:
            roll = dper()
            if roll <= 10:
                roll = dper()
                if roll <= 50:
                    treasure = "Arrows, 50" + randgedwability(grade)
                elif roll <= 80:
                    treasure = "Bolts, 50" + rangedwability(grade)
                elif roll <= 100:
                    treasure = "Bullets, 50" + rangedwability(grade)
                elif roll <= 15:
                    treasure = "Throwing Axe" + rangedwability(grade)
                elif roll <= 25:
                    treasure = "Crossbow, Heavy" + rangedwability(grade)
                elif roll <= 35:
                    treasure = "Crossbow, Light" + rangedwability(grade)
                elif roll <= 39:
                    treasure = "Dart" + rangedwability(grade)
                elif roll <= 41:
                    treasure = "Javelin"+ rangedwabiltiy(grade)
                elif roll <= 46:
                    treasure = "Shortbow" + rangedwability(grade)
                elif roll <= 51:
                    treasure = "Shortbow, Composite (+0)" + rangedwability(grade)
                elif roll <= 56:
                    treasure = "Shortbow, Composite (+1)" + rangedwability(grade)
                elif roll <= 61:
                    treasure = "Shortbow, Composite (+2)" + rangedwability(grade)
                elif roll <= 65:
                    treasure = "Sling" + rangedwability(grade)
                elif roll <= 75:
                    treasure = "Longbow" + rangedwability(grade)
                elif roll <= 80:
                    treasure = "Longbow, Composite" + rangedwability(grade)
                elif roll <= 85:
                    treasure = "Longbow, Composite (+1)" + rangedwability(grade)
                elif roll <= 90:
                    treasure = "Longbow, Composite (+2)" + rangedwability(grade)
                elif roll <= 95:
                    treasure = "Longbow, Composite (+3)" + rangedwability(grade)
                elif roll <= 100:
                    treasure = "Longbow, Composite (+4)" + rangedwability(grade)
    return treasure

def specweapon(grade):
    roll = dper()
    if grade == "minor":
        if roll <= 15:
            treasure = "Sleep Arrow"
        elif roll <= 25:
            treasure = "Screaming Bolt"
        elif roll <= 45:
            treasure = "Masterword Silver Dagger"
        elif roll <= 65:
            treasure = "Cold Iron Longsword"
        elif roll <= 75:
            treasure = "Javelin of Lightning"
        elif roll <= 80:
            treasure = sarrow()
        elif roll <= 90:
            treasure = "Adamantine Dagger"
        elif roll <= 100:
            treasure = "Adamantine Battleaxe"
    elif grade == "meduim":
        if roll <= 9:
            treasure = "Javelin of Lightning"
        elif roll <= 15:
            treasure = sarrow()
        elif roll <= 24:
            treasure = "Adamantine Dagger"
        elif roll <= 33:
            treasure = "Adamantine Battleaxe"
        elif roll <= 37:
            treasure = "Greater " + sarrow()
        elif roll <= 40:
            treasure = "Shatterspike"
        elif roll <= 46:
            treasure = "Dagger of Venom"
        elif roll <= 51:
            treasure = "Trident of Warning"
        elif roll <= 57:
            treasure = "Assassin's Dagger"
        elif roll <= 62:
            treasure = "Shifter's Sorrow"
        elif roll <= 66:
            treasure = "Trident of Fish Command"
        elif roll <= 74:
            treasure = "Flame Tongue"
        elif roll <= 79:
            treasure = "Luck Blade (0 wishes)"
        elif roll <= 86:
            treasure = "Sword of Subtlety"
        elif roll <= 91:
            treasure = "Sword of the Planes"
        elif roll <= 95:
            treasure = "Nine Lives Stealer"
        elif roll <= 98:
            treasure = "Sword of Life Stealing"
        elif roll <= 100:
            treasure = "Oathbow"
    elif grade == "major":
        pass
    return treasure
def meleewability(grade):
    roll = dper()
    if grade == "minor":
        if roll <= 10:
            treasure = bane()
        elif roll <= 17:
            treasure = " Defending"
        elif roll <= 27:
            treasure = " Flaming"
        elif roll <= 37:
            treasure = " Frost"
        elif roll <= 47:
            treasure = " Shock"
        elif roll <= 56:
            treasure = " Ghost Touch"
        elif roll <= 67:
            treasure = " Keen"
        elif roll <= 71:
            treasure = " Ki Focus"
        elif roll <= 75:
            treasure = " Merciful"
        elif roll <= 82:
            treasure = " Mighty Cleaving"
        elif roll <= 87:
            treasure = " Spell Storing"
        elif roll <= 91:
            treasure = " Throwing"
        elif roll <= 95:
            treasure = " Thundering"
        elif roll <= 99:
            treasure = " Vicious"
        else:
            treasure = meleewability("minor") + meleewability("minor")
    return treasure
def rangedwability(grade):
    pass
def sarrow():
    roll = dper()
    treasure = "Slaying Arrow, "
    if roll <= 5:
        treasure + "Aberrations"
    elif roll <= 9:
        treasure + "Animals"
    elif roll <= 16:
        treasure + "Constructs"
    elif roll <= 22:
        treasure + "Dragons"
    elif roll <= 27:
        treasure + "Elementals"
    elif roll <= 32:
        treasure + "Fey"
    elif roll <= 39:
        treasure + "Giants"
    elif roll == 40:
        treasure + "Aquatic Humanoids"
    elif roll <= 42:
        treasure + "Dwarfs"
    elif roll <= 44:
        treasure + "Elves"
    elif roll == 45:
        treasure + "Gnolls"
    elif roll == 46:
        treasure + "Gnomes"
    elif roll <= 49:
        treasure + "Goblins"
    elif roll == 50:
        treasure + "Halfings"
    elif roll <= 54:
        treasure + "Humans"
    elif roll <= 57:
        treasure + "Reptilian"
    elif roll <= 60:
        treasure + "Orcs"
    elif roll <= 65:
        treasure + "Magical Beasts"
    elif roll <= 70:
        treasure + "Monstrous Humanoids"
    elif roll <= 72:
        treasure + "Oozes"
    elif roll == 73:
        treasure + "Air Outsiders"
    elif roll <= 76:
        treasure + "Chaotic Outsiders"
    elif roll == 77:
        treasure + "Earth Outsiders"
    elif roll <= 80:
        treasure + "Evil Outsiders"
    elif roll == 81:
        treasure + "Fire Outsiders"
    elif roll <= 84:
        treasure + "Good Outsiders"
    elif roll <= 87:
        treasure + "Lawful Outsiders"
    elif roll == 88:
        treasure + "Water Outsiders"
    elif roll <= 90:
        treasure + "Plants"
    elif roll <= 98:
        treasure + "Undead"
    elif roll <= 100:
        treasure + "Vermin"
    return treasure

def potion(grade):
    roll = dper()
    if grade == "minor":
        if roll <= 10:
            treasure = "Cure Light Wounds (potion)"
        elif roll <= 13:
            treasure = "Endure Elements (potion)"
        elif roll <= 15:
            treasure = "Hide from Animals (potion)"
        elif roll <= 17:
            treasure = "Hide from Undead (potion)"
        elif roll <= 19:
            treasure = "Jump (potion)"
        elif roll <= 22:
            treasure = "Mage Armor (potion)"
        elif roll <= 25:
            treasure = "Magic Fang (potion)"
        elif roll == 26:
            treasure = "Magic Stone (oil)"
        elif roll <= 29:
            treasure = "Magic Weapon (oil)"
        elif roll == 30:
            treasure = "Pass Without Trace (potion)"
        elif roll <= 32:
            treasure = "Protection from (Alignment) (potion)"
        elif roll <= 34:
            treasure = "Remove Fear (potion)"
        elif roll == 35:
            treasure = "Sanctuary (potion)"
        elif roll <= 38:
            treasure = "Shield of Faith +2 (potion)"
        elif roll == 39:
            treasure = "Shillelagh (oil)"
        elif roll <= 41:
            treasure = "Bless Weapon (oil)"
        elif roll <= 44:
            treasure = "Enlarge Person (potion)"
        elif roll == 45:
            treasure = "Reduce Person (potion)"
        elif roll <= 47:
            treasure = "Aid (potion)"
        elif roll <= 50:
            treasure = "Barkskin +2 (potion)"
        elif roll <= 53:
            treasure = "Bear's Endurance (potion)"
        elif roll <= 56:
            treasure = "Blur (potion)"
        elif roll <= 59:
            treasure = "Bull's Strength (potion)"
        elif roll <= 62:
            treasure = "Cat's Grace (potion)"
        elif roll <= 67:
            treasure = "Cure Moderate Wounds (potion)"
        elif roll == 68:
            treasure = "Darkness (oil)"
        elif roll <= 71:
            treasure = "Darkvision (potion)"
        elif roll <= 74:
            treasure = "Delay Poison (potion)"
        elif roll <= 76:
            treasure = "Eagle's Splendor (potion)"
        elif roll <= 78:
            treasure = "Fox's Cunning (potion)"
        elif roll <= 81:
            treasure = "Invisibility (potion or oil)"
        elif roll <= 84:
            treasure = "Lesser Restoration (potion)"
        elif roll <= 86:
            treasure = "Levitate (potion or oil)"
        elif roll == 87:
            treasure = "Misdirection (potion)"
        elif roll <= 89:
            treasure = "Owl's Wisdom (potion)"
        elif roll <= 91:
            treasure = "Protection from Arrows 10/magic (potion)"
        elif roll <= 93:
            treasure = "Remove Paralysis (potion)"
        elif roll <= 96:
            treasure = "Resist Enery (type) 10 (potion)"
        elif roll == 97:
            treasure = "Shield of Faith +3 (potion)"
        elif roll <= 99:
            treasure = "Spider Climb (potion)"
        elif roll == 100:
            treasure = "Undetectable Alignment (potion)"
    return treasure

def ring(grade):
    roll = dper()
    if grade  == "minor":
        if roll <= 18:
            treasure = "Ring of Protection +1"
        elif roll <= 28:
            treasure = "Ring of Feather Falling"
        elif roll <= 36:
            treasure = "Ring of Sustenance"
        elif roll <= 44:
            treasure = "Ring of Climbing"
        elif roll <= 52:
            treasure = "Ring of Jumping"
        elif roll <= 60:
            treasure = "Ring of Swimming"
        elif roll <= 70:
            treasure = "Ring of Counterspells"
        elif roll <= 75:
            treasure = "Ring of Mind Shielding"
        elif roll <= 80:
            treasure = "Ring of Protection +2"
        elif roll <= 85:
            treasure = "Ring of Force Shield"
        elif roll <= 90:
            treasure = "Ring of the Ram"
        elif roll <= 93:
            treasure = "Ring of Animal Friendship"
        elif roll <= 96:
            treasure = "Ring of Energy Resistance, Major"
        elif roll <= 98:
            treasure = "Ring of Chameleon Power"
        elif roll <= 100:
            treasure = "Ring of Water Walking"
    return treasure

def scroll(grade):
    roll = dper()
    if roll <= 70:
        if grade == "minor":
            roll = dper()
            if roll <= 5:
                treasure = "0th-Level Arcane Scroll"
            elif roll <= 50:
                treasure = "1st-Level Arcane Scroll"
            elif roll <= 95:
                treasure = "2nd-Level Arcane Scroll"
            else:
                treasure = "3rd-Level Arcane Scroll"
        elif grade == "meduim":
            pass
        elif grade == "major":
            pass
    else:
        if grade == "minor":
            roll = dper()
            if roll <= 5:
                treasure = "0th-Level Divine Scroll"
            elif roll <= 50:
                treasure = "1st-Level Divine Scroll"
            elif roll <= 95:
                treasure = "2nd-Level Divine Scroll"
            else:
                treasure = "3rd-Level Divine Scroll"
        elif grade == "meduim":
            pass
        elif grade == "major":
            pass
    return treasure
def wand(grade):
    roll = dper()
    treasure = "Wand of "
    if grade == "minor":
        if roll <= 2:
            treasure += "Detect Magic"
        elif roll <= 4:
            treasure += " Light"
        elif roll <= 7:
            treasure += "Burning Hands"
        elif roll <= 10:
            treasure += "Charm Animal"
        elif roll <= 13:
            treasure += "Charm Person"
        elif roll <= 16:
            treasure += "Color Spray"
        elif roll <= 19:
            treasure += "Cure Light Wounds"
        elif roll <= 22:
            treasure += "Detect Secret Doors"
        elif roll <= 25:
            treasure += "Enlarge Person"
        elif roll <= 28:
            treasure += "Magic Missle (1st)"
        elif roll <= 31:
            treasure += "Shocking Grasp"
        elif roll <= 34:
            treasure += "Summon Monster I"
        elif roll <= 36:
            treasure += "Magic Missle (3rd)"
        elif roll == 37:
            treasure += "Magic Missle(5th)"
        elif roll <= 40:
            treasure += "Bear's Endurance"
        elif roll <= 43:
            treasure += "Bull's Strength"
        elif roll <= 46:
            treasure += "Cat's Grace"
        elif roll <= 49:
            treasure += "Cure Moderate Wounds"
        elif roll <= 51:
            treasure += "Darkness"
        elif roll <= 54:
            treasure += "Daze Monster"
        elif roll <= 57:
            treasure += "Delay Poison"
        elif roll <= 60:
            treasure += "Eagle's Splendor"
        elif roll <= 63:
            treasure += "False Life"
        elif roll <= 66:
            treasure += "Fox's Cunning"
        elif roll <= 68:
            treasure += "Ghoul Touch"
        elif roll <= 71:
            treasure += "Hold Person"
        elif roll <= 74:
            treasure += "Invisibility"
        elif roll <= 77:
            treasure += "Knock"
        elif roll <= 80:
            treasure += "Levitate"
        elif roll <= 83:
            treasure += "Acid Arrows"
        elif roll <= 86:
            treasure += "Mirror Image"
        elif roll <= 89:
            treasure += "Owl's Wisdom"
        elif roll <= 91:
            treasure += "Shatter"
        elif roll <= 94:
            treasure += "Silence"
        elif roll <= 97:
            treasure += "Summon Monster II"
        elif roll <= 100:
            treasure += "Web"
    elif grade == "meduim":
        pass
    elif grade == "major":
        pass
    return treasure
def wonder(grade):
    roll = dper()
    if grade == "minor":
        minorlist = ["Feather Token, Anchor", "Universal Solvent", "Elixir of Love", "Unguent of Timelessness", "Feather Token, Fan", "Dust of Tracelessness", "Elixir of Hiding", "Elixir of Sneaking", "Elixir of Swimming", "Elixir of Vision", "Silversheen", "Feather Token, Bird", "Feather Token, Tree", "Feather Token, Swan Boat", "Elixir of Truth", "Feather Token, Whip", "Dust of Dryness", "Bag of Tricks, Gray", "Hand of the Mage", "Bracers of Armor +1", "Cloak of Resistance +1", "Pearl of Power, 1st-Level", "Phylactery of Faithfulness", "Salve of Slipperiness", "Elixir of Fire Breath", "Pipes of the Sewers", "Dust of Illusion", "Goggles of Minute Seeing", "Brooch of Shielding", "Necklace of Fireballs type I", "Dust of Appearance", "Hat of Disguise", "Pipes of Sounding", "Efficient Quiver", "Amulet of Natural Armor +1", "Handy Haversack", "Horn of Fog", "Elemental Gem", "Robe of Bones", "Sovereign Glue", "Bag of Holding Type I", "Boots of Elvenkind", "Boots of the Winterlands",
        "Candle of Truth", "Cloak of Elvenkind", "Eyes of the Eagle", "Scarab, Golembane", "Necklace of Fireballs Type II", "Stone of Alarm", "Bag of Tricks, Rust", "Bead of Force", "Chime of Opening", "Horseshoes of Speed", "Rope of Climbing", "Dust of Disappearance", "Lens of Detection", "Figurine of Wondrous Power, Silver Raven", "Amulet of Health +2", "Bracers of Armor +2", "Cloak of Charisma +2", "Cloak of Resistance +2", "Gauntlets of Ogre Power", "Gloves of Arrow Snaring", "Gloves of Dexterity +2", "Headband of Intellect +2", "Ioun Stone, Clear Spindle", "Restorative Ointment", "Marvelous Pigments", "Pearl of Power, 2nd-Level", "Periapt of Wisdom +2", "Stone Salve", "Necklace of Fireballs Type III", "Circlet of Persuasion", "Slippers of Spider Climbing", "Incense of Meditation", "Bag of Holding Type II", "Bracers of Archery, Lesser", "Ioun Stone, Dusty Rose Prism", "Helm of Comprehend Languages and Read Magic", "Vest of Escape", "Eversmoking Bottle", "Sustaining Spoon", "Necklace of Fireballs Type IV",
        "Boots of Striding and Springing", "Wind Fan", "Necklace of Fireballs Type V", "Amulet of Mighty Fists +1", "Horseshoes of a Zephyr", "Pipes of Haunting", "Gloves of Swimming and Climbing", "Bag of Tricks, Tan", "Circlet of Blasting, Minor", "Horn of Goodness/Evil", "Shrouds of Disintegration", "Robe of Useful Items", "Boat, Folding", "Cloak of the Manta Ray", "Bottle of Air", "Bag of Holding Type III", "Periapt of Health"]
        treasure = minorlist[roll - 1]
    elif grade == "meduim":
        pass
    elif grade == "major":
        pass
    return treasure

def shieldtype():
    roll = dper()
    if roll <= 10:
        shield = "Buckler"
    elif roll <= 15:
        shield = "Light Wooden Shield"
    elif roll <= 20:
        shield = "Light Steel Shield"
    elif roll <= 30:
        shield = "Heavy Wooden Shield"
    elif roll <= 95:
        shield = "Heavy Steel Shield"
    else:
        shield = "Tower Shield"
    return shield

def armortype():
    roll = dper()
    if roll == 1:
        armor = "Padded"
    elif roll == 2:
        armor = "Leather"
    elif roll <= 17:
        armor = "Studded Leather"
    elif roll <= 32:
        armor = "Chain Shirt"
    elif roll <= 42:
        armor = "Hide"
    elif roll == 43:
        armor = "Scale Mail"
    elif roll == 44:
        armor = "Chainmail"
    elif roll <= 57:
        armor = "Breastplate"
    elif roll == 58:
        armor = "Splint Mail"
    elif roll == 59:
        armor = "Banded Mail"
    elif roll == 60:
        armor = "Half-Plate"
    else:
        armor = "Full Plate"
    return armor

def specshield(grade):
    roll = dper()
    if grade == "minor":
        if roll <= 30:
            treasure = "Darkwood Buckler"
        elif roll <= 80:
            treasure = "Darkwood Shield"
        elif roll <= 95:
            treasure = "Mithral Heavy Shield"
        elif roll <= 100:
            treasure = "Caster's Shield"
    elif grade == "meduim":
        if roll <= 20:
            treasure = "Darkwood Buckler"
        elif roll <= 45:
            treasure = "Darkwood Shield"
        elif roll <= 70:
            treasure = "Mithral Heavy Shield"
        elif roll <= 85:
            treasure = "Caster's Shield"
        elif roll <= 90:
            treasure = "Spined Shield"
        elif roll <= 95:
            treasure = "Lion's Shield"
        elif roll <= 100:
            treasure = "Winged Shield"
    elif grade == "major":
        pass
    return treasure
def specarmor(grade):
    roll = dper()
    if grade == "minor":
        if roll <= 50:
            treasure = "Mithral Shirt"
        elif roll <= 80:
            treasure = "Dragonhide Plate"
        elif roll <= 100:
            treasure = "Elven Chain"
    elif grade == "meduim":
        if roll <= 25:
            treasure = "Mithral Shirt"
        elif roll <= 45:
            treasure = "Dragonhide Plate"
        elif roll <= 57:
            treasure = "Elven Chain"
        elif roll <= 67:
            treasure = "Rhino Hide"
        elif roll <= 82:
            treasure = "Adamantine Breastplate"
        elif roll <= 97:
            treasure = "Dwarven Plate"
        elif roll <= 100:
            treasure = "Banded Mail of Luck"
    elif grade == "major":
        pass
    return treasure
def shieldability(grade):
    pass
def armorability(grade):
    roll = dper()
    if grade == "minor":
        if roll <= 25:
            treasure = " Glamered"
        elif roll <= 32:
            treasure = " Light Fortification"
        elif roll <= 52:
            treasure = " Slick"
        elif roll <= 72:
            treasure = " Shadow"
        elif roll <= 92:
            treasure = " Silent Moves"
        elif roll <= 96:
            treasure = " Spell Resistance (13)"
        elif roll == 97:
            treasure = " Improved Slick"
        elif roll == 98:
            treasure = " Improved Shadow"
        elif roll == 99:
            treasure = " Improved Silent Moves"
    return treasure

def dieroll(number, size):
    import random
    roll = 0
    n = number
    while n > 0:
        roll = roll + (random.randint(1, size))
        n -= 1
    return roll

def dper():
    import random
    a = random.randint(1,10)
    b = random.randint(1,10)
    if a == 10 and b == 10:
        return 100
    elif a == 10 and b < 10:
        return b
    elif a < 10 and b == 10:
        return (a * 10)
    else:
        return ((a * 10) + b)


if __name__ == '__main__':
    main()