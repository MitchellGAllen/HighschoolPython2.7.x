#-------------------------------------------------------------------------------
# Name:        DnD Text Adventure
# Purpose: Fun
#
# Author:      CreationCatalyst
#
# Created:     06/02/2013
# Copyright:   (c) mallen 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    done = "false"
    time = 1
    name = ""
    Str = 0
    Dex = 0
    Con = 0
    Int = 0
    Wis = 0
    Cha = 0
    Class = ""
    statlist = [] #this is a container for ability core generation
    featlist = ["Power Attack", "Point Blank Shot", "Toughness"]
    fighterfeatlist = ["Power Attack", "Point Blank Shot", "Rapid Shot", "Toughness"]
    charfeats = []
    rten = "false" #this marks whether time 10 has been run or not
    rel = "false" #this does so for time 11
    hpa = "false" #for determining whether the player has the option to Power Attack
    #these are the player's saves
    fsav = 0
    rsav = 0
    wsav = 0
    init = 0 #this is the player's initiative mod
    hp = 0 #player's hit points
    equ = [] #this is the player's equipped items
    inv = [] #this is the player's inventory

    while done == "false":
        if time == 1:
            print "Type an option's number to select that option or type 0 to quit or ~ to restart or blank to repeat step"
            input = raw_input("""
            1:Start
            0:Quit
            """)
            if input == "0":
                done = "true"
            elif input == "1":
                time += 1
            elif input == "~":
                time = 1

        elif time == 2:
            print
            print "Welcome to Alandale stranger. Whats your name?"
            input = raw_input("Enter Name : ")
            if input == "0":
                done = "true"
            elif input == "~":
                time = 1
            elif input:
                name = input
                time += 1

        elif time == 3:
            print
            print "Hello " + name + " you look like an Adventurer tell me about yourself."
            input = raw_input("""Choose your class
            1:Fighter
            2:Monk
            """)
            if input == "1":
                Class = "Fighter"
                time += 1
            elif input == "2":
                Class = "Monk"
                time += 1
            elif input == "0":
                done = "true"
            elif input == "~":
                time = 1
        elif time == 4:
            print
            print "So your " + name + " the " + Class
            print "How good are you though?"
            statlist = [stat(),stat(),stat(),stat(),stat(),stat()]
            print
            print "1 : " + str(statlist[0]), "| 2 : " + str(statlist[1]), "| 3 : " + str(statlist[2]), "| 4 : " + str(statlist[3]), "| 5 : " + str(statlist[4]), "| 6 : " + str(statlist[5])
            input = raw_input("""Choose your Strength from this list
            """)
            if input == "0":
                done = "true"
            elif input == "~":
                time = 1
            elif input == "":
                time = 4
            elif int(input) <= 6 and int(input) >= 1:
                Str = statlist.pop(int(input)-1)
                time += 1
        elif time == 5:
            print
            print "So your strength is " + str(Str)
            print "But how about dexterity?"
            print
            print "1 : " + str(statlist[0]), "| 2 : " + str(statlist[1]), "| 3 : " + str(statlist[2]), "| 4 : " + str(statlist[3]), "| 5 : " + str(statlist[4])
            input = raw_input("""Choose your Dexterity from this list
            """)
            if input == "0":
                done = "true"
            elif input == "~":
                time = 1
            elif int(input) <= 5 and int(input) >= 1:
                Dex = statlist.pop(int(input)-1)
                time += 1
            else:
                time = 5
        elif time == 6:
            print
            print"So your dexterity is " + str(Dex)
            print "But how about constitution?"
            print
            print "1 : " + str(statlist[0]), "| 2 : " + str(statlist[1]), "| 3 : " + str(statlist[2]), "| 4 : " + str(statlist[3])
            input = raw_input("""Choose your Constitution from this list
            """)
            if input == "0":
                done = "true"
            elif input == "~":
                time = 1
            elif int(input) <= 4 and int(input) >= 1:
                Con = statlist.pop(int(input)-1)
                time += 1
            else:
                time = 6
        elif time == 7:
            print
            print "So your constitution is " + str(Con)
            print "But how about Intelligence?"
            print
            print "1 : " + str(statlist[0]), "| 2 : " + str(statlist[1]), "| 3 : " + str(statlist[2])
            input = raw_input("""Choose your Intelligence from this list
            """)
            if input == "0":
                done = "true"
            elif input == "~":
                time = 1
            elif int(input) <= 3 and int(input) >= 1:
                Int = statlist.pop(int(input)-1)
                time += 1
            else:
                time = 7
        elif time == 8:
            print
            print "So your Intelligence is " + str(Int)
            print "But how about Wisdom?"
            print
            print "1 : " + str(statlist[0]), "| 2 : " + str(statlist[1])
            input = raw_input("""Choose your Wisdom from this list
            """)
            if input == "0":
                done == "true"
            elif input == "~":
                time = 1
            elif int(input) <= 2 and int(input) >= 1:
                Wis = statlist.pop(int(input)-1)
                Cha = statlist.pop(0)
                time += 1
            else:
                time= 8
        elif time == 9:
            print
            print "So your Strength is " + str(Str) + "?"
            print "And your Dexterity is " + str(Dex) + "?"
            print "And your Constitution is " + str(Con) + "?"
            print "And your Intelligence is " + str(Int) + "?"
            print "And your Wisdom is " + str(Wis) + "?"
            print "And your Charisma is " + str(Cha) + "?"
            print """
            1 : correct
            2 : start over stat generation
            0 : quit
            ~ : restart
            """
            input = raw_input("")
            if input == "0":
                done = "true"
            elif input == "~":
                time = 1
            elif input == "1":
                time += 1
                rten = "false"
            elif input == "2":
                time = 4
        elif time == 10:
            if rten == "false":
                print
                print "You look like someone with a few tricks."
                print
                print "1 : " + featlist[0], "| 2 : " + featlist[1], "| 3 : " + featlist[2]
                input = raw_input("""Choose a feat from this list
                """)
                if input == "1":
                    if Str >= 13:
                        charfeats += [featlist[0]]
                        if Class == "Fighter":
                            time += 1
                        else:
                            time += 2
                        hpa = "true"
                        rel = "false"
                    else:
                        print
                        print "You don't look strong enough for that"
                        time = 10
                        rten = "true"
                elif input == "2":
                    charfeats += [featlist[1]]
                    if Class == "Fighter":
                        time += 1
                    else:
                        time += 2
                    rel = "false"
                elif input == "3":
                    charfeats += [featlist[2]]
                    if Class == "Fighter":
                        time += 1
                    else:
                        time += 2
                    rel = "false"
                elif input == "0":
                    done = "true"
                elif input == "~":
                    time = 1
            else:
                print "1 : " + featlist[0], "| 2 : " + featlist[1], "| 3 : " + featlist[2]
                input = raw_input("""Choose a feat from this list
                """)
                if input == "1":
                    if int(Str) >= 13:
                        charfeats += [featlist[0]]
                        time += 1
                        hpa = "true"
                        rel = "false"
                    else:
                        print
                        print "You don't look strong enough for that"
                        time = 10
                        rten = "true"
                elif input == "2":
                    charfeats += [featlist[1]]
                    time += 1
                    rel = "false"
                elif input == "3":
                    charfeats += [featlist[2]]
                    time += 1
                    rel = "false"
                elif input == "0":
                    done = "true"
                elif input == "~":
                    time = 1
        elif time == 11 and Class == "Fighter":
            if rel == "false":
                print
                print "A fighter like yourself must know more than just basic stuff right?"
                print
                print "1 : " + fighterfeatlist[0], "| 2 : " + fighterfeatlist[1], "| 3 : " + fighterfeatlist[2], "| 4 : " + fighterfeatlist[3]
                input = raw_input("""Choose a bonus feat from this list
                """)
                if input == "1":
                    if featcheck("Power Attack", charfeats) == "true":
                        print
                        print "Looks like you already have that feat"
                        time = 11
                        rel = "true"
                    elif Str >= 13:
                        charfeats += [fighterfeatlist[0]]
                        time += 1
                        hpa = "true"
                    else:
                        print
                        print "You don't look strong enough for that"
                        time = 11
                        rel = "true"
                elif input == "2":
                    if featcheck("Point Blank Shot", charfeats) == "true":
                        print
                        print "Looks like you already have that feat"
                        time = 11
                        rel = "true"
                    else:
                        charfeats += [fighterfeatlist[1]]
                        time += 1
                elif input == "3":
                    if Dex >= 13 and featcheck("Point Blank Shot", charfeats) == "true":
                        charfeats += [fighterfeatlist[2]]
                        time += 1
                    elif Dex < 13:
                        print
                        print "You don't look agile enough for that"
                        time = 11
                        rel = "true"
                    elif featcheck("Point Blank Shot", charfeats) == "false":
                        print
                        print "Don't you need the Point Blank Shot technique for that?"
                        time = 11
                        rel = "true"
                elif input == "4":
                    if featcheck("Toughness", charfeats) == "true":
                        print
                        print "Looks like you already have that feat"
                        time = 11
                        rel = "true"
                    else:
                        charfeats += [fighterfeatlist[3]]
                        time += 1
                elif input == "0":
                    done = "true"
                elif input == "~":
                    time = 1
            else:
                print "1 : " + fighterfeatlist[0], "| 2 : " + fighterfeatlist[1], "| 3 : " + fighterfeatlist[2], "| 4 : " + fighterfeatlist[3]
                input = raw_input("""Choose a bonus feat from this list
                """)
                if input == "1":
                    if featcheck("Power Attack", charfeats) == "true":
                        print
                        print "Looks like you already have that feat"
                        time = 11
                        rel = "true"
                    elif Str >= 13:
                        charfeats += [fighterfeatlist[0]]
                        time += 1
                        hpa = "true"
                    else:
                        print
                        print "You don't look strong enough for that"
                        time = 11
                        rel = "true"
                elif input == "2":
                    if featcheck("Point Blank Shot", charfeats) == "true":
                        print
                        print "Looks like you already have that feat"
                        time = 11
                        rel = "true"
                    else:
                        charfeats += [fighterfeatlist[1]]
                        time += 1
                elif input == "3":
                    if Dex >= 13 and featcheck("Point Blank Shot", charfeats) == "true":
                        charfeats += [fighterfeatlist[2]]
                        time += 1
                    elif Dex < 13:
                        print
                        print "You don't look agile enough for that"
                        time = 11
                        rel = "true"
                    elif featcheck("Point Blank Shot", charfeats) == "false":
                        print
                        print "Don't you need the Point Blank Shot technique for that?"
                        time = 11
                        rel = "true"
                elif input == "4":
                    if featcheck("Toughness", charfeats) == "true":
                        print
                        print "Looks like you already have that feat"
                        time = 11
                        rel = "true"
                    else:
                        charfeats += [fighterfeatlist[3]]
                        time += 1
                elif input == "0":
                    done = "true"
                elif input == "~":
                    time = 1

        elif time == 12:
            if Class == "Fighter":
                equ = ["Scale Mail", "Longsword", "Light Steel Shield"]
                inv = []
                time += 1
            elif Class == "Monk":
                equ = ["Monk Robe"]
                inv = ["Potion of Cure Light Wounds"]
                time += 1


        elif time == 13:
            if Class == "Fighter":
                fsav += 2 + stat_bonus(Con)
                rsav += stat_bonus(Dex)
                wsav += stat_bonus(Wis)
                init += stat_bonus(Dex)
                time += 1
                if featcheck("Toughness", charfeats) == "true":
                    hp += stat_bonus(Con) + 13
                else:
                    hp += stat_bonus(Con) + 10

            elif Class == "Monk":
                fsav += 2 + stat_bonus(Con)
                rsav += 2 + stat_bonus(Dex)
                wsav += 2 + stat_bonus(Wis)
                init += stat_bonus(Dex)
                time += 1
                if featcheck("Toughness", charfeats) == "true":
                    hp += stat_bonus(Con) + 11
                else:
                    hp += stat_bonus(Con) + 8
        elif time == 14:
            ac = acref(Class, Dex) #player's armor class
            print
            print "So your capabilities are as follows"
            print name + " the " + Class
            print "Strength : " + str(Str)
            print "Dexterity : " + str(Dex)
            print "Constitution : " + str(Con)
            print "Intelligence : " + str(Int)
            print "Wisdom : " + str(Wis)
            print "Charisma : " + str(Cha)
            print "Hit Points : " + str(hp)
            print "Saves"
            print "Fortitude : " + str(fsav)
            print "Reflex : " + str(rsav)
            print "Will : " + str(wsav)
            print "Armor Class : " + str(ac)
            print "Initiative : " + str(init)
            print "Equipment"
            print equ
            print "Inventory"
            print inv
            print "Feats"
            print charfeats
            print
            print """
            1 : correct
            0 : quit
            ~ : restart
            """
            input = raw_input("")
            if input == "0":
                done = "true"
            elif input == "~":
                time = 1
            elif input == "1":
                time += 1


#this is a use of a cure wounds spell effect whether its from a caster or a potion
#type is the specific cure spell (eg light, moderate, serious) and level is the caster level of the caster who casts the spell or creates the item
def cw(type,level):
    hp += dieroll(type + (1 * level),(type * 8) + (1 * level))

#this refreshs the armor class score when called
def acref(Class, Dex):
    if Class == "Fighter":
        if stat_bonus(Dex) > 3:
            return 18
        else:
            return 15 + stat_bonus(Dex)
    elif Class == "Monk":
        return 11 + stat_bonus(Dex)

def featcheck(feat, charfeats):
    if any(feat in s for s in charfeats):
        return "true"
    else:
        return "false"

#this determines the stat bonus gained from ability scores
def stat_bonus(stat):
    return (stat - 10)/2

def dieroll(number, size):
    import random
    roll = 0
    n = number
    while n > 0:
        roll = roll + (random.randint(1, size))
        n -= 1
    return roll

def stat():
    import random
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    roll = [roll1, roll2, roll3, roll4]
    roll.sort()
    return roll[1] + roll[2] + roll[3]

if __name__ == '__main__':
    main()
